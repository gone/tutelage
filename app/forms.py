

from django import forms

#from ajax_select.fields import AutoCompleteSelectMultipleField


class ProfileForm(forms.Form):
    about = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    skill_level = forms.ChoiceField(choices=(
            ("Novice", "Novice"),
            ("Intermediate", "Intermediate"),
            ("Advanced", "Advanced"),
            ("Professional", "Professional"),
            ))

    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop('profile')
        return super(ProfileForm, self).__init__(*args, **kwargs)


    def save(self):
        self.profile.skill_level = self.cleaned_data['skill_level']
        self.profile.about = self.cleaned_data['about']
        self.profile.user.first_name = self.cleaned_data['first_name']
        self.profile.user.last_name = self.cleaned_data['last_name']
        self.profile.user.email = self.cleaned_data['email']
        self.profile.user.save()
        self.profile.save()
        return self.profile
