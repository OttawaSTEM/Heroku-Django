from django.contrib import admin
from polls.models import Question

class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question 
    
    list_display = [
        'question_1',
    ]

admin.site.register(Question, QuestionAdmin)