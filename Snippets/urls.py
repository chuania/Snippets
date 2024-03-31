from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from MainApp import views

urlpatterns = [
    path("", views.index_page, name="home"),
    path("admin/", admin.site.urls),
    path("snippets/add", views.add_snippet, name="snippet-add"),
    path("snippets/list", views.snippets_page, name="snippets-list"),
    path("snippets/my", views.snippets_my, name="snippets-my"),
    path("snippet/<int:snippet_id>", views.snippet_detail, name="snippet-detail"),
    path(
        "snippet/<int:snippet_id>/delete", views.snippet_delete, name="snippet-delete"
    ),
    path("comment/create", views.comment_create, name="comment-create"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("register/", views.registration, name="registration"),
    path(
        "snippet/<int:snippet_id>/editprivacy",
        views.snippet_edit_privacy,
        name="snippet-edit-privacy",
    ),
    path("post/<int:snippet_id>/edit/", views.snippet_edit, name="snippet-edit"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Ctrl + Alt + L
