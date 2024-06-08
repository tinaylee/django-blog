from django.urls import path
from blogging.views import PostDetailView
from blogging.views import PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
]
