from django.http import Http404, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib import auth
from MainApp.models import Snippet, Language
from MainApp.forms import SnippetForm, UserRegistrationForm, CommentForm
from django.contrib import messages


def index_page(request):
    id = request.GET.get("id")
    if id:
        try:
            snippet = Snippet.objects.get(id=id)
            # snippet = get_object_or_404(id=id)
            context = {
                "pagename": "PythonBin",
                "snippet": snippet,
            }
            return render(request, "pages/index.html", context)
        except ObjectDoesNotExist:
            context = {
                "pagename": "PythonBin",
            }
            return render(request, "pages/index.html", context)
    else:
        context = {
            "pagename": "PythonBin",
        }
    return render(request, "pages/index.html", context)


def add_snippet(request):
    if request.method == "GET":  # получить страницу с формой
        form = SnippetForm()
        context = {"form": form, "pagename": "Добавление нового сниппета"}
        return render(request, "pages/add_snippet.html", context)
    elif request.method == "POST":  # получить данные от формы
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
        return redirect("snippets-list")


# 127.0.0.1:8000/snippets/list?sort=name
def snippets_page(request):
    snippets = Snippet.objects.filter(private=False) | Snippet.objects.filter(
        user=request.user.id
    )
    languages = Language.objects.all()
    sort = request.GET.get("sort")
    lang = request.GET.get("lang")
    user = request.GET.get("user")
    if sort:
        snippets = snippets.order_by(sort)
    if lang:
        snippets = snippets.filter(lang=lang)
    if user:
        snippets = snippets.filter(user=user)
    users = User.objects.annotate(num_snippets=Count("snippets")).exclude(
        num_snippets=0
    )
    context = {
        "pagename": "Просмотр сниппетов",
        "snippets": snippets,
        "sort": sort,
        "lang": lang,
        "users": users,
        "languages": languages,
    }
    return render(request, "pages/view_snippets.html", context)


def snippet_edit_privacy(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    if snippet.user != request.user:
        raise PermissionDenied()
    else:
        if snippet.private:
            Snippet.objects.filter(id=snippet_id).update(private=False)
        else:
            Snippet.objects.filter(id=snippet_id).update(private=True)
    return redirect("snippets-my")


def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.save()
            return redirect("snippet-detail", snippet_id)
    else:
        form = SnippetForm(instance=snippet)

    context = {"form": form, "pagename": "Редактирование сниппета"}
    return render(request, "pages/add_snippet.html", context)


@login_required
def snippets_my(request):
    my_snippets = Snippet.objects.filter(user=request.user)
    context = {"pagename": "Мои сниппеты", "snippets": my_snippets}
    return render(request, "pages/view_snippets.html", context)


def snippet_detail(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    comment_form = CommentForm()
    context = {
        "pagename": "Информация о сниппете",
        "snippet": snippet,
        "comment_form": comment_form,
    }
    return render(request, "pages/snippet-detail.html", context)


def snippet_delete(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    if snippet.user != request.user:
        raise PermissionDenied()
    snippet.delete()
    return redirect("snippets-my")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login successful")
        else:
            messages.error(request, "User is not found")
        return redirect("home")


def logout_page(request):
    auth.logout(request)
    return redirect("home")


def registration(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        context = {"pagename": "Регистрация", "form": form}
        return render(request, "pages/registration.html", context)
    elif request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:  # данные не валидные
            context = {"pagename": "Регистрация", "form": form}
            return render(request, "pages/registration.html", context)
        return redirect("home")


def comment_create(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST, request.FILES)
        snippet_id = request.POST.get("snippet_id")
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            snippet = Snippet.objects.get(id=snippet_id)
            comment.snippet = snippet
            comment.save()
        else:
            raise ValidationError(
                "Filetype not supported. Supported formats are png, jpeg, gif. The maximum size is 2.5MB."
            )
        return redirect(request.META.get("HTTP_REFERER", "/"))
