from django.db.models import fields
from .models import Areas
from django.forms import ModelForm

class AreasForm(ModelForm):
    class Meta:
        model=Areas
        fields='_all_'