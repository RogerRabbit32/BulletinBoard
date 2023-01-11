from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm


@login_required
def logged_view(request):
    return render(request, 'logged_in.html')


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 10


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_add.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)
