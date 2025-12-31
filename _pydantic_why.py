from pydantic import BaseModel, EmailStr, AnyUrl, Field 
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='name of th epatient',
                                description='gin=ve the name of the patient in less than 50 char', 
                                example=['Mohammad'])]
    age: int = Field(gt=18, lt=45)
    email: EmailStr
    linkedin_url: AnyUrl
    weight: Annotated[float, Field(gt=18, strict=True)]
    married: Annotated[bool, Field(default=None, description='is the patient married or not')]
    allergis: Annotated[Optional[List[str]],Field(default=None, max_length=5)]
    contact_details: Dict[str, str]



def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergis)
    print(patient.married)
    print(patient.email)
    print(patient.linkedin_url)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergis)
    print(patient.married)
    print(patient.linkedin_url)
    print('updated')

patient_info = {'name': 'Mohammad', 
                'age': 30, 
                'weight': 57.5,
                'married': False,
                'email': 'mohammad70623@gmail.com',
                'linkedin_url': 'https://www.linkedin.com/in/mohammad-51a10a287/',
                'allergis':['dust', 'pollen'], 
                'contact_details': {
                                    'Phone': '0183597062',
                                    'current address': 'Ashulia'}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
