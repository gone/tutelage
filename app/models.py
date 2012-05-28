from django.db import models
from ecl_django.models import BcryptMixin, CreatedMixin


def file_url(name):
    def inner(instance, filename):
        r = re.compile(r'[^\S]')
        filename = r.sub('', filename)
        now = datetime.now()
        timestamp = int(time.time())
        return 'uploads/{0}/{1.year:04}/{1.month:02}/{1.day:02}/{2}/{3}'.format( \
                name, now, timestamp, filename)
    return inner


class Ingredient(CreatedMixin):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Tool(CreatedMixin):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class User(CreatedMixin, BcryptMixin()):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    skill = models.PositiveSmallIntegerField(choices=(
        (0, "Novice"),
        (1, "Intermediate"),
        (2, "Advanced"),
        (3, "Professional")))
    about = models.TextField(default="")

    cc_name = models.CharField(max_length=128)
    cc_type = models.CharField(max_length=32, null=True, blank=True)
    cc_exp_month = models.CharField(max_length=2, null=True, blank=True)
    cc_exp_year = models.CharField(max_length=4, null=True, blank=True)
    cc_last_4 = models.CharField(max_length=4, null=True, blank=True)
    cc_zip = models.CharField(max_length=5, null=True, blank=True)
    cc_address_1 = models.CharField(max_length=128, null=True, blank=True)
    cc_address_2 = models.CharField(max_length=128, null=True, blank=True)
    cc_state = models.CharField(max_length=2, null=True, blank=True)
    cc_country = models.CharField(max_length=32, null=True, blank=True)

    stripe_customer_id = models.CharField(max_length=32, null=True, blank=True)

    ingredients = models.ManyToManyField(Ingredient, related_name='users')
    tools = models.ManyToManyField(Tool, related_name='users')

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


class Lesson(CreatedMixin):
    user = models.ForeignKey(User, related_name='lessons_teaching')
    title = models.CharField(max_length=128)
    description = models.TextField(default="")
    tags = models.CharField(max_length=128, default="")
    video = models.FileField(upload_to=file_url("lessonvideos"))
    ingredients = models.ManyToManyField(Ingredient, related_name='lessons')
    tools = models.ManyToManyField(Tool, related_name='lessons')

    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    users_who_rated = models.ManyToManyField(User, through='LessonRating', related_name='rated_lessons')
    followers = models.ManyToManyField(User, related_name='lessons_taking')

    class Meta():
        unique_together = ('user', 'title')

    @property
    def rating(self):
        result = self.ratings.aggregate(avg=Avg('rating'))['avg']
        if not result:
            return 0
        return result

    def __unicode__(self):
        return self.name


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

