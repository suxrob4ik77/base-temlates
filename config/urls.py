from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from configapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('configapp.urls'))
    path('',index,name='home'),
    path('',index)
]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
