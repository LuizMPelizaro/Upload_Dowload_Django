from django.urls.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.index,name=('index')),
]
if settings.DEBUG :
  urlpatterns += static(settings.MEDIA_URL,documet_root=settings.MEDIA_ROOT)