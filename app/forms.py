import decimal

from django import forms
from .models import Lesson, LessonIngredient, LessonRequest, LessonPledge, Step, ChefPledge, Tool, Customer
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
                  'skill_level': profile.skill_level,
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

class LessonDetailsForm(forms.ModelForm):
    # video

    cooking_time = forms.CharField()
    prep_time = forms.CharField()
    def clean_prep_time(self):
        prep_time = self.cleaned_data['prep_time']
        if not ":" in prep_time:
            prep_time = "00:%s:00" % prep_time
        return prep_time
    def clean_cooking_time(self):
        cooking_time = self.cleaned_data['cooking_time']
        if not ":" in cooking_time:
            cooking_time = "00:%s:00" % cooking_time
        return cooking_time

    def clean_title(self):
        title = self.cleaned_data['title']
        try:
            old_lesson = Lesson.objects.get(title=title, teacher_id=self.teacher.id)
            if old_lesson.id == getattr(self.instance, 'id', False):
                return title
            raise forms.ValidationError("You already have a lesson with that name")
        except Lesson.DoesNotExist:
            return title

    def save(self, *args, **kwargs):
        instance = super(LessonDetailsForm, self).save(*args, **kwargs)
        instance.teacher = self.teacher
        instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.teacher = kwargs.pop('teacher')
        return super(LessonDetailsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Lesson
        fields = ('description', 'title', 'image', 'price', 'serving_size',
                  'prep_time', 'cooking_time', 'cuisine', 'restrictions',
                  'course', 'primary_ingredients', 'kind',)

        widgets = {
             'primary_ingredients': forms.SelectMultiple(attrs={'class': 'chzn'}),
             'course': forms.SelectMultiple(attrs={'class':'chzn'}),
             'restrictions': forms.SelectMultiple(attrs={'class':'chzn'}),
             'cuisine': forms.SelectMultiple(attrs={'class':'chzn'}),
             'kind': forms.RadioSelect,
             'title': forms.TextInput(attrs={'class':"create-lesson-input-mid", 'placeholder':"Lesson Title"}),
             'teacher': forms.HiddenInput
        }

class IngredentsDetailsForm(forms.ModelForm):

    class Meta:
        model = LessonIngredient
        fields =  ("ingredient", "measurement")

class ToolsDetailsForm(forms.ModelForm):

    class Meta:
        model = Tool
        fields =  ("name", )


class StepDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        rv = super(StepDetailsForm, self).__init__(*args, **kwargs)
        try:
            self.fields['tools'].queryset = self.instance.lesson.tools.all()
            self.fields['ingredients'].queryset = self.instance.lesson.lessoningredient_set.all()
        except:
            self.fields['tools'].queryset = self.initial['lesson'].tools.all()
            self.fields['ingredients'].queryset = self.initial['lesson'].lessoningredient_set.all()
        return rv

    class Meta:
        model = Step

class ChefPledgeForm(forms.ModelForm):

    def __init__(self, user=None, lesson_req=None, *args, **kwargs):
        self.user = user
        self.lesson_req = lesson_req
        super(ChefPledgeForm, self).__init__(*args, **kwargs)
        self.fields['amount_required'].label = "How much do you need to make this lesson?"

    def save(self, *args, **kwargs):
        kwargs.pop('commit', None)
        chefpledge = super(ChefPledgeForm, self).save(commit=False, *args, **kwargs)
        chefpledge.user = self.user
        chefpledge.request = self.lesson_req
        chefpledge.save()
        return chefpledge

    class Meta:
        model = ChefPledge
        exclude = ('active','request', 'user')

class ContributionForm(forms.ModelForm):
    request_slug = forms.CharField()

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        return super(ContributionForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        kwargs.pop('commit', None)
        try:
            contribute = LessonPledge.objects.get(user=self.user, request=self.req)
            contribute.amount = self.cleaned_data['amount']
        except LessonPledge.DoesNotExist:
            contribute = super(ContributionForm, self).save(commit=False, *args, **kwargs)
            contribute.user = self.user
            contribute.request = self.req
        contribute.save()
        return contribute

    def clean_request_slug(self):
        slug = self.cleaned_data['request_slug']
        try:
            self.req = LessonRequest.objects.get(slug=slug)
        except LessonRequest.DoesNotExist:
            raise forms.ValidationError()
        return self.cleaned_data['request_slug']

    def clean(self):
        try:
            self.user.customer
            return super(ContributionForm, self).clean()
        except Customer.DoesNotExist:
            raise forms.ValidationError("We need a credit card to bill you")

    class Meta:
        model = LessonPledge
        fields = ('amount', 'email')


class LessonRequestForm(forms.ModelForm):

    initial = forms.CharField(label="Initial Contribution")
    email = forms.BooleanField(required=False)

    class Meta:
        model = LessonRequest
        fields = ('title', 'kind', 'restrictions', 'serving_size',
                  'time_in_min', 'cuisine', 'restrictions',
                  'course', 'primary_ingredients', 'description',
                  'need_by')

        widgets = {
             'primary_ingredients': forms.SelectMultiple(attrs={'class': 'chzn'}),
             'course': forms.SelectMultiple(attrs={'class':'chzn'}),
             'restrictions': forms.SelectMultiple(attrs={'class':'chzn'}),
             'cuisine': forms.SelectMultiple(attrs={'class':'chzn'}),
             'need_by': forms.DateTimeInput(attrs={'class':'datepicker'}),
             'kind': forms.RadioSelect,
             'title': forms.TextInput(attrs={'class':"create-lesson-input-mid", 'placeholder':"Lesson Title"}),
             'teacher': forms.HiddenInput
        }


    def __init__(self, request, *args, **kwargs):
        user = self.user = request.user
        rv =  super(LessonRequestForm, self).__init__(*args, **kwargs)
        self.fields['kind'].label = "Type"
        self.fields['title'].label = "Name"
        self.fields['time_in_min'].label = "Time Required"
        self.fields['serving_size'].label = "Serving Size"
        return rv

    def save(self, *args, **kwargs):
        lesson_request = super(LessonRequestForm, self).save(*args, **kwargs)
        initial = decimal.Decimal(self.cleaned_data['initial'])
        email = self.cleaned_data['email']
        LessonPledge.objects.create(user=self.user,
                                    amount=initial,
                                    email=email,
                                    request=lesson_request
                                    )
        return lesson_request


class LessonPurchaseForm(forms.Form):

    def __init__(self, user, lesson, *args, **kwargs):
        self.user = user
        self.lesson = lesson
        return super(LessonPurchaseForm, self).__init__(*args, **kwargs)

    def clean(self):
        try:
            self.user.customer
            return super(LessonPurchaseForm, self).clean()
        except Customer.DoesNotExist:
            raise forms.ValidationError("We need a credit card to bill you")

    def save(self, *args, **kwargs):
        self.lesson.followers.add(self.user)
