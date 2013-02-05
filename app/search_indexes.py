from haystack.indexes import *
from haystack import site

import app.models as models


#class FeaturedChefIndex(indexes.SearchIndex, Indexes.Indexable):

class LessonIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    teacher = CharField(model_attr="teacher")
    flavor_text = CharField(model_attr="flavor_text")
    title = CharField(model_attr="title")
    description = CharField(model_attr="description")


    def index_queryset(self):
        """used when the entire index for the model is updated"""
        return models.Lesson.objects.filter(status=2)

site.register(models.Lesson, LessonIndex)
