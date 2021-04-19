from django.db import models


# Create your models here.
class Students(models.Model):
    status = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    id= models.IntegerField(primary_key=True)
    gender=models.CharField(max_length=50)
    phone =models.CharField(max_length=10)
    address=models.CharField(max_length=122)
    date = models.DateField()
    desc = models.TextField()

# View the data send by user in order by name
    def __str__(self): 
        return self.name


class Teachers(models.Model):
    status = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    gender=models.CharField(max_length=50)
    phone =models.CharField(max_length=10)
    address=models.CharField(max_length=122)
    date = models.DateField()
    desc = models.TextField()

    def __str__(self): 
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    gender=models.CharField(max_length=50)
    phone =models.CharField(max_length=10)
    address=models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self): 
        return self.name
