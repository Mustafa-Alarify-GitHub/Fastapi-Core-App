# FastAPI Core Template
This project is a modular FastAPI backend template with support for environment management, database integration, and scalable app structure.
## How to Use This Template
### 1. Clone the Repository
```sh
### 2. Install Dependencies
### 3. Configure Environment Variables
- Copy or create a `.env` file in the root directory. Example variables:
### 4. Run Database Migrations
### 5. Start the Application
### 6. Access Modular Apps
## Project Structure
## Tips
## Advanced Usage & Customization

### 1. Adding a New App Module
- Create a new folder under `apps/` (e.g., `apps/user`).
- Implement your app logic, routes, and GraphQL schemas as in the `book` example.
- Mount your app in `main.py` using `main_app.mount("/yourapp", your_app, "YourApp")`.

### 2. Environment Management
- Use `.env`, `.env.development`, `.env.production`, etc. for different environments.
- The `EnvManager` class loads the correct environment file based on the `ENV` variable.
- You can add app-specific environment files in `apps/<app_name>/.env.<env>`.

### 3. Database Configuration
- Change the `DATABASE_URL` in your `.env` file to use PostgreSQL, MySQL, etc.
- All database logic is handled via SQLModel and SQLAlchemy.

### 4. Alembic Migrations
- Migration scripts are in the `migrations/versions/` folder.
- To create a new migration: `poetry run alembic revision --autogenerate -m "your message"`
- To upgrade/downgrade: `poetry run alembic upgrade head` or `poetry run alembic downgrade -1`

### 5. GraphQL Support
- Each app can expose a GraphQL endpoint using Strawberry and FastAPI integration.
- See `apps/book/gql/` for an example of GraphQL queries and types.

### 6. Shared Logic
- Place shared entities, models, repositories, and schemas in the `shared/` directory for reuse across apps.

### 7. Production Deployment
- Use a production server like Gunicorn with Uvicorn workers for deployment.
- Example: `poetry run gunicorn main:main_app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000`

---
---
Feel free to customize this template for your own backend projects!
