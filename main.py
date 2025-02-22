from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1 : {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}
@app.get("/")
def index():
    return {"name": "First Data"}

#Student ID as Path parameter to access student detail
@app.get("/get-student/{student_id}")
def get_students(student_id: int = Path(..., description="The ID of the student you want to view", gt=0,lt=3)):
    return students[student_id]