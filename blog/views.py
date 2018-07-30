# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    page = request.GET.get('page',1)

    paginator = Paginator(posts_list, 3)
    posts=paginator.page(page)
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, slug):
    post_detail = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post_detail})
