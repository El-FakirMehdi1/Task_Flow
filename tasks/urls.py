from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('categories/',views.categories_page,name='categories'),
    path('dashboard/',views.dashboard_page,name='dashboard'),
    path('about/',views.about_page,name='about'),
    path('add_task',views.add_task,name='add_task'),
    path(
        "edit_task/<int:id>/",
        views.edit_task,
        name="edit_task"
    ),
    path(
        'delete_task/<int:id>/',
        views.delete_task,
        name='delete_task'
    ),
    path("login/",views.login_user,name="login"),
    path("register/",views.register_user,name="register"),
    path("logout/",views.logout_user,name="logout"),
]
