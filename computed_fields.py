from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str 
    age: int 
    email: EmailStr
    weight: float 
    height: float
    married: bool
    allergis: List[str] 
    contact_details: Dict[str, str]


    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi 



def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print('BMI', patient.calculate_bmi)
    print(patient.email)
    print(patient.allergis)
    print(patient.married)
    print(patient.contact_details)
    print('updated')


patient_info = {
    'name': 'Mohammad', 
    'age': 70, 
    'weight': 57.5,
    'height': 1.72,
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
