from django.db import models

# Create your models here.
class admin_users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    superuser = models.BooleanField(default=False)

class book_table(models.Model):
    bookid = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=50)
    bookimg = models.ImageField(upload_to='img', null=True, blank=True)
    totalbooks = models.IntegerField()
    Available = models.IntegerField(null=True)
    issued = models.IntegerField(null=True)


class issued_table(models.Model):
    
    stud_rollno = models.IntegerField()
    stud_name = models.CharField(max_length=50)
    issue_date = models.DateField() 
    return_date = models.DateField()
    book_name = models.CharField(max_length=50)
    bookid = models.ForeignKey(book_table,null=True,on_delete=models.SET_NULL)