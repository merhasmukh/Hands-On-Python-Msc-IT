from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta, timezone


app = FastAPI(title="Simple JWT Authentication Demo")


# ============================================================
# JWT Configuration
# ============================================================

SECRET_KEY = "gggggj6yt6o"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30


# OAuth2PasswordBearer reads:
# Authorization: Bearer <token>
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# ============================================================
# Fake Database
# ============================================================

users_db = {}


# ============================================================
# Pydantic Models
# ============================================================

class UserSignup(BaseModel):
    username: str
    password: str
    full_name: str


class UserLogin(BaseModel):
    username: str
    password: str


class User(BaseModel):
    username: str
    full_name: str


# ============================================================
# 1. SIGNUP
# ============================================================

@app.post("/signup")
def signup(user: UserSignup):

    # Check if user already exists
    if user.username in users_db:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Store user
    # NOTE: Password is stored directly only for classroom demo.
    # Real applications must hash passwords.
    users_db[user.username] = {
        "username": user.username,
        "password": user.password,
        "full_name": user.full_name
    }

    return {
        "message": "User created successfully",
        "username": user.username
    }


# ============================================================
# 2. LOGIN → GENERATE REAL JWT
# ============================================================

@app.post("/login")
def login(user: UserLogin):

    # Find user
    db_user = users_db.get(user.username)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Check password
    if user.password != db_user["password"]:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Token expiration time
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=TOKEN_EXPIRE_MINUTES
    )

    # JWT payload
    payload = {
        "sub": user.username,
        "name": db_user["full_name"],
        "exp": expire
    }

    # Generate JWT
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ============================================================
# 3. GET CURRENT USER FROM JWT
# ============================================================

def get_current_user(token: str = Depends(oauth2_scheme)):

    try:

        # Decode JWT
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        # Find user
        user = users_db.get(username)

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user

    except jwt.ExpiredSignatureError:

        raise HTTPException(
            status_code=401,
            detail="Token has expired"
        )

    except jwt.InvalidTokenError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


# ============================================================
# 4. PROTECTED GET API
# ============================================================

@app.get("/profile")
def get_profile(
    current_user: dict = Depends(get_current_user)
):

    return {
        "message": "Authentication successful!",
        "username": current_user["username"],
        "full_name": current_user["full_name"]
    }


# ============================================================
# Run
# ============================================================

# uvicorn app:app --reload