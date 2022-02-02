from django.contrib import admin
from django.urls import path
from polls.views import Question_View

urlpatterns = [
    path('', Question_View.as_view(), name='polls'),
    path('admin/', admin.site.urls),  
]