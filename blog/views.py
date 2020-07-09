from django.shortcuts import render
from django.views.generic import View
from .models import Post, Category
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import CategoryForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q


def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__contains=search_query))
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {'page_object': page, 'is_paginated': is_paginated, 'next_url': next_url, 'prev_url': prev_url}

    return render(request, 'blog/index.html', context={'page_object': page})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


class CategoryDetail(ObjectDetailMixin, View):
    model = Category
    template = 'blog/category_detail.html'


class CategoryCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = CategoryForm
    template = 'blog/category_create.html'
    raise_exception = True


class CategoryUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Category
    form_model = CategoryForm
    template = 'blog/category_update_form.html'
    raise_exception = True


class CategoryDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Category
    template = 'blog/category_delete_form.html'
    redirect_url = 'categories_list_url'
    raise_exception = True


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', context={'categories': categories})
