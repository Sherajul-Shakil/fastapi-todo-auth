from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, admin, users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

# make venv -> python -m venv todoenv
# activate bash -> source todoenv/Scripts/activate
# activate cmd -> todoenv/Scripts/activate
# make txt file -> pip freeze > requirements.txt
# pip install -r requirements.txt
# uvicorn main:app --reload
