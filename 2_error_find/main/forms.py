from django import forms
from .models import Student, Abilty, School

abiltie = Abilty.objects.all()

class AddStudent(forms.ModelForm):
    abilty = forms.ModelMultipleChoiceField(queryset=abiltie, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Student
        fields = ['f_name', 'tuman', 'maktab', 'abilty', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['maktab'].queryset = School.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get('tuman'))
                self.fields['maktab'].queryset = School.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['maktab'].queryset = self.instance.tuman.maktab_set.all() 