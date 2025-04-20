from django.db import models

# Create your models here.

class UserData(models.Model):

    username = models.CharField(max_length=20,primary_key=True)
    email = models.EmailField(max_length=30)
    mobile_number = models.IntegerField()
    password = models.CharField(max_length=20)


    def __str__(self):
        return f"username is {self.username}and email is {self.email} and mobile number is {self.mobile_number} and password is {self.password}"
    
    class Meta:
        db_table = "userdata"

# class AdminAccess(models.Model):

#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     username = models.CharField(max_length=20,unique=True)
#     age = models.IntegerField()
#     major_skill = models.CharField(max_length=20)
#     city = models.CharField(max_length=20)
#     designation = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return f"id is {self.id} and name is {self.name} and username is {self.username} and age is {self.age} and major_skill is {self.major_skill} and city is {self.city} and designation is {self.designation} and password is {self.password}"
    
#     class Meta:
#         db_table = "adminaccess"