from django import forms
from .models import Lesson
from .constants import SKILL_LEVELS
#from ajax_select.fields import AutoCompleteSelectMultipleField


class ProfileForm(forms.Form):
    about = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    skill_level = forms.ChoiceField(choices=SKILL_LEVELS)

    def __init__(self, *args, **kwargs):
        profile = self.profile = kwargs.pop('profile')
        user = profile.user
        initial = {'about': profile.about,
                  'first_name': user.first_name,
                  'last_name': user.last_name,
                  'email': user.email,
                  'skill_level':profile.skill_level,
                  }
        kwargs['initial'] = initial
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



class LessonDetails(forms.ModelForm):
    title
    lesson_price
    primary_ingredients
    serving_size
    course_types
    video
    image
    prep_time
    cooking_time
    cuisine_type
    restrictions

    class Meta:
        model =Lesson


class IngredentsDetails(forms.Form):
    pass

class StepDetails(forms.Form):
    pass
