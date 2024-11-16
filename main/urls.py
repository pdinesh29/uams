from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    # path('create',views.createe,name="create"),
    # path('modify',views.modifyy,name="modify"),
    path('logout',views.logout,name='logout'),
    path('<str:name>',views.student,name="report"),
]
