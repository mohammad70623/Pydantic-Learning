from pydantic import BaseModel, EmailStr, AnyUrl, Field , field_validator
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):

    name: str 
    age: int 
    email: EmailStr
    linkedin_url: AnyUrl
    weight: float 
    married: bool
    allergis: List[str] 

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domain =['hdfc.com', 'icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid Domain')
        
        return value




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
                'email': 'mohammad70623@hdfc.com',
                'linkedin_url': 'https://www.linkedin.com/in/mohammad-51a10a287/',
                'allergis':['dust', 'pollen'], 
                'contact_details': {
                                    'Phone': '0183597062',
                                    'current address': 'Ashulia'}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
