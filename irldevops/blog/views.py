from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Post
from django.shortcuts import render
from .forms import CommentForm
# Create your views here.


class ObjectOwnerMixin:

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class PostListView(ListView):
    model = Post
    ordering = ['created']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post


class PostResultsView(DetailView):
    template_name = 'blog/results.html'


class PostUpdateView(ObjectOwnerMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']

    def get_success_url(self):
        return reverse('blog:detail',
                       kwargs={'pk': self.object.pk})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail',
                       kwargs={'pk': self.object.pk})


class PostDeleteView(ObjectOwnerMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')


class CommentView(CreateView):
    form_class = CommentForm
    template_name = 'blog/comment.html'

    def form_valid(self, form):
        comment = form.save(commit=False)

        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        comment.post = post
        comment.author = self.request.user
        comment.save()
        return super(CommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail',
                       kwargs={'pk': self.object.post.pk})
