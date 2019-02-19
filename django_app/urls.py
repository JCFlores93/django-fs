
from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world', views.hello_world),
    path('sorted', views.returnOK),
    path('hi/<str:name>/<int:age>', views.retur_say_hi)
]
