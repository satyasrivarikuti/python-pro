from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)



from django.contrib.auth.models import User
class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def str(self):
        return f'{self.Name} ({self.Register_Number})'



