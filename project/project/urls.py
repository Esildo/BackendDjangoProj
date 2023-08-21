
from django.contrib import admin
from django.urls import path
from .views import  main_view
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('api/', include('books.urls'))

]
