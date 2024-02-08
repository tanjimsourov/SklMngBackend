from users import views
from django.urls import path

urlpatterns = [
    path('superuser', views.SuperuserRegister.as_view(), name="superuser"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    path('addstaff', views.addStaff.as_view(), name="addstaff"),
    path('employeelist', views.EmployeeList.as_view(), name="employees"),
    path('addteacher', views.addTeacher.as_view(), name="addTeacher"),
    path('teacherlist', views.TeacherList.as_view(), name="teachers"),
    path('addstudent', views.addStudent.as_view(), name="addStudent"),
    path('allstudents', views.StudentList.as_view(), name="students"),
    path('student/<int:class_>/', views.StudentListSpecificClass.as_view(), name="StudentSpecificClass"),
    path('student/<int:class_>/<str:section>', views.StudentListSpecificSection.as_view(), name="StudentSpecificClass"),

]
