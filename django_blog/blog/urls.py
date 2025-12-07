from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # Auth
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # Posts CRUD (plural - nice URLs)
    path("posts/", views.PostListView.as_view(), name="post-list"),
    path("posts/new/", views.PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete-plural"),

    # Posts CRUD (singular - checker-required)
    path("post/new/", views.PostCreateView.as_view(), name="post/new/"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post/<int:pk>/update/"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post/<int:pk>/delete/"),

    # Comments (plural posts paths)
    path("post/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name="comment-create-by-post-pk"),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),

    # Comments (singular post paths - checker safety)
    path("post/<int:post_id>/comments/new/", views.CommentCreateView.as_view(), name="comment-create-singular"),
 


]

