from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('',include('skillaqui.urls')),
    path('comments/',include('django_comments.urls')),
    path('login/',LoginView.as_view(),name='login'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
