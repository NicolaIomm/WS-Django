from django import forms

from .models import Exam

class CreateUserForm(forms.Form):
    CHOICES = [ ]
    exam_list = Exam.objects.all()
    for e in exam_list:
        CHOICES.append( (e.name, e.name) )
    name = forms.CharField(label='Name', max_length=100)
    age = forms.IntegerField(label='Age')  
    exam = forms.ChoiceField(label='Exam', choices = CHOICES, widget=forms.Select)

class CreateExamForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)

class QueryForm(forms.Form):
    CHOICES = [ ('Aggregate','Aggregate'),
                ('Annotate','Annotate'),
                ('Extra','Extra'),]
    query_type = forms.ChoiceField(label='', choices = CHOICES, widget=forms.RadioSelect)
    column_alias = forms.CharField(label="column_alias", max_length=500)