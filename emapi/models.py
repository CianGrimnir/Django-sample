from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class employee(models.Model):
    employee_id=models.PositiveIntegerField(primary_key=True)
    #employee_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    department=models.CharField(max_length=50)

    def __str__(self):
        return str(self.employee_id)+' '+self.first_name+' '+self.last_name+' '+self.department
	
    def get_dict(self): 
        return {"Employee ID":self.employee_id,
                "First Name":self.first_name,
                "last name":self.last_name,
                "Department": self.department,
                }
