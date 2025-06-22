from pydantic import BaseModel, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email:str
    linkedin_url:AnyUrl
    age:Annotated[int,Field(gt=0,lt=120)]
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None,description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details: Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        if value.split('@')[-1] not in ['kgpain.iitkgp.ac.in','sbi.com']:
            raise ValueError("Not a valid domain")
        
        return value
    
    @field_validator('name')
    @classmethod
    def name_transformer(cls,value):
        return value.upper()
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")
    
patient_info={'name':'naveen','email':'abc@sbi.com','linkedin_url':'http://linkedin.com/1322','age': 22, 'weight': 64,'contact_details':{'phone':'238764'}}

patient1=Patient(**patient_info)

update_patient_data(patient1)