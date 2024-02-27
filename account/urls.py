from django.urls import path
from account import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base,name='account'),

    # path('', views.account, name='account'),
    path('home/',views.home,name='home'),
    path('profiles',views.profile,name='profiles'),
    path('signin/',views.signin,name='signin'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('category/',views.category,name = 'category'),
    path("add_book/", views.add_book, name="add_book"),
    path("view_books/", views.view_books, name="view_books"),
    path("view_students_book/", views.view_students_book, name="view_students_book"),
    path("delete_book/<int:id>/", views.delete_book, name="delete_book"),
    path("delete_student/<int:id>/", views.delete_student, name="delete_student"),
    path("book_list/<int:id>/", views.book_list, name="book_list"),
    path("issue_book/",views.issue_book,name="issue_book"),   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


#  +static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)