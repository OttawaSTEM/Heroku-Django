from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

from polls.models import Question

class Question_Form(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_1']

    question_1 = forms.MultipleChoiceField(choices=((1,1), (2, 2)), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(Question_Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('question_1'),
            Submit('sent', ('Submit')),
        )