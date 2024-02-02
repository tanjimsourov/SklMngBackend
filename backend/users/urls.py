from users import views
from django.urls import path

urlpatterns = [
    path('superuser', views.SuperuserRegister.as_view(), name="superuser"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    # path('userlist', views.UserList.as_view(), name="users"),
    # path('employeelist', views.EmployeeList.as_view(), name="employees"),

    # path('addstuff', views.addStaff.as_view(), name="adduser"),
    # path('getuser/<int:id>/', views.GetUserDetails.as_view(), name="GetUserDetails"),
    # path('addnomini/<int:id>', views.AddNominiDetails.as_view(), name="AddNomini"),
    # path('addcustomer', views.addCustomer.as_view(), name="addcustomer"),
    # path('changepassword', views.ChangePasswordView.as_view(), name="change_password"),
    # path('reset_pass_req', views.ResetPassReq.as_view(), name="reset_password_req"),
    # path('reset_pass_verify', views.ResetPassVerify.as_view(), name="reset_password_verify"),
    # path('reset_pass', views.ResetPass.as_view(), name="reset_password_verify"),
]
