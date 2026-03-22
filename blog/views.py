from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Post , Category
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.is_superuser


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  
        context['selected_category'] = self.request.GET.get('category')
        return context


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user 
        comment.save()
        return redirect('blog:post_detail', pk=post.pk)

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

@user_passes_test(is_admin)
@login_required(login_url='login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
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


