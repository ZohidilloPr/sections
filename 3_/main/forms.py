from django import forms
from .models import People, Tuman

class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tuman'].queryset = Tuman.objects.none()

        if 'davlat' in self.data:
            try:
                davlat_id = int(self.data.get('davlat'))
                self.fields['tuman'].queryset = Tuman.objects.filter(davlat_id=davlat_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['tuman'].queryset = self.instance.davlat.tuman_set.all()