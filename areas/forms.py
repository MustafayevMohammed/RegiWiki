from django import forms
from django.db.models import fields
from django.forms import widgets
from . import models
import areas

class CommentForm(forms.ModelForm):
    class Meta:
        widgets = {
            "basliq" : forms.TextInput(attrs={'class':'fields'}),
            "rayon" : forms.Select(attrs={'class':'fields'}),
            "mezmun" :forms.Textarea(attrs={'class':'fields',
            'cols':81,
            'rows':8,
            'style':'resize:none;'}),
            "sekil" : forms.ClearableFileInput(attrs={'class':'fields'})
        }
        model = models.CommentModel
        exclude = ["created_date","yazan"]


class ConversationForm(forms.ModelForm):
    class Meta:
        widgets = {
            "mezmun" : forms.Textarea(attrs={"class":"fields",
            "cols":81,
            "rows":6,
            "style":"resize:none;"}),
        }
        model = models.ConversationModel
        fields = ["mezmun"]