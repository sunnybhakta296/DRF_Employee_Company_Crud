from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=[('private', 'Private'), ('public', 'Public')])
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    about=models.TextField()
    position=models.CharField(max_length=100, choices=(
        ('Manager', "manager"),
        ('Software developers', 'sd'),
        ('Project Manager', "pm")
    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)