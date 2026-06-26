# Unit 4 Capstone Project

This project demonstrates a full-stack deployment of a web application using the tools learned in Unit 4.

## Architecture
1. **Backend**: FastAPI (Python 3.11), storing data in SQLite.
2. **Frontend**: Pure HTML, CSS, and Vanilla JavaScript.
3. **Reverse Proxy**: Nginx serving the static frontend files and routing `/api/` traffic to the backend.
4. **Containerization**: Docker Compose orchestrating the entire stack.

## How to Run This Project

1. Make sure you have Docker and Docker Compose installed on your system.
2. Open a terminal in this directory (`unit-4/capstone_project/`).
3. Run the following command:
   ```bash
   docker compose up --build
   ```
4. Open your web browser and navigate to: [http://localhost](http://localhost)

You should see the frontend load. If you type a message and submit it, the Javascript will send a POST request to `/api/messages`. Nginx will forward that to the FastAPI container on port 8000, which will save it to the SQLite database.

Press `Ctrl+C` in the terminal to stop the containers.
