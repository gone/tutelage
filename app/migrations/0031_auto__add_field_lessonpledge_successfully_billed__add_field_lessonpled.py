# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LessonPledge.successfully_billed'
        db.add_column('app_lessonpledge', 'successfully_billed',
                      self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'LessonPledge.billed_at'
        db.add_column('app_lessonpledge', 'billed_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'LessonRequest.successfully_funded'
        db.add_column('app_lessonrequest', 'successfully_funded',
                      self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'LessonPledge.successfully_billed'
        db.delete_column('app_lessonpledge', 'successfully_billed')

        # Deleting field 'LessonPledge.billed_at'
        db.delete_column('app_lessonpledge', 'billed_at')

        # Deleting field 'LessonRequest.successfully_funded'
        db.delete_column('app_lessonrequest', 'successfully_funded')

    models = {
        'app.about': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'About', '_ormbases': ['pages.Page']},
            'blockone': ('mezzanine.core.fields.RichTextField', [], {}),
            'blockthree': ('mezzanine.core.fields.RichTextField', [], {}),
            'blocktwo': ('mezzanine.core.fields.RichTextField', [], {}),
            'hero': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        'app.category': {
            'Meta': {'object_name': 'Category'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.chefpledge': {
            'Meta': {'object_name': 'ChefPledge'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amount_required': ('app.models.CurrencyField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chefs'", 'to': "orm['app.LessonRequest']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'app.course': {
            'Meta': {'object_name': 'Course'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.customer': {
            'Meta': {'object_name': 'Customer'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'app.dietaryrestrictions': {
            'Meta': {'object_name': 'DietaryRestrictions'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restriction': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.featuredchef': {
            'Meta': {'object_name': 'FeaturedChef'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'chef': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'featured_chef'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': "orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'app.home': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Home', '_ormbases': ['pages.Page']},
            'call_to_action': ('mezzanine.core.fields.RichTextField', [], {}),
            'hero': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        'app.homeblock': {
            'Meta': {'object_name': 'HomeBlock'},
            'body': ('mezzanine.core.fields.RichTextField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '126'}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blocks'", 'to': "orm['app.Home']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_copy': ('django.db.models.fields.CharField', [], {'max_length': '126'}),
            'link_target': ('django.db.models.fields.CharField', [], {'max_length': '126'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'product_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'substitution1': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'substitution2': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.lesson': {
            'Meta': {'unique_together': "(('teacher', 'title'),)", 'object_name': 'Lesson'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'cooking_time': ('durationfield.db.models.fields.duration.DurationField', [], {}),
            'course': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Course']", 'symmetrical': 'False', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Cuisine']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'flavor_text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'lessons'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lessons'", 'symmetrical': 'False', 'through': "orm['app.LessonIngredient']", 'to': "orm['app.Ingredient']"}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': "orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'kind': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'prep_time': ('durationfield.db.models.fields.duration.DurationField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'primary_ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'primary_lessons'", 'blank': 'True', 'to': "orm['app.Ingredient']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'restrictions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.DietaryRestrictions']", 'symmetrical': 'False', 'blank': 'True'}),
            'serving_size': ('django.db.models.fields.IntegerField', [], {}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teaching'", 'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'lessons'", 'blank': 'True', 'to': "orm['app.Tool']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'users_who_rated': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'rated_lessons'", 'symmetrical': 'False', 'through': "orm['app.LessonRating']", 'to': "orm['auth.User']"})
        },
        'app.lessoningredient': {
            'Meta': {'object_name': 'LessonIngredient'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Ingredient']"}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Lesson']"}),
            'measurement': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'prep': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.lessonpledge': {
            'Meta': {'unique_together': "(('user', 'request'),)", 'object_name': 'LessonPledge'},
            'amount': ('app.models.CurrencyField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'billed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_pledged': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pledges'", 'to': "orm['app.LessonRequest']"}),
            'successfully_billed': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'app.lessonrating': {
            'Meta': {'unique_together': "(('user', 'lesson'),)", 'object_name': 'LessonRating'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings'", 'to': "orm['app.Lesson']"}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings'", 'to': "orm['auth.User']"})
        },
        'app.lessonrequest': {
            'Meta': {'ordering': "('need_by', 'id')", 'object_name': 'LessonRequest'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'course': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'requests'", 'blank': 'True', 'to': "orm['app.Course']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'requests'", 'blank': 'True', 'to': "orm['app.Cuisine']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'need_by': ('django.db.models.fields.DateField', [], {}),
            'primary_ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'requests'", 'blank': 'True', 'to': "orm['app.Ingredient']"}),
            'restrictions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'requests'", 'blank': 'True', 'to': "orm['app.DietaryRestrictions']"}),
            'serving_size': ('django.db.models.fields.SmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'successfully_funded': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'time_in_min': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.profile': {
            'Meta': {'object_name': 'Profile'},
            'about': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Course']", 'symmetrical': 'False', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Cuisine']", 'symmetrical': 'False', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'googleplus': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'profiles'", 'blank': 'True', 'to': "orm['app.Ingredient']"}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'personal_video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'personal_video_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pinterest': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'professional_chef': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'restrictions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.DietaryRestrictions']", 'symmetrical': 'False', 'blank': 'True'}),
            'skill_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'testimonial1_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'testimonial1_src': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'testimonial1_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'testimonial2_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'testimonial2_src': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'testimonial2_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'testimonial3_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'testimonial3_src': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'testimonial3_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'profiles'", 'blank': 'True', 'to': "orm['app.Tool']"}),
            'tumblr': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'website1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'website1_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'website2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'website2_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'app.step': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('lesson', 'order'),)", 'object_name': 'Step'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'steps'", 'blank': 'True', 'to': "orm['app.LessonIngredient']"}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': "orm['app.Lesson']"}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'technique': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'technique_steps'", 'blank': 'True', 'to': "orm['app.Lesson']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'steps'", 'blank': 'True', 'to': "orm['app.Tool']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.subcategory': {
            'Meta': {'unique_together': "(('name', 'parent'),)", 'object_name': 'SubCategory'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subcategories'", 'to': "orm['app.Category']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.tool': {
            'Meta': {'object_name': 'Tool'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'product_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True'}),
            'substitution1': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'substitution2': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.video': {
            'Meta': {'object_name': 'Video'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['app.Lesson']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'generic.assignedkeyword': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'AssignedKeyword'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': "orm['generic.Keyword']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {})
        },
        'generic.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'pages.page': {
            'Meta': {'ordering': "('titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '[1, 2, 3]', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': "orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['app']