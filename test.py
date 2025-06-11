from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_tasks():
    #List all tasks (should be empty)
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == {"detail":"success"}

def test_create_task():
    #Add a task
    response = client.post("/tasks", json = {"title" : "First task", "description" : "First task desc"})
    assert response.status_code == 201
    assert response.json() == { "detail":"success", "First task" : {"title" : "First task", "description" : "First task desc", "completed" : False}}

def test_duplicate_create_task():
    #Add a duplicate task
    response = client.post("/tasks", json = {"title" : "First task", "description" : "First task desc"})
    assert response.status_code == 409
    assert response.json() == {"detail":"Task 'First task' already exists"}


#Run tests
test_get_tasks()
test_create_task()
test_duplicate_create_task()