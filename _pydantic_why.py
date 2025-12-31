from pydantic import BaseModel 
from typing import List, Dict, Optional
class Patient(BaseModel):

    name: str 
    age: int 
    weight: float 
    married: bool
    allergis: Optional[List[str]] = None
    contact_details: Dict[str, str]



def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergis)
    print(patient.married)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergis)
    print(patient.married)
    print('updated')

patient_info = {'name': 'Mohammad', 
                'age': 30, 
                'weight': 57.5,
                'married': False,
                'allergis':['dust', 'pollen'], 
                'contact_details': {'Email': 'mohammad70623@gmail.com',
                                    'Phone': '0183597062',
                                    'current address': 'Ashulia'}}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
