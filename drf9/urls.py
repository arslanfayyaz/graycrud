from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('app1.urls')),
    path('student/', include('app1.urls')),

    path('university/', include('app1.urls')),
    path('teacher/', include('app1.urls')),
    path('song/', include('app1.urls')),

]
