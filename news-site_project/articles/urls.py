from django.urls import path

from . import views

urlpatterns = [
    path("articles/new/", views.article, name='new_article'),
    path("articles/new/upload", views.upload_file, name='upload_article'),
    path("articles/", views.Articles_ListView.as_view(), name='Articles_ListView'),
    path("articles/subarticle/<int:cat>", views.Articles_subcategory_list, name='Articles_SubListView'),
    path("articles/<int:pk>/", views.Articles_DetailView.as_view(), name='Articles_DetailView'),
    path("articles/<int:pk>/delete", views.Articles_DeleteView.as_view(), name='delete_article'),
]
