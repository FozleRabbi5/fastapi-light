
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import Dict, List, Any, Union, Optional, Annotated


class StudentType(BaseModel):

    name: str
    age: int
    email: EmailStr
    linkedin: AnyUrl
    is_married: bool = None
    weight: float
    subjects: List[str]
    contacts : Dict[str, str]
 
    @model_validator(mode='before')
    @classmethod
    def validate_student(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        print("Validating student data...")
        print(values)
        if values.get('age') >= 60:
            if not values.get('contacts') or not values['contacts'].get('emergency_number'):
                raise ValueError("Must provide emergency number for students older than 60")
        return values

    @field_validator('weight', mode='after')
    @classmethod
    def validate_weight(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Weight must be greater than 0")
        return v

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: EmailStr) -> EmailStr:
        if 'diu' not in v:
            raise ValueError("Invalid email format")
        return v


def add_student(student: StudentType):
    name = student.name
    age = student.age
    email = student.email
    is_married = student.is_married
    weight = student.weight
    subjects = student.subjects
    print(is_married)
    print(age)
    print(weight)
    print(email)
    print(subjects)
    print(student.contacts)

    if age < 0:
        raise ValueError("Age must be greater than 0")

    print(name)
    if age < 18:
        print("young")
    else:
        print("adult")

 
std = {
    "name": "Rantu",
    "age": 60,
    "email": "rantu@diu.edu.bd",
    "linkedin": "https://www.linkedin.com/in/rantu",
    "weight": "44",
    "subjects": ["Math", "Science", "English"],
    "contacts": {"phone": "123-456-7890", "address": "123 Main St"}
}

st = StudentType(**std)
add_student(st)
