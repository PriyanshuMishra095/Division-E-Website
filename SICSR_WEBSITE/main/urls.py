from django.urls import path
from . import views

urlpatterns=[
    path("home",views.index,name="index"),
    path("timetable",views.timetable,name="timetable"),
    path("notes",views.notes,name="notes"),
    path("divisionlist",views.divisionlist,name="divisionlist"),
    path("userlist",views.userlist,name="userlist"),
    path("contact",views.contact,name="contact"),
    path("sign-up",views.signup,name="sign-up"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),


    path('userlist/delete/<int:id>', views.delete, name='delete')
]