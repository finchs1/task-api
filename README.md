## Tasks API Project

### Overview

Simple REST Task API that allows for manipulating tasks.

### Features

- FastAPI for API endpoints as well as unit tests.
- Allows tasks to be listed, created, deleted, and set as completed.
- Saves and loads tasks to a json file in the same directory.

### Requirements

- Python 3.7+
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

### Optionally, run unit tests for the list and create endpoints:
`python test.py`
