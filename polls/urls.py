from django.urls import path

from polls.views import Question_View

urlpatterns = [
    path('', Question_View.as_view(), name='polls'),
]