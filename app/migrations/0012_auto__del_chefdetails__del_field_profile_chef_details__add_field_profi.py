# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ChefDetails'
        db.delete_table('app_chefdetails')

        # Removing M2M table for field course on 'ChefDetails'
        db.delete_table('app_chefdetails_course')

        # Removing M2M table for field cuisine on 'ChefDetails'
        db.delete_table('app_chefdetails_cuisine')

        # Removing M2M table for field restrictions on 'ChefDetails'
        db.delete_table('app_chefdetails_restrictions')

        # Deleting field 'Profile.chef_details'
        db.delete_column('app_profile', 'chef_details_id')

        # Adding field 'Profile.location'
        db.add_column('app_profile', 'location',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Profile.website1'
        db.add_column('app_profile', 'website1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Profile.website1_url'
        db.add_column('app_profile', 'website1_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Profile.website2'
        db.add_column('app_profile', 'website2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Profile.website2_url'
        db.add_column('app_profile', 'website2_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Profile.facebook'
        db.add_column('app_profile', 'facebook',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Profile.Twitter'
        db.add_column('app_profile', 'Twitter',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Profile.LinkedIn'
        db.add_column('app_profile', 'LinkedIn',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Profile.Pinterest'
        db.add_column('app_profile', 'Pinterest',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Profile.YouTube'
        db.add_column('app_profile', 'YouTube',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Profile.Testimonial1_text'
        db.add_column('app_profile', 'Testimonial1_text',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Profile.Testimonial1_src'
        db.add_column('app_profile', 'Testimonial1_src',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Profile.Testimonial2_text'
        db.add_column('app_profile', 'Testimonial2_text',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Profile.Testimonial2_src'
        db.add_column('app_profile', 'Testimonial2_src',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Profile.Testimonial3_text'
        db.add_column('app_profile', 'Testimonial3_text',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Profile.Testimonial3_src'
        db.add_column('app_profile', 'Testimonial3_src',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding M2M table for field course on 'Profile'
        db.create_table('app_profile_course', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['app.profile'], null=False)),
            ('course', models.ForeignKey(orm['app.course'], null=False))
        ))
        db.create_unique('app_profile_course', ['profile_id', 'course_id'])

        # Adding M2M table for field cuisine on 'Profile'
        db.create_table('app_profile_cuisine', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['app.profile'], null=False)),
            ('cuisine', models.ForeignKey(orm['app.cuisine'], null=False))
        ))
        db.create_unique('app_profile_cuisine', ['profile_id', 'cuisine_id'])

        # Adding M2M table for field restrictions on 'Profile'
        db.create_table('app_profile_restrictions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['app.profile'], null=False)),
            ('dietaryrestrictions', models.ForeignKey(orm['app.dietaryrestrictions'], null=False))
        ))
        db.create_unique('app_profile_restrictions', ['profile_id', 'dietaryrestrictions_id'])

    def backwards(self, orm):
        # Adding model 'ChefDetails'
        db.create_table('app_chefdetails', (
            ('website1_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('Pinterest', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('YouTube', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('LinkedIn', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('website2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Testimonial1_src', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Testimonial3_src', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('website1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Testimonial3_text', self.gf('django.db.models.fields.TextField')()),
            ('Testimonial1_text', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Testimonial2_src', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('website2_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('Twitter', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('Testimonial2_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('app', ['ChefDetails'])

        # Adding M2M table for field course on 'ChefDetails'
        db.create_table('app_chefdetails_course', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chefdetails', models.ForeignKey(orm['app.chefdetails'], null=False)),
            ('course', models.ForeignKey(orm['app.course'], null=False))
        ))
        db.create_unique('app_chefdetails_course', ['chefdetails_id', 'course_id'])

        # Adding M2M table for field cuisine on 'ChefDetails'
        db.create_table('app_chefdetails_cuisine', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chefdetails', models.ForeignKey(orm['app.chefdetails'], null=False)),
            ('cuisine', models.ForeignKey(orm['app.cuisine'], null=False))
        ))
        db.create_unique('app_chefdetails_cuisine', ['chefdetails_id', 'cuisine_id'])

        # Adding M2M table for field restrictions on 'ChefDetails'
        db.create_table('app_chefdetails_restrictions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chefdetails', models.ForeignKey(orm['app.chefdetails'], null=False)),
            ('dietaryrestrictions', models.ForeignKey(orm['app.dietaryrestrictions'], null=False))
        ))
        db.create_unique('app_chefdetails_restrictions', ['chefdetails_id', 'dietaryrestrictions_id'])

        # Adding field 'Profile.chef_details'
        db.add_column('app_profile', 'chef_details',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.ChefDetails'], null=True),
                      keep_default=False)

        # Deleting field 'Profile.location'
        db.delete_column('app_profile', 'location')

        # Deleting field 'Profile.website1'
        db.delete_column('app_profile', 'website1')

        # Deleting field 'Profile.website1_url'
        db.delete_column('app_profile', 'website1_url')

        # Deleting field 'Profile.website2'
        db.delete_column('app_profile', 'website2')

        # Deleting field 'Profile.website2_url'
        db.delete_column('app_profile', 'website2_url')

        # Deleting field 'Profile.facebook'
        db.delete_column('app_profile', 'facebook')

        # Deleting field 'Profile.Twitter'
        db.delete_column('app_profile', 'Twitter')

        # Deleting field 'Profile.LinkedIn'
        db.delete_column('app_profile', 'LinkedIn')

        # Deleting field 'Profile.Pinterest'
        db.delete_column('app_profile', 'Pinterest')

        # Deleting field 'Profile.YouTube'
        db.delete_column('app_profile', 'YouTube')

        # Deleting field 'Profile.Testimonial1_text'
        db.delete_column('app_profile', 'Testimonial1_text')

        # Deleting field 'Profile.Testimonial1_src'
        db.delete_column('app_profile', 'Testimonial1_src')

        # Deleting field 'Profile.Testimonial2_text'
        db.delete_column('app_profile', 'Testimonial2_text')

        # Deleting field 'Profile.Testimonial2_src'
        db.delete_column('app_profile', 'Testimonial2_src')

        # Deleting field 'Profile.Testimonial3_text'
        db.delete_column('app_profile', 'Testimonial3_text')

        # Deleting field 'Profile.Testimonial3_src'
        db.delete_column('app_profile', 'Testimonial3_src')

        # Removing M2M table for field course on 'Profile'
        db.delete_table('app_profile_course')

        # Removing M2M table for field cuisine on 'Profile'
        db.delete_table('app_profile_cuisine')

        # Removing M2M table for field restrictions on 'Profile'
        db.delete_table('app_profile_restrictions')

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
        'app.course': {
            'Meta': {'object_name': 'Course'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.creditcard': {
            'Meta': {'object_name': 'CreditCard'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exp_month': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'exp_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_4': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'stripe_customer_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'app.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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
            'featured_lessons': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Lesson']", 'symmetrical': 'False'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_text': ('mezzanine.core.fields.RichTextField', [], {}),
            'intro_video': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.lesson': {
            'Meta': {'unique_together': "(('teacher', 'title'),)", 'object_name': 'Lesson'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'cooking_time': ('durationfield.db.models.fields.duration.DurationField', [], {}),
            'course': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Course']", 'symmetrical': 'False'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Cuisine']", 'symmetrical': 'False'}),
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
            'primary_ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'primary_lessons'", 'symmetrical': 'False', 'to': "orm['app.Ingredient']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'restrictions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.DietaryRestrictions']", 'symmetrical': 'False'}),
            'serving_size': ('django.db.models.fields.IntegerField', [], {}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teaching'", 'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lessons'", 'symmetrical': 'False', 'to': "orm['app.Tool']"}),
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
            'prep': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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
        'app.profile': {
            'LinkedIn': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'Meta': {'object_name': 'Profile'},
            'Pinterest': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'Testimonial1_src': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'Testimonial1_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Testimonial2_src': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'Testimonial2_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Testimonial3_src': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'Testimonial3_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'YouTube': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'about': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            'course': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Course']", 'symmetrical': 'False'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Cuisine']", 'symmetrical': 'False'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'profiles'", 'symmetrical': 'False', 'to': "orm['app.Ingredient']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'professional_chef': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'restrictions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.DietaryRestrictions']", 'symmetrical': 'False'}),
            'skill_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'profiles'", 'symmetrical': 'False', 'to': "orm['app.Tool']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'website1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'website1_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'website2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'website2_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'app.step': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('lesson', 'order'),)", 'object_name': 'Step'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'steps'", 'blank': 'True', 'to': "orm['app.LessonIngredient']"}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': "orm['app.Lesson']"}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'start_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
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