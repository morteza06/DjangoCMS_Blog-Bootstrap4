from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from djangocms_blog.sitemaps import BlogSitemap

admin.autodiscover()

            #=== Function views
            # 1.Add an import: from my_app import views
            # 2.Add a URL to urlpatterns: path('', views.home, name='home')
            #=== Class-bsed views
            # 1.Add an import: from other_app.views import Home
            # 2.Add a URL to urlpatterns: path('',Home.as_view(), name='home')
            #=== Includeing another URLconf
            # 1.Import the include() function: from django.urls import inculde, path
            # 2.Add a URL to urlpatterns: path('blog/', include('blog.urls'))

urlpatterns = [path(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages':CMSSitemap, 'Blog': BlogSitemap,}}), 
               path('', include('djangocms_blog.taggit_urls'))] 

urlpatterns += i18n_patterns(path('admin/', admin.site.urls), 
                             path('', include('cms.urls')))



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#BLOG_URLCONF = 'mysite.blog_urls'
