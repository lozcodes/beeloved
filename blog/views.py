# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, slug):
    post_detail = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post_detail})
