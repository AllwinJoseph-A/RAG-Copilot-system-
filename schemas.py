from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional
from enum import Enum

# Define User Roles for Security (RBAC)
class UserRole(str, Enum):
    CEO = "CEO"
    HR_MANAGER = "HR_Manager"
    DEPT_MANAGER = "Department_Manager"
    EMPLOYEE = "Employee"

# Define the structural template for an Employee profile
class EmployeeSchema(BaseModel):
    employee_id: str = Field(..., description="Unique alphanumeric identifier")
    name: str
    designation: str
    department: str
    manager_id: Optional[str] = None
    salary: float
    joining_date: date
    location: str
    skills: List[str]
    experience_years: int
    role: UserRole

    class Config:
        from_attributes = True