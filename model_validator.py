from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str 
    age: int 
    email: EmailStr
    weight: float 
    married: bool
    allergis: List[str] 
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError(
                'Patient older than 60 must have an emergency contact'
            )
        return model



def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergis)
    print(patient.married)
    print(patient.contact_details)
    print('updated')


patient_info = {
    'name': 'Mohammad', 
    'age': 70, 
    'weight': 57.5,
    'married': False,
    'email': 'mohammad70623@hdfc.com',
    'allergis': ['dust', 'pollen'], 
    'contact_details': {
        'Phone': '0183597062',
        'current address': 'Ashulia',
        'emergency': '2324234'
    }
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
