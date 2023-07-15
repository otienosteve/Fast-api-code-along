from fastapi import FastAPI
from models import Student, session

app =FastAPI()


@app.get('/home')
def index():
    return {"msg":"welcome to Fastapi"}


@app.get('/student')
def get_all_students():
    # query for all students
    session.query(Student).all()
    print(add Student)
    #return the student data
    return {'msg':'all students'}

@app.get('/student/1')
def get_one_students():

    return {'msg':'1 students'}

