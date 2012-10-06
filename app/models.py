import re
from datetime import datetime
import time


from django.db import models
from django.contrib.auth.models import User
from mezzanine.pages.models import Page
from mezzanine.core.models import Displayable
from mezzanine.core.fields import RichTextField

from ecl_django.models import CreatedMixin


def file_url(name):
    def inner(instance, filename):
        r = re.compile(r'[^\S]')
        filename = r.sub('', filename)
        now = datetime.now()
        timestamp = int(time.time())
        return 'uploads/{0}/{1.year:04}/{1.month:02}/{1.day:02}/{2}/{3}'.format( \
                name, now, timestamp, filename)
    return inner


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


class FeaturedChef(Page):
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
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name

class Tool(CreatedMixin):
    name = models.CharField(max_length=32, unique=True)

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
    user = models.ForeignKey(User)
    phone = models.CharField(max_length=10, unique=True)
    about = models.CharField(max_length=300, default='')

    ingredients = models.ManyToManyField(Ingredient, related_name='profiles')
    tools = models.ManyToManyField(Tool, related_name='profiles')

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



class Recipie(CreatedMixin, Displayable):
    tags = models.CharField(max_length=128, default="")
    ## ingredients = models.ManyToManyField(Ingredient, related_name='recipies')
    ## tools = models.ManyToManyField(Tool, related_name='recipies')
    #techniques = asdf

    # @property
    # def rating(self):
    #     #TODO: user proper rating algo. Find that sucker online.
    #     result = self.ratings.aggregate(avg=Avg('rating'))['avg']
    #     if not result:
    #         return 0
    #     return result

    # def __unicode__(self):
    #     return self.title




class Lesson(CreatedMixin, Displayable):
    teacher = models.ForeignKey(User, related_name='lessons_teaching')
    recipie = models.ForeignKey(Recipie, related_name='lessons')
    video = models.FileField(upload_to=file_url("lessonvideos"))

    flavor_text = models.TextField(default="")
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    users_who_rated = models.ManyToManyField(User, through='LessonRating', related_name='rated_lessons')
    followers = models.ManyToManyField(User, related_name='lessons_taking',  blank=True, null=True)

    class Meta():
        unique_together = ('teacher', 'title')

    @property
    def rating(self):
        #TODO: user proper rating algo. Find that sucker online.
        result = self.ratings.aggregate(avg=Avg('rating'))['avg']
        if not result:
            return 0
        return result

    def __unicode__(self):
        return self.title



class Step(CreatedMixin):
    lesson = models.ForeignKey(Lesson, related_name='steps')
    order = models.PositiveSmallIntegerField(default=0)
    start_time = models.IntegerField(null=True, blank=True)
    end_time = models.IntegerField(null=True, blank=True)

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
