from django.urls import path
from . import views

urlpatterns = [
  path('login_screen',views.login,name='loginScreen'),
  path('CreateEmployeeAccount',views.new_account , name='CreateAccount'),
  path('',views.homepage,name='homepage'),
  path('active-inactive',views.active_inactive,name='active-inactive'),
  path('search',views.search,name='search'),
  path('addStudentPage',views.addStudentPage,name='addStudentPage'),
  path('editPage',views.editPage,name='editPage'),
  path('department_assignment',views.department_assignment,name='department_assignment'),
  path('log_out', views.log_out, name='logOut'),
  path('whoLogedin', views.who_pressed_login, name="who_pressed_login"),
  path('HomePage',views.validate,name='validate'),
  path('check_new_Account', views.check_new_Account, name='check_new_Account'),
  path('addStudent',views.addStudent,name='addStudent'),
  path('updateStudents',views.updateStudents,name='updateStudents'),
  path('update', views.updateDone, name='update'),
  path('delete', views.deleteStudent, name="deleteSt"),
  path('changeStatus',views.changeStatus,name='changeStatus'),
  path('getSt',views.getSt,name='getST'),
  path('assign/<int:id>',views.assign,name='assing'),
]
