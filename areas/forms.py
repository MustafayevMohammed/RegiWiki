from django import forms
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