from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    age:int
    address:Address
    
address_dict={'city':'nalgonda','state':'telangana','pin':'508001'}

address1=Address(**address_dict)

patient_dict={'name':'naveen','age':22,'address':address1}

patient1=Patient(**patient_dict)

print(patient1)