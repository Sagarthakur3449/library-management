from django.contrib import admin
from .models import Student,Book,Author,IssueBook,BookCategory


# Register your models here.
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(IssueBook)
admin.site.register(BookCategory)

