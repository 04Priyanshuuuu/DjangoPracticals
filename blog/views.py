from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Post
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.is_superuser


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Post.objects.values('category__id', 'category__name').distinct()
        return context


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('blog:post_detail', pk=post.pk)

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

@user_passes_test(is_admin)
@login_required(login_url='login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Create'})

@user_passes_test(is_admin)
@login_required(login_url='login')
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Edit', 'post': post})

@user_passes_test(is_admin)
@login_required(login_url='login')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})


