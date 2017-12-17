from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^post/$',
        view=views.PostListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^post/(?P<pk>\d+)$',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^post/(?P<pk>\d+)/results/$',
        view=views.PostResultsView.as_view(),
        name='results'
    ),
    url(
        regex=r'^post/(?P<pk>\d+)/update/$',
        view=views.PostUpdateView.as_view(),
        name='update'
    ),
    url(regex=r'^post/create/$',
        view=views.PostCreateView.as_view(),
        name='create'),
    url(
        regex=r'^post/(?P<pk>\d+)/delete/$',
        view=views.PostDeleteView.as_view(),
        name='delete'
    )

]
