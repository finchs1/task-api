## Tasks API Project

### Overview

Simple REST Task API that allows for manipulating tasks.

### Features

- FastAPI for API endpoints as well as unit tests.
- Allows tasks to be listed, created, deleted, and set as completed.
- Saves and loads tasks to the tasks.json file.

### API Endpoints

API is by default on port 8000.

List all tasks:\
GET /tasks\
Response: All tasks (json)\
Example Responses:\
200 {"detail":"success", "Clean dishes" : {"title": "Clean dishes", "description" : "Clean the dishes before tomorrow", completed: false}}\
200 {"detail":"success"}


Create task:\
POST /tasks with json data that includes title and description\
Task titles cannot be duplicates\
Response: detail message with task created if successful, otherwise just detail message (json)\
Example: POST /tasks {"title": "Clean dishes", "description" : "Clean the dishes before tomorrow"}\
Example Responses:\
201 {"detail":"success", "Clean dishes" : {"title": "Clean dishes", "description" : "Clean the dishes before tomorrow", completed: false}}\
409 {"detail":"Task 't' already exists"}


Set task as complete:\
PUT /tasks/{tasktitle}\
Example: PUT "/tasks/Clean dishes"\
Example Responses:\
200 {"detail":"success", "Clean dishes" : {"title": "Clean dishes", "description" : "Clean the dishes before tomorrow", completed: true}}\
409 {"detail":"Task 'Clean dishes' already marked as completed"}\
404 {"detail":"Task 't' does not exist"}


Delete a task:\
DELETE /tasks/{tasktitle}\
Example: DELETE "/tasks/Clean dishes"\
Example Responses:\
200 {"detail":"success"}\
404 {"detail":"Task 't' does not exist"}

### Requirements

- Python 3.7+
- Python-pip
- FastAPI
- Uvicorn (included with fastapi[standard])
- curl (for testing/using the API)

### Installation

1. Clone the respository:
   ```bash
   git clone https://github.com/finchs1/task-api.git
   cd task-api

2. Install FastAPI:
   ```bash
   pip install "fastapi[standard]"

3. Run API:
   ```bash
   python main.py

### API Manual Testing

To manually test the API, curl can be used as so:

Get all tasks from API

`curl -X GET http://localhost:8000/tasks`

Add task

`curl -X POST http://localhost:8000/tasks --json '{"title": "taskTitle", "description" : "Task description"}'`

Set task as completed (replace taskTitle with title of task)

`curl -X PUT http://localhost:8000/tasks/taskTitle`

Delete task (replace taskTitle with title of task)

`curl -X DELETE http://localhost:8000/tasks/taskTitle`

### Optionally, run unit tests for the list endpoint and create endpoint:
`python test.py`

No output for the test indicates success.
