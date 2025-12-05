from django.urls import path
from.views import home, about, contact, feedback, service, profile, gallery, list_students, add_students,edit_students,delete_students,students_list,course_list,register_User,login_User,logout_User,dashboard,add_course,edit_course,delete_course,active_course

urlpatterns = [
    path('home/',home),
    path('about/',about),
    path('contact/',contact),
    path('feedback/',feedback),
    path('service/',service),
    path('profile/',profile),
    path('gallery/',gallery),
    path('students/',list_students),
    path('due/',course_list),
    path('courses/',course_list,name="course_list"),
    path('courses/add/', add_course, name="add_course"),
    path('courses/edit/<int:id>/', edit_course, name="edit_course"),
    path('courses/delete/<int:id>/', delete_course, name="delete_course"),
    path('courses/active/', active_course, name="active_course"),
    path('register/',register_User),
    path('login/',login_User),
    path('logout/',logout_User),
    path('dashboard/',dashboard),
    path('students/',students_list,name="students_list"),    
    path('students/add/',add_students,name="add_student"),
    path('students/edit/<int:id>/',edit_students,name="edit_student"),
    path('students/delete/<int:id>/',delete_students,name="delete_student")
    
]