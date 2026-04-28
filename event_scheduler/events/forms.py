from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event name'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Event description (optional)'}),
        }

    def __init__(self, *args, user=None, instance=None, **kwargs):
        self.user = user
        super().__init__(*args, instance=instance, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time and self.user:
            conflict_qs = Event.objects.filter(user=self.user, date=date, time=time)
            if self.instance and self.instance.pk:
                conflict_qs = conflict_qs.exclude(pk=self.instance.pk)
            if conflict_qs.exists():
                raise forms.ValidationError(
                    "You already have an event scheduled at this date and time. Please choose a different time."
                )
        return cleaned_data
