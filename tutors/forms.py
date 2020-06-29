from django import forms
from .widgets import CustomClearableFileInput
from .models import Tutor, Subject


class TutorForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        subjects = Subject.objects.all()
        friendly_names = [(s.id, s.get_friendly_name()) for s in subjects]

        self.fields['subject'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
