from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import handler404, handler500
from django.conf.urls.i18n import i18n_patterns
from forms import views
import forms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('site_dashboard.urls'), name="dashboard"),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('@<str:username>/', views.profile_view, name="profile"),
    path('logout/', views.logout_view, name='logout'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
] + i18n_patterns(
    path('i18n/', include("django.conf.urls.i18n")),
    path('fd/', include('form_dashboard.urls')),
    path('settings/', include('settings.urls')),
    path('', include('forms.urls')),
    prefix_default_language = True
)



if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

handler404 = "forms.views.handler404"
handler500 = "forms.views.handler500"