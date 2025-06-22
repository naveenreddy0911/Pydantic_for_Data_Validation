from pydantic import BaseModel, AnyUrl, Field, model_validator
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
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("Patient older than 60 must have emergency contact number")
    
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")
    
patient_info={'name':'naveen','email':'abc@sbi.com','linkedin_url':'http://linkedin.com/1322','age': 22, 'weight': 64,
              'married':False,'contact_details':{'phone':'8923231','emergency':'9823473'}}

patient1=Patient(**patient_info)

update_patient_data(patient1)