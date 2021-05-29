from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True,max_length=20)
    join_date = models.DateField(null=True,blank=True)
    password = models.CharField(max_length=255)


    def __str__(self):
        return self.username


    @staticmethod
    def userExits(username):
        try:
            username = User.objects.get(username=username)
            return username
        except:
            return False

class Task(models.Model):
    t_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200,validators=[MinLengthValidator(10)])
    task_des = models.CharField(max_length=2000,null=True)
    task_file = models.FileField(upload_to='task',blank=True)
    create_on_time = models.DateTimeField(null=True)