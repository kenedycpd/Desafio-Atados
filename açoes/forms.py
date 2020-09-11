from django.forms import ModelForm
from .models import Actions

class ActionsForm(ModelForm):
    class Meta:
        model = Actions
        fields = '__all__'