import re
from datetime import datetime
#import magic
import time
from itertools import chain

from django.conf import settings

import magic


from boto.elastictranscoder.layer1 import ElasticTranscoderConnection
elastic_connection = ElasticTranscoderConnection(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
ENCODING_PIPELINE = "1362949390843-834791" # culiation-transcode


from boto.s3.connection import S3Connection
s3_connection = S3Connection(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

MAIN_BUCKET = settings.AWS_STORAGE_BUCKET_NAME
ENCODING_BUCKET = settings.AWS_ENCODING_BUCKET_NAME



from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from django.utils.functional import cached_property

from django.template.defaultfilters import slugify, timeuntil

from django.db.models import Sum

from django.core.urlresolvers import reverse

from mezzanine.pages.models import Page
from mezzanine.core.models import Displayable
from mezzanine.core.fields import RichTextField


from durationfield.db.models.fields.duration import DurationField

from .constants import SKILL_LEVELS, VIDEO_TYPE, VIDEO_SUBTYPES


UPLOADS_DIR = 'uploads/{0}/{1.year:04}/{1.month:02}/{1.day:02}/{2}/{3}'



from decimal import Decimal
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^app\.models\.CurrencyField"])

class CurrencyField(models.DecimalField):
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        try:
           return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
        except AttributeError:
           return None


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


class FeaturedChef(CreatedMixin,Displayable):
    chef = models.OneToOneField(User, related_name="featured_chef")
    # featured_lessons = models.ManyToManyField("Lesson")
    # intro_video = models.ImageField(upload_to=file_url("featured_chef_intro"))
    # intro_text = RichTextField()


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
    image = models.ImageField(upload_to=file_url("ingredient_images"), null=True, blank=True)
    category = models.CharField(max_length=32, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    substitution1 = models.CharField(max_length=32, null=True, blank=True)
    substitution2 = models.CharField(max_length=32, null=True, blank=True)
    product_link = models.URLField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name

class LessonIngredient(CreatedMixin):
    name = models.CharField(max_length=32, null=False)
    ingredient = models.ForeignKey(Ingredient, blank=True, null=True, on_delete=models.SET_NULL)
    lesson = models.ForeignKey("Lesson")
    number = models.IntegerField(null=False, blank=False, default="0")
    measurement = models.CharField(max_length=32, null=False, blank=True)
    prep = models.CharField(max_length=32, blank=True)

    def __unicode__(self):
        return self.name
        #return "%s, %s" % (self.ingredient, self.measurement)


class Tool(CreatedMixin):
    name = models.CharField(max_length=32, null=False)
    size = models.CharField(max_length=32, null=True, default="")
    type = models.CharField(max_length=32, null=True, default="")
    image = models.ImageField(upload_to=file_url("tool_images"), null=True, blank=True)
    category = models.CharField(max_length=32, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    substitution1 = models.CharField(max_length=32, null=True, blank=True)
    substitution2 = models.CharField(max_length=32, null=True, blank=True)
    product_link = models.URLField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name

class LessonTool(CreatedMixin):
    name = models.CharField(max_length=32, null=False)
    tool = models.ForeignKey(Tool, blank=True, null=True, on_delete=models.SET_NULL)
    lesson = models.ForeignKey("Lesson")

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
    #skill_level = models.IntegerField(choices=SKILL_LEVELS, default=0)

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

    testimonial1_text = models.TextField(blank=True)
    testimonial1_src = models.CharField(max_length=255, blank=True)
    testimonial1_link = models.URLField(max_length=255, blank=True)

    testimonial2_text = models.TextField(blank=True)
    testimonial2_src = models.CharField(max_length=255, blank=True)
    testimonial2_link = models.URLField(max_length=255, blank=True)

    testimonial3_text = models.TextField(blank=True)
    testimonial3_src = models.CharField(max_length=255, blank=True)
    testimonial3_link = models.URLField(max_length=255, blank=True)

    personal_video = models.FileField(upload_to=file_url("personal_video"), blank=True)
    personal_video_image = models.ImageField(upload_to=file_url("personal_video_intro"), blank=True)
    video = models.ForeignKey("Video", related_name="profiles", null=True, blank=True)

    @cached_property
    def tags(self):
        """Grabs a list of the lessons dietary restrictions, cuisines, courses,
        and primary ingredients from the database"""
        course = self.course.all()
        cuisine = self.cuisine.all()
        restrictions = self.restrictions.all()
        #list it to prevent caching the generator
        return list(chain(course, cuisine, restrictions))


    def __unicode__(self):
        return unicode(self.user)




# class CreditCard(CreatedMixin):
#     user = models.ForeignKey(User)
#     name = models.CharField(max_length=128)
#     type = models.CharField(max_length=32, null=True, blank=True)
#     exp_month = models.CharField(max_length=2, null=True, blank=True)
#     exp_year = models.CharField(max_length=4, null=True, blank=True)
#     last_4 = models.CharField(max_length=4, null=True, blank=True)
#     zip = models.CharField(max_length=5, null=True, blank=True)
#     address_1 = models.CharField(max_length=128, null=True, blank=True)
#     address_2 = models.CharField(max_length=128, null=True, blank=True)
#     state = models.CharField(max_length=2, null=True, blank=True)
#     country = models.CharField(max_length=32, null=True, blank=True)

#     stripe_customer_id = models.CharField(max_length=32, null=True, blank=True)


class Customer(CreatedMixin):
    user = models.OneToOneField(User)
    customer_id = models.CharField(max_length=128)

class Video(CreatedMixin):
    video = models.FileField(upload_to=file_url("lessonvideos"))

    def get_absolute_url(self):
        return "%s%s" % (settings.MEDIA_URL, self.video)

    def validate_video(self):
        try:
            f = self.video.file
        except ValueError:
            raise ValidationError("Need a Video File")
        # TODO: choice the video types to support
        mime = magic.from_buffer(f.read(1024), mime=True)
        f.seek(0)

        try:
            type_, subtype = mime.split('/')
        except ValueError:
            raise ValidationError("The file must be a video")
        if type_ != VIDEO_TYPE:
            raise ValidationError("The file must be a video")
        if subtype not in VIDEO_SUBTYPES:
            raise ValidationError("Video format not suported")

    def clean(self):
        self.validate_video()


    def encode_video(self):
        #copy movie to transcoding bucket
        source_bucket = s3_connection.get_bucket(MAIN_BUCKET)
        dest_bucket = s3_connection.get_bucket(ENCODING_BUCKET)
        key = source_bucket.get_key(unicode(self.video))
        dest_key = dest_bucket.get_key(unicode(self.video))
        if not dest_key:
            key.copy(dest_bucket, unicode(self.video))

        dest = unicode(self.video).replace('/lessonvideos/', '/encodedvideos/')
        existing = source_bucket.get_key(dest)

        if not existing:
            input_dict = {
                "Key":unicode(self.video),
                "FrameRate":"auto",
                "Resolution":"auto",
                "AspectRatio":"auto",
                "Interlaced":"auto",
                "Container":"auto",
                }

            output_dict = {
                "Key": dest,
                "ThumbnailPattern":"",
                "Rotate":"auto",
                "PresetId":"1351620000000-100070", #web
                }
            elastic_connection.create_job(ENCODING_PIPELINE, input_dict, output_dict)
            TranscodedVideo.objects.create(video=self, encoded=dest)

        def save(self, *args, **kwargs):
            super(self.__class__, self).save()
            self.encode_video()

class TranscodedVideo(CreatedMixin):
    video = models.ForeignKey(Video, related_name="codecs")
    encoded = models.FileField(upload_to=file_url("encodedvideos"), blank=True, null=True)

    def get_absolute_url(self):
        return "%s%s" % (settings.MEDIA_URL, self.encoded)


class Lesson(CreatedMixin, Displayable):
    #TODO: this model should probably have a slug
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

    primary_ingredients = models.ManyToManyField(Ingredient, related_name='primary_lessons', blank=True)
    course = models.ManyToManyField('Course', blank=True)
    cuisine = models.ManyToManyField('Cuisine', blank=True)
    restrictions = models.ManyToManyField("DietaryRestrictions", blank=True)

    kind = models.SmallIntegerField(choices=((0, "Recipe"),
                                             (1, "Technique")), default=0)

    ingredients = models.ManyToManyField(Ingredient, through="LessonIngredient", related_name="lessons")
    tools = models.ManyToManyField(Tool, through="LessonTool", related_name="lessons", blank=True)
    video = models.ForeignKey(Video, related_name="lessons", null=True, blank=True)


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
        return int(max(self.prep_time.total_seconds() / 60, 1))

    @property
    def cook_in_min(self):
        return int(max(self.cooking_time.total_seconds() / 60, 1))


    def get_absolute_url(self):
        return reverse("lesson_detail", kwargs={'lesson_id':self.id})

    def __unicode__(self):
        return self.title


class Step(CreatedMixin):


    def get_ingredient_set(self):
        return self.lesson.ingredients.all().values('pk')

    def get_tools_set(self):
        return self.lesson.tools.all().values('pk')

    lesson = models.ForeignKey(Lesson, related_name='steps')
    title = models.CharField(max_length=128, blank=False, null=False)

    text = models.TextField()

    order = models.PositiveSmallIntegerField(default=0)
    technique = models.ForeignKey(Lesson, related_name="technique", null=True, blank=True)
    ingredients = models.ManyToManyField(LessonIngredient, related_name="steps", blank=True)
    tools = models.ManyToManyField(LessonTool, related_name="steps", blank=True)

    picture = models.ImageField(upload_to=file_url(""))



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

def SlugifyUniquely(value, model, slugfield="slug"):
    suffix = 0
    potential = base = slugify(value)
    while True:
        if suffix:
            potential = "-".join([base, str(suffix)])
        if not model.objects.filter(**{slugfield: potential}).count():
            return potential
        suffix += 1

class LessonRequest(CreatedMixin):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    time_in_min  = models.SmallIntegerField()
    time_in_min = models.SmallIntegerField(choices=(
            (0, "Quick (less than 30 min)"),
            (1, "Moderate (30-90 min)"),
            (2, "Slow (90 min or more)"),
            ), default=0)


    serving_size = models.SmallIntegerField()
    description = models.TextField()
    need_by = models.DateField()
    kind = models.SmallIntegerField(choices=((0, "Recipe"),
                                             (1, "Technique")), default=0)


    slug = models.SlugField()
    successfully_funded = models.NullBooleanField(default=None)
    course = models.ManyToManyField('Course', related_name="requests", blank=True)
    cuisine = models.ManyToManyField('Cuisine', related_name="requests", blank=True)
    restrictions = models.ManyToManyField("DietaryRestrictions", related_name="requests", blank=True)
    primary_ingredients = models.ManyToManyField(Ingredient, related_name="requests", blank=True)

    def to_dict(self):
        return {
            "title":self.title,
            "time_in_min":self.time_in_min,
            "serving_size":self.serving_size,
            "description":self.description,
            "need_by":timeuntil(self.need_by),
            "kind": self.kind,
            "slug":self.slug,
            "course": [str(course) for course in self.course.all()],
            "cuisine": [str(cuisine) for cuisine in self.cuisine.all()],
            "restrictions": [str(restrictions) for restrictions in self.restrictions.all()],
            "primary_ingredients": [str(primary_ingredients) for primary_ingredients in self.primary_ingredients.all()],
            "chef": self.chef_attatched.to_dict() if self.chef_attatched else None,
            "chef_profile_url": reverse('miniprofile', args=[self.chef_attatched.id]) if self.chef_attatched else "#",
            "inpot": int(self.in_pot),
            "percent":  self.percent,
            "pledges":[pledge.to_dict() for pledge in self.pledges.all()[:10]],
            }

    def save(self):
        if not self.id:
            # replace self.name with your prepopulate_from field
            self.slug = SlugifyUniquely(self.title, self.__class__)
        super(self.__class__, self).save()

    @property
    def percent(self):
        if self.chef_attatched:
            return (float(self.in_pot) / float(self.amount_needed))*100
        else:
            return 0

    @cached_property
    def chef_attatched(self):
        try:
            return self.chefs.filter(active=True)[0]

        except IndexError:
            return None

    @cached_property
    def in_pot(self):
        return self.pledges.all().aggregate(Sum('amount'))['amount__sum'] or 0

    @cached_property
    def amount_needed(self):
        return self.chef_attatched.amount_required or None


    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('need_by','id')

    def get_absolute_url(self):
        return reverse("ask")  + "?slug=" + self.slug

class LessonPledge(CreatedMixin):
    user = models.ForeignKey(User)
    amount = CurrencyField(max_digits=7, decimal_places=2)
    email = models.BooleanField(help_text="keep me informed via email")
    request = models.ForeignKey(LessonRequest, related_name="pledges")
    date_pledged =models.DateField(auto_now_add=True)

    successfully_billed = models.NullBooleanField(default=None)
    billed_at = models.DateTimeField(null=True)
    def to_dict(self):
        return {
            "user_id": self.user.id,
            "user_name": self.user.get_full_name(),
            "amount": int(self.amount),
            "date_pledged": datetime.strftime(self.date_pledged, "%m/%d/%y"),
            }

    class Meta:
        unique_together = (("user", "request"))

class ChefPledge(CreatedMixin):
    user = models.ForeignKey(User)
    amount_required = CurrencyField(max_digits=7, decimal_places=2)
    request = models.ForeignKey(LessonRequest, related_name="chefs")
    active = models.BooleanField(default=True)

    def full_name(self):
        return self.user.get_full_name()

    def to_dict(self):
        return {
            "user_id": self.user.id,
            "full_name": self.full_name(),
            "amount_required": int(self.amount_required),
            "active": self.active,
            }

    def __unicode__(self):
        return unicode(self.user)


    # class Meta:
    #     unique_together = (("user", "request", "active"###where active is true ))
    #     this is handled via a postgres unique partal index.

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

#class userSignupRequest(CreatedMixin):
    #email = EmailField(max_length=256)
    
    
    