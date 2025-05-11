
from django.conf import settings

from django.shortcuts import redirect
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from django.views.generic import TemplateView

from django.contrib import admin
from django.urls import path

from django.urls import path, include, re_path

from .views import (rate_limiter_view, view_404, 
                        handler_403, home_view) #subscribe_view

from .sitemaps import StaticSitemap
# from blog.sitemaps import BlogSitemap

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

handler404 = view_404

handler403 = handler_403

admin.site.site_header = 'Admin panel'           
admin.site.index_title = 'Site Admin'              
admin.site.site_title = 'Admin site'
admin.site.site_url = "" 


sitemap_dict = {'sitemaps': {'static': StaticSitemap}}


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('user/', include('user.urls')),
    path('blog/', include(wagtail_urls)),
    path('contact-us/', include('inquiry.urls')),
    

    path('sitemap.xml', sitemap, sitemap_dict, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('ratelimit-error/', rate_limiter_view, name='ratelimit-error'),
    
    # wagtail urls
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),

    # add new path here

    path('', home_view, name='home'),

    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
   urlpatterns +=  []

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   
urlpatterns += [ re_path(r'^.*/$', view_404, name='page_not_found'),]