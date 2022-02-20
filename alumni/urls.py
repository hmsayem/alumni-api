from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls'), name = 'blog_api'),
    path('api/blog/', include('blog.api.urls'), name = 'blog_api'),
    path('api/account/', include('account.api.urls'), name = 'account_api'),
    path('', include('django.contrib.auth.urls')),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )

