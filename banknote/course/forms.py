from django import forms
from .models import Course,QuestionAnswer


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['Name','Description', 'Number_of_Sessions','Course_Content','Price','Start_date','Image']
        widgets = {

            'Description': forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
            'content_session': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            'Start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        fields=['question']
        model=QuestionAnswer
