from django.urls import path

from .views import (
	post_create,
	post_update,
	post_delete,
	post_detail,
	post_list,
)


urlpatterns = [
	path('create/', post_create, name="post_create"), 
	path('edit/', post_update, name="post_update"), 
	path('delete/', post_delete, name="post_delete"), 
	path('detail/', post_detail, name="post_detail"), 
	path('', post_list, name="post_list"),
]