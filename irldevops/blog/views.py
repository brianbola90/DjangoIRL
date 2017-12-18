from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Post
# Create your views here.


class PostListView(ListView):
    model = Post
    ordering = ['created']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post


class PostResultsView(DetailView):
    template_name = 'blog/results.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']

    def get_success_url(self):
        return reverse('blog:detail',
                       kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(PostUpdateView, self).get_object()
        if not obj.author == self.request.user:
            raise PermissionDenied
        return obj


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail',
                       kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(PostDeleteView, self).get_object()
        if not obj.author == self.request.user:
            raise PermissionDenied
        return obj
