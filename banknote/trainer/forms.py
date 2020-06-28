from django import forms
from .models import Trainer
class TrainerForm(forms.ModelForm):

    class Meta:
        model=Trainer
        fields = ['Name','Title', 'Facebook_URL','Instagram_URL','Whatsapp_Number','Linkedin_URL','Image_URL']
