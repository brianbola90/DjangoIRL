from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from actstream import views as actstream_views

from jet.dashboard.dashboard_modules import google_analytics_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('irldevops.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    # follow unfollow urls
    url(r'^followers/(?P<content_type_id>[^/]+)/(?P<object_id>[^/]+)/$',
        actstream_views.followers, name='actstream_followers'),
    url(r'^following/(?P<user_id>[^/]+)/$',
        actstream_views.following, name='actstream_following'),
    url(r'^follow/(?P<content_type_id>[^/]+)/(?P<object_id>[^/]+)/$',
        actstream_views.follow_unfollow, name='actstream_follow'),
    url(r'^follow_all/(?P<content_type_id>[^/]+)/(?P<object_id>[^/]+)/$',
        actstream_views.follow_unfollow, {'actor_only': False},
        name='actstream_follow_all'),
    url(r'^unfollow_all/(?P<content_type_id>[^/]+)/(?P<object_id>[^/]+)/$',
        actstream_views.follow_unfollow, {'actor_only': False, 'do_follow': False},
        name='actstream_unfollow_all'),
    url(r'^unfollow/(?P<content_type_id>[^/]+)/(?P<object_id>[^/]+)/$',
        actstream_views.follow_unfollow, {'do_follow': False},
        name='actstream_unfollow'),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^taggit/', include('taggit_selectize.urls')),
    url(r'^cookies/', include('cookie_consent.urls'))
   # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
