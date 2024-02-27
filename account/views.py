from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Book,Student,BookCategory,IssueBook
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request,'base.html')

def profile(request):
    return render(request,'profile.html')

def account(request):
    return render(request,'home.html')

def home(request):
    category=BookCategory.objects.all()
    return render(request,'base.html',{'category':category})

def signin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password =request.POST.get('password')
        repeatpassword =request.POST.get('repeatpassword')
        print(username,firstname,lastname,email,password,repeatpassword)
        user =User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save() 
        return redirect('/profiles')
    return render(request,'signin.html')

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("==============",username,password)
        user = authenticate(username=username,password=password)
        print(user)
        if user is None:
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/profiles')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return render(request,'login.html')


@login_required(login_url="login")
def add_book(request):
    if request.method=='POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        category = request.POST.get('category')
        description = request.POST.get('description')
        print(name,author,category,description)
        category=BookCategory.objects.get(category=category)
        user =Book.objects.create(name=name,writer=author,category=category,description = description)
        user.save()
        return redirect('add_book/')
    return render(request,'add_book.html')


@login_required(login_url="login")
def view_books(request):
    data = Book.objects.all()
    return render(request,'view_books.html',{'data':data})

def delete_book(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('view_books')

@login_required(login_url="login")
def view_students_book(request):
    students = IssueBook.objects.all()
    return render(request,'view_students_book.html',{'students':students})

def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('view_students_book.html')

def category(request):
    category = BookCategory.objects.all()
    return render(request,'base.html',{'category':category})

def book_list(request,id):
    book=Book.objects.filter(category_id=id)
    print("==========",book)
    return render(request,'booklist.html',{'book':book})

@login_required(login_url="login")
def issue_book(request):
    student = Student.objects.get(user_id = request.user.id)
    print('________________',student)
    issues = IssueBook.objects.filter(student_id=student.id)
    return render(request,'issue_book.html',{'issues':issues})
