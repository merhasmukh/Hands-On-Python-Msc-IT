from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import time

app = FastAPI(title="Auth and Middleware Demo")

# ===========================================================================
# 1. CORS Middleware Example
# ===========================================================================
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===========================================================================
# 2. Custom Middleware Example
# ===========================================================================
from fastapi import Request
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    # Add a custom header to every response
    response.headers["X-Process-Time"] = str(process_time)
    return response

# ===========================================================================
# 3. Simple JWT / OAuth2 Auth Example
# ===========================================================================
# This creates the standard OAuth2 flow that Swagger UI understands
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock User Database
fake_users_db = {
    "alice": {"username": "alice", "full_name": "Alice Wonderland", "password": "secretpassword"}
}

class User(BaseModel):
    username: str
    full_name: str | None = None

# Endpoint to generate a token (Login)
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # In production, use passlib to verify hashed passwords!
    if form_data.password != user_dict["password"]:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # Return a fake token (In production, use python-jose to generate a real JWT)
    return {"access_token": form_data.username, "token_type": "bearer"}


# A protected dependency
def get_current_user(token: str = Depends(oauth2_scheme)):
    # The 'token' here is whatever was passed in the 'Authorization: Bearer <token>' header
    user_dict = fake_users_db.get(token)
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return User(**user_dict)


# Protected Route (Notice the Dependency!)
@app.get("/users/me", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# Run with: uvicorn app:app --reload
