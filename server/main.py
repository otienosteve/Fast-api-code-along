
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List 
from .models import Student, session

app =FastAPI()


class StudentSchema(BaseModel):
    first_name: str 
    last_name: str
    age: int 
    home_town: str 
    
    class Config:
        orm_mode = True


@app.get('/home')
def index():
    return {"msg":"welcome to Fastapi"}


@app.get('/student', response_model=List[StudentSchema])
def get_all_students():
    # query for all students
    students = session.query(Student).all()
    #return the student data
    return students

@app.get('/student/{id}')
def get_one_students(id : int)-> StudentSchema:
    # use the variable a desired to return a specific resource
    student = session.query(Student).filter_by(id =id).first()
    # return the resource to the user
    return student

@app.post('/student', response_model=StudentSchema)
def add_student(payload: StudentSchema):
    print(payload)
    # logic to add new student to our database using our payload
    # new_student = Student(**payload)
    # session.add(new_student)
    # session.commit()

    return  {"msg":"success"}
