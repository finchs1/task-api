from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
from uvicorn import run
import os
import json

#Pydantic model for a Task
class Task(BaseModel):
    title: str #Task title
    description: str #Task description
    completed: bool = False #Task status, default is False

    def to_dict(self):
        return {
            "title": self.title,
            "description" : self.description,
            "completed" : self.completed
        }

#Dictionary to store tasks, key = title, value = task
tasks = {}

FILE_PATH = "tasks.json"

#Load tasks from file
def load_tasks():
    data = {}
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
    
    #Add loaded tasks to tasks dict
    for key in data:
        tasks[key] = Task(title = data[key]["title"], description = data[key]["description"], completed = data[key]["completed"])

    print("Loading complete!")

#Save tasks to file
def save_tasks():
    if len(tasks) == 0:
        print("No save required, tasks are empty")
        return

    data = {}
    for key in tasks:
        data[key] = tasks[key].to_dict()

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)

    print("Saving complete!")

#Lifespan function for handling saving and loading tasks
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Loading tasks...")
    load_tasks()
    yield
    print("Saving tasks...")
    save_tasks()

#Create FastAPI instance
app = FastAPI(lifespan = lifespan)

#API endpoint to retrieve all tasks, takes no args
@app.get("/tasks", status_code = 200)
def get_tasks():
    response = {}

    #add success message to response
    response["detail"] = "success"

    #Add tasks to response dict
    for title in tasks:
        response[title] = tasks[title]

    return response

#API endpoint to create a task, takes a task as an argument
@app.post("/tasks", status_code = 201)
def create_task(task: Task):
    response = {}

    #Check if the task already exists, if so, return 409 code and message
    if task.title in tasks:
        raise HTTPException(status_code = 409, detail = f"Task '{task.title}' already exists")
    else:
        #add success message to response
        response["detail"] = "success"
        #Set title of task and task object into response
        response[task.title] = task
        tasks[task.title] = task

    return response

#API endpoint to mark a task as completed, takes a task title as an argument
@app.put("/tasks/{title}", status_code = 200)
def mark_task(title: str):
    resp = {}

    #Check if the task exists
    if title in tasks:
        #If the task exists and it is not marked as completed
        if not tasks[title].completed:
            #Set task to completed and add to response
            tasks[title].completed = True
            resp["detail"] = "success"
            resp[title] = tasks[title]
        else:
            #If task is marked already, return 409 and error message
            raise HTTPException(status_code = 409, detail = f"Task '{title}' already marked as completed")
    else:
        #If task doesn't exist, return 404 and error message
        raise HTTPException(status_code = 404, detail = f"Task '{title}' does not exist")
    
    return resp

#API endpoint to delete a task, takes task title as argument
@app.delete("/tasks/{title}", status_code = 200)
def delete_task(title: str):
    response = {}

    #Check if the task exists
    if title in tasks:
        #Delete task and add message
        response["detail"] = "success"
        del tasks[title]
    else:
        #If task doesn't exist, 
        raise HTTPException(status_code = 404, detail = f"Task '{title}' does not exist")

    return response

#Run on localhost:8000
if __name__ == "__main__":
    run(app, host="127.0.0.1", port = 8000)