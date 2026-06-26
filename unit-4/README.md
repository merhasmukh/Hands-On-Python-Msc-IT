# Unit IV — Professional Development, Deployment and DevOps

> **Course**: MSc (IT) — Hands-On Python  
> **Target**: Semester Students (Beginners to Intermediate)  
> **Python Version**: 3.11+

---

## 📚 What You Will Learn

By the end of this unit, you will be able to take your Python applications from your local computer and deploy them professionally. You will learn:

- **Project Organization**: Structuring projects, managing secrets with `.env`, and the 12-Factor App principles.
- **Version Control**: Mastering Git, GitHub, branching, and pull requests.
- **Linux Essentials**: Navigating the file system, managing permissions, and understanding processes.
- **Deployment**: Understanding WSGI vs ASGI, setting up Gunicorn/Uvicorn, and configuring Nginx as a reverse proxy.
- **Containerization**: Packaging applications with Docker and orchestrating them with Docker Compose.
- **CI/CD**: Automating testing and deployment pipelines using GitHub Actions.
- **AI-Assisted Development**: Using AI tools (like Copilot/ChatGPT) effectively and ethically for debugging and documentation.

Finally, you will synthesize all your knowledge in the **Capstone Project**: Deploying a containerized FastAPI backend and frontend behind Nginx.

---

## 🗂️ Folder Structure

```
unit-4/
├── README.md                        ← You are here
├── requirements.txt                 ← Dependencies
├── 01_project_organization/         ← .env, python-dotenv, 12-factor
├── 02_version_control/              ← Git, GitHub, branching
├── 03_linux_essentials/             ← File system, permissions, processes
├── 04_deployment_fundamentals/      ← ASGI, Nginx, Gunicorn
├── 05_containerization/             ← Docker, Docker Compose
├── 06_ci_cd/                        ← GitHub Actions
├── 07_ai_assisted_dev/              ← Prompt engineering, ethics
└── capstone_project/                ← Final full-stack deployment project
```

---

## 🚀 How to Use These Materials

### For Students

1. **Read the Notebooks**: Each folder (01 through 07) contains a Jupyter Notebook explaining the concepts.
2. **Review the Samples**: Look at the sample configurations (like `nginx.conf`, `Dockerfile`, `.gitignore`) provided in the folders to see what professional configuration looks like.
3. **Complete the Exercises**: Open the `.txt` exercise files and answer the conceptual and command-line questions. 
4. **Build the Capstone**: Follow the README in the `capstone_project/` folder to deploy your final web application.

---

*Made with ❤️ for MSc (IT) students — Python 3.11+*
