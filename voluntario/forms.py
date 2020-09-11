from django.forms import ModelForm
from .models import Voluntary

class VoluntaryForm(ModelForm):
    class Meta:
        model = Voluntary
        fields = '__all__'