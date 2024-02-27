from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Student(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length = 100)
    mobile_num = models.IntegerField(default = 0)
    stu_image =  models.ImageField()
    def __str__(self):
        return self.user.username
    
class BookCategory(models.Model):
    category = models.CharField(max_length =100)
    def __str__(self):
        return self.category
    
class Book(models.Model):
    category = models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    writer = models.CharField(max_length =100)
    description = models.CharField(max_length = 700)
    imges=models.ImageField(upload_to='media',blank=True, null=True)
    def __str__(self):
        return self.name
    
class Author(models.Model):
    author = models.CharField(max_length = 150)
    def __str__(self):
        return self.author
           
class IssueBook(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    returndate = models.DateField(default = None)
    def __str__(self):
        return self.book.name



    
     