from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^post/$',
        view=views.PostListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^post/(?P<slug>[\w-]+)$',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^post/(?P<slug>[\w-]+)/results/$',
        view=views.PostResultsView.as_view(),
        name='results'
    ),
    url(
        regex=r'^post/(?P<slug>[\w-]+)/update/$',
        view=views.PostUpdateView.as_view(),
        name='update'
    ),
    url(regex=r'^post/create/$',
        view=views.PostCreateView.as_view(),
        name='create'),
    url(
        regex=r'^post/(?P<slug>[\w-]+)/delete/$',
        view=views.PostDeleteView.as_view(),
        name='delete'
    ),
    url(
        regex=r'^post/(?P<slug>[\w-]+)/comment/$',
        view=views.CommentView.as_view(),
        name='comment'
    ),
    url(
        regex=r'^post/drafts/$',
        view=views.PostListMyUnpulbished.as_view(),
        name='drafts'
    ),
    url(
        regex=r'^post/(?P<slug>[-\w]+)/publish/$',
        view=views.PublishPostView.as_view(),
        name='publish'
     ),
    url(
        regex=r'^tag/(?P<slug>[-\w]+)/$',
        view=views.TagIndexView.as_view(),
        name='tagged'
    ),




]
