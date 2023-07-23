
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List,Optional 
from .models import Student, session

app =FastAPI()


class StudentSchema(BaseModel):
    first_name: str 
    last_name: str
    age: int 
    home_town: str 
    
    class Config:
        orm_mode = True


class StudentUpdateSchema(BaseModel):
    first_name: Optional[str] 
    last_name: Optional[str]
    age: Optional[int] 
    home_town: Optional[str] 
    


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
def add_student( payload: StudentSchema):
    # logic to add new student to our database using our payload
    new_student = Student(**dict(payload))
    session.add(new_student)
    session.commit()
    # return new Student as a response
    return  new_student

@app.put('/student/{id}')
def full_update(id: int , payload: StudentSchema)-> StudentSchema:
    # retrieve the student
    student = session.query(Student).filter_by(id=id).first()
    # Update the student retrieved with the corresponding payload 
    for key,value in payload.dict().items():
        setattr(student, key,value)
    # persist the changes in the database 
    session.commit()
    # return a response to the user
    return student


@app.patch('/student/{id}')
def partial_update(id: int, payload: StudentUpdateSchema) -> StudentSchema: 
    # retrieve student from the database 
    student = session.query(Student).filter_by( id = id).first()
    if not student:
        raise HTTPException(status_code= 404, detail="Student not found")
    for key,value in payload.dict(exclude_unset = True).items():
        setattr(student, key, value)

    return student 
