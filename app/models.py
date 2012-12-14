import re
from datetime import datetime
#import magic
import time
from itertools import chain


from django.conf import settings
from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from django.utils.functional import cached_property

from mezzanine.pages.models import Page
from mezzanine.core.models import Displayable
from mezzanine.core.fields import RichTextField



from durationfield.db.models.fields.duration import DurationField

from .constants import SKILL_LEVELS, VIDEO_TYPE, VIDEO_SUBTYPES


UPLOADS_DIR = 'uploads/{0}/{1.year:04}/{1.month:02}/{1.day:02}/{2}/{3}'


def file_url(name):
    def inner(instance, filename):
        r = re.compile(r'[^\S]')
        filename = r.sub('', filename)
        now = datetime.now()
        timestamp = int(time.time())
        return  UPLOADS_DIR.format(name, now, timestamp, filename)
    return inner


class CreatedMixin(models.Model):
    """
    Abstract model mixin that adds `created_on` and `updated_on` fields to
    models.
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta():
        abstract = True


class Home(Page):
    call_to_action = RichTextField()
    hero = models.ImageField(upload_to=file_url("home_hero"))


class HomeBlock(CreatedMixin):
    home = models.ForeignKey(Home, related_name="blocks")
    header = models.CharField(max_length=126)
    body = RichTextField()
    link_copy = models.CharField(max_length=126)
    link_target = models.CharField(max_length=126)


class About(Page):
    blockone = RichTextField()
    blocktwo = RichTextField()
    blockthree = RichTextField()
    hero = models.ImageField(upload_to=file_url("about_hero"))


class FeaturedChef(Displayable):
    intro_video = models.ImageField(upload_to=file_url("featured_chef_intro"))
    intro_text = RichTextField()
    chef = models.OneToOneField(User, related_name="featured_chef")
    featured_lessons = models.ManyToManyField("Lesson")

##############################
# class Tag(CreatedMixin):   #
#     tag = asdf             #
#     icon = asdf            #
#     details = asdf         #
#     section = asdf         #
#                            #
#     def __unicode__(self): #
#         return self.name   #
##############################


class Ingredient(CreatedMixin):
    name = models.CharField(max_length=32, null=False)

    def __unicode__(self):
        return self.name

class LessonIngredient(CreatedMixin):
    ingredient = models.ForeignKey(Ingredient)
    lesson = models.ForeignKey("Lesson")
    number = models.IntegerField(null=False, blank=False, default="0")
    measurement = models.CharField(max_length=32, null=False)
    prep = models.CharField(max_length=32)

    def __unicode__(self):
        return "%s %s of %s" % (self.number, self.measurement, self.ingredient)


class Tool(CreatedMixin):
    name = models.CharField(max_length=32, null=False)
    size = models.CharField(max_length=32, null=False)
    type = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Category(CreatedMixin):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class SubCategory(CreatedMixin):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey(Category, related_name='subcategories')

    def __unicode__(self):
        return self.name

    class Meta():
        unique_together = ('name', 'parent')


class Profile(CreatedMixin):
    user = models.OneToOneField(User)
    about = models.CharField(max_length=300, default='', blank=True)

    ingredients = models.ManyToManyField(Ingredient, related_name='profiles', blank=True)
    tools = models.ManyToManyField(Tool, related_name='profiles', blank=True)
    skill_level = models.IntegerField(choices=SKILL_LEVELS, default=0)

    professional_chef = models.BooleanField(default=False)

    location = models.CharField(max_length=255, blank=True)
    website1 = models.CharField(max_length=255, blank=True)
    website1_url = models.URLField(blank=True)
    website2 = models.CharField(max_length=255, blank=True)
    website2_url = models.URLField(blank=True)

    facebook =  models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    pinterest = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    googleplus = models.URLField(blank=True)
    tumblr = models.URLField(blank=True)

    course = models.ManyToManyField('Course', blank=True)
    cuisine = models.ManyToManyField('Cuisine', blank=True)
    restrictions = models.ManyToManyField("DietaryRestrictions", blank=True)

    Testimonial1_text = models.TextField(blank=True)
    Testimonial1_src = models.CharField(max_length=255, blank=True)

    Testimonial2_text = models.TextField(blank=True)
    Testimonial2_src = models.CharField(max_length=255, blank=True)

    Testimonial3_text = models.TextField(blank=True)
    Testimonial3_src = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return unicode(self.user)


class CreditCard(CreatedMixin):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=32, null=True, blank=True)
    exp_month = models.CharField(max_length=2, null=True, blank=True)
    exp_year = models.CharField(max_length=4, null=True, blank=True)
    last_4 = models.CharField(max_length=4, null=True, blank=True)
    zip = models.CharField(max_length=5, null=True, blank=True)
    address_1 = models.CharField(max_length=128, null=True, blank=True)
    address_2 = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    country = models.CharField(max_length=32, null=True, blank=True)

    stripe_customer_id = models.CharField(max_length=32, null=True, blank=True)


class Video(CreatedMixin):
    video = models.FileField(upload_to=file_url("lessonvideos"))
    lesson = models.ForeignKey('Lesson', related_name='videos')

    def get_absolute_url(self):
        return "%s%s" % (settings.MEDIA_URL, self.video)

    # def validate_video(self):
    #     try:
    #         f = self.video.file
    #     except ValueError:
    #         raise ValidationError("Need a Video File")
    #     # TODO: choice the video types to support
    #     mime = magic.from_buffer(f.read(1024), mime=True)
    #     try:
    #         type_, subtype = mime.split('/')
    #     except ValueError:
    #         raise ValidationError("The file must be a video")
    #     if type_ != VIDEO_TYPE:
    #         raise ValidationError("The file must be a video")
    #     if subtype not in VIDEO_SUBTYPES:
    #         raise ValidationError("Video format not suported")

    # def clean(self):
    #     self.validate_video()


class Lesson(CreatedMixin, Displayable):
    #title included thanks to displayable
    teacher = models.ForeignKey(User, related_name='teaching')
    image = models.FileField(upload_to=file_url("lessonimage"))
    flavor_text = models.TextField(default="")
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True,
                                blank=True)
    users_who_rated = models.ManyToManyField(User, through='LessonRating',
                                             related_name='rated_lessons')

    followers = models.ManyToManyField(User, related_name='lessons',
                                       blank=True, null=True)
    serving_size = models.IntegerField()

   #tags = models.ChraField(max_length=128, default="")

    prep_time = DurationField()
    cooking_time = DurationField()

    primary_ingredients = models.ManyToManyField(Ingredient, related_name='primary_lessons')
    course = models.ManyToManyField('Course')
    cuisine = models.ManyToManyField('Cuisine')
    restrictions = models.ManyToManyField("DietaryRestrictions")

    kind = models.SmallIntegerField(choices=((0, "Recipe"),
                                             (1, "Technique")), default=0)

    ingredients = models.ManyToManyField(Ingredient, through="LessonIngredient", related_name="lessons")
    tools = models.ManyToManyField(Tool, related_name="lessons")

    class Meta():
        unique_together = ('teacher', 'title')

    @cached_property
    def tags(self):
        """Grabs a list of the lessons dietary restrictions, cuisines, courses,
        and primary ingredients from the database"""
        primary_ingredients = self.primary_ingredients.all()
        course = self.course.all()
        cuisine = self.cuisine.all()
        restrictions = self.restrictions.all()
        #list it to prevent caching the generator
        return list(chain(primary_ingredients, course, cuisine, restrictions))

    @property
    def rating(self):
        #TODO: user proper rating algo. http://www.evanmiller.org/how-not-to-sort-by-average-rating.html
        result = self.ratings.aggregate(avg=Avg('rating'))['avg']
        if not result:
            return 0
        return int(result)

    @property
    def prep_in_min(self):
        return max(self.prep_time.total_seconds() / 60, 1)

    @property
    def cook_in_min(self):
        return max(self.prep_time.total_seconds() / 60, 1)


    def __unicode__(self):
        return self.title


class Step(CreatedMixin):
    lesson = models.ForeignKey(Lesson, related_name='steps')
    title = models.CharField(max_length=128, blank=False, null=False)

    text = models.TextField()

    order = models.PositiveSmallIntegerField(default=0)
    start_time = models.IntegerField(null=True, blank=True)
    technique = models.ManyToManyField(Lesson, related_name="technique_steps", blank=True)
    ingredients = models.ManyToManyField(LessonIngredient, related_name="steps", blank=True)
    tools = models.ManyToManyField(Tool, related_name="steps", blank=True)

    class Meta():
        ordering = ('order',)
        unique_together = ('lesson', 'order')

    def __unicode__(self):
        return "Step {}".format(self.order)


class LessonRating(CreatedMixin):
    user = models.ForeignKey(User, related_name='ratings')
    lesson = models.ForeignKey(Lesson, related_name='ratings')
    rating = models.PositiveSmallIntegerField(choices=(
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)))

    class Meta():
        unique_together = ('user', 'lesson')


class Course(CreatedMixin):
    course = models.CharField(max_length=256)

    def __unicode__(self):
        return self.course


class Cuisine(CreatedMixin):
    cuisine = models.CharField(max_length=256)

    def __unicode__(self):
        return self.cuisine


class DietaryRestrictions(CreatedMixin):
    restriction = models.CharField(max_length=256)

    def __unicode__(self):
        return self.restriction
