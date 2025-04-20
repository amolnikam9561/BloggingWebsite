from django.db import models

# Create your models here.
class Questions(models.Model):
    SUBJECT_CHOICES = [
        ('Python', 'Python'),
        ('DSA', 'DSA'),
        ('OOP', 'OOP'),
        ('Software Engineering', 'Software Engineering'),
        ('DBMS', 'DBMS'),
        ('Web Dev', 'Web Dev'),
        ('Operating Systems', 'Operating Systems'),
        ('Machine Learning', 'Machine Learning'),
        ('Data Science', 'Data Science'),
        ('Cloud Computing', 'Cloud Computing'),
        ('Distributed Systems', 'Distributed Systems'),
        ('Blockchain Tech', 'BlockChain Tech'),
    ]

    qno = models.IntegerField(primary_key=True)
    qtext = models.CharField(max_length=300)
    answer = models.CharField(max_length=500)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)

    def __str__(self) -> str:
        return f"{self.qno}, {self.qtext}, {self.answer}, {self.op1}, {self.op2}, {self.op3}, {self.op4}, {self.subject}"

    class Meta:
        db_table = 'questions'

class UserDatabase(models.Model):

    username = models.CharField(max_length=20,unique=True,primary_key=True)
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.username},{self.email},{self.password}"
    
    class Meta:
        db_table = 'userdatabase'

class AdminDatabase(models.Model):

    username = models.CharField(max_length=20,unique=True,primary_key=True)
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.username},{self.email},{self.password}"
    
    class Meta:
        db_table = 'admindatabase'

class Results(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    score = models.IntegerField()
    date_time = models.DateTimeField()

    class Meta:
        db_table = 'results'
