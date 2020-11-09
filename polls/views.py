from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from . import forms

class Question_View(generic.TemplateView):
    template_name = 'polls/index.html'
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        kwargs['form'] = forms.Question_Form()
        return super(Question_View, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_instance = forms.Question_Form(request.POST)
        print(form_instance)
        if form_instance.is_valid():
            # temp = form_instance.cleaned_data.get('question_1') 
            # print(temp) 
            form_instance = form_instance.save(commit=False)
            form_instance.save()

            return HttpResponseRedirect(reverse_lazy('polls'))        
        else:
            return super(Question_View, self).get(request)