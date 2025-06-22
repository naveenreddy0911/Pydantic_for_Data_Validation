from pydantic import BaseModel, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email:str
    linkedin_url:AnyUrl
    age:Annotated[int,Field(gt=0,lt=120)]
    weight:Annotated[float,Field(gt=0,strict=True)]
    height:Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None,description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details: Dict[str,str]
    
    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight/(self.height)**2,2)
    
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.bmi)
    print("Inserted")
    
patient_info={'name':'naveen','email':'abc@sbi.com','linkedin_url':'http://linkedin.com/1322','age': 22, 'weight': 64,
              'height':1.65,'married':False,'contact_details':{'phone':'873291','emergency':'875952'}}

patient1=Patient(**patient_info)

update_patient_data(patient1)