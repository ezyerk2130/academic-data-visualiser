from django import forms
from .models import Style


class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = [ "title", "instructor", "module_course","academic_year","type","description",]