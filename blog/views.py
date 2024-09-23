# views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    tag = request.GET.get('tag')  # Получаем тег из GET-запроса
    if tag:
        posts = Post.objects.filter(tags__icontains=tag)
    else:
        posts = Post.objects.all()

    return render(request, 'post_list.html', {'posts': posts})

def post_list(request):
    query = request.GET.get('q')
    tag = request.GET.get('tag')

    posts = Post.objects.all()

    if query:
        posts = posts.filter(title__icontains=query)
    if tag:
        posts = posts.filter(tags__icontains=tag)

    return render(request, 'post_list.html', {'posts': posts})


# views.py
def post_list(request):
    query = request.GET.get('q')  # Получаем поисковый запрос
    tag = request.GET.get('tag')

    posts = Post.objects.all()

    if query:
        posts = posts.filter(title__icontains=query)  # Фильтр по заголовку
    if tag:
        posts = posts.filter(tags__icontains=tag)  # Фильтр по тегу

    return render(request, 'post_list.html', {'posts': posts})
