from django.urls import path
from . import views

urlpatterns = [
    path("", views.member_list, name="member_list"),
    path("add/", views.add_member, name="add_member"),
    path("update/<int:id>/", views.update_member, name="update_member"),
    path("delete/<int:id>/", views.delete_member, name="delete_member"),
]
