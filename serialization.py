from pydantic import BaseModel 

class Address(BaseModel):

    city: str 
    state: str 
    pin: str 

class Patient(BaseModel):

    name: str 
    gender: str 
    age: int 
    address: Address
    
address_dict= {'city': 'Dhaka',
               'state': 'Dhaka',
               'pin': '4710'}
address1 = Address(**address_dict)

patient_dict = {'name':'Mohammad',
                'gender': 'Male',
                'age': 22,
                'address': address1}
patient1 = Patient(**patient_dict)

temp1 = patient1.model_dump(include=['name', 'gender'])

print(temp1)
print(type(temp1))

temp2 = patient1.model_dump_json(exclude=['name', 'gender'])

print(temp2)
print(type(temp2))