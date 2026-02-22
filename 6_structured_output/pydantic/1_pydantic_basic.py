from pydantic import BaseModel 
 
# #1. base model 
# class Student(BaseModel):
#     name: str 
# new_student = {'name':"puskar"}
# student = Student(**new_student)   # ** (double star ) is used to unpack dictionary
# print(type(student))


# #2. default values 
# from typing import Optional
# class Student(BaseModel):
#     name: str = "puskar"
#     age: Optional[int] = None  # put none value when Optional is used  
# new_student = {'age':45}
# student = Student(**new_student)
# print(dict(student))

# # 3. basic validation as EmailStr (inbuilt validation for emails)
# from typing import Optional
# from pydantic import EmailStr 

#     # install email validator: pip install pydantic[email]
# class Student(BaseModel):
#     name: str = "puskar"
#     age: Optional[int] = None 
#     email: EmailStr 

# new_student = {'age':45,'email': 'abc@gmail.com'}
# student = Student(**new_student)
# print(dict(student))

# # 4. setting field value (description , set lower and upper bounds)
# from typing import Optional
# from pydantic import EmailStr, Field 

# class Student(BaseModel):
#     name: str = "puskar" 
#     age: Optional[int] = None 
#     email: EmailStr
#     cgpa: float = Field(gt = 0, lt =10,default = 5, description = "A decimal value representing the cgpa of the student")

# new_student = {'age': 36, 'email':"puskar@gmail.com",'cgpa':7}
# student = Student(**new_student)
# print(student.model_dump_json())