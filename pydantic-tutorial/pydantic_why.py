
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Any, Union, Optional, Annotated


class StudentType(BaseModel):

    name: Annotated[str, Field(max_length=50, description="Name must be less than 50 characters", title="Student Name")]
    age:int
    email: EmailStr
    linkedin: AnyUrl
    is_married: Optional[bool] = None
    weight: Annotated[float, Field(gt=0, description="Weight must be greater than 0", title="Student Weight", strict=True)]
    subjects : List[Union[str, int]]


def add_student(student: StudentType):
    name = student.name
    age = student.age
    email = student.email
    is_married = student.is_married
    weight = student.weight
    subjects = student.subjects
    print(is_married)
    print(weight)
    print(email)
    print(subjects)

    if age < 0:
        raise ValueError("Age must be greater than 0")
    
    print(name)
    if age < 18:
        print("young")
    else:
        print("adult")

std = {
"name": "Rantu",
"age": 14,
"email": "rantu@example.com",
"linkedin": "https://www.linkedin.com/in/rantu",
"weight": "44",
"subjects": ["Math", "Science", "English", 1],
}

st = StudentType(**std)
add_student(st)  
