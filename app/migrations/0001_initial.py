# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Home'
        db.create_table('app_home', (
            ('page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('call_to_action', self.gf('mezzanine.core.fields.RichTextField')()),
            ('hero', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('app', ['Home'])

        # Adding model 'HomeBlock'
        db.create_table('app_homeblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('home', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blocks', to=orm['app.Home'])),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=126)),
            ('body', self.gf('mezzanine.core.fields.RichTextField')()),
            ('link_copy', self.gf('django.db.models.fields.CharField')(max_length=126)),
            ('link_target', self.gf('django.db.models.fields.CharField')(max_length=126)),
        ))
        db.send_create_signal('app', ['HomeBlock'])

        # Adding model 'About'
        db.create_table('app_about', (
            ('page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('blockone', self.gf('mezzanine.core.fields.RichTextField')()),
            ('blocktwo', self.gf('mezzanine.core.fields.RichTextField')()),
            ('blockthree', self.gf('mezzanine.core.fields.RichTextField')()),
            ('hero', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('app', ['About'])

        # Adding model 'FeaturedChef'
        db.create_table('app_featuredchef', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('chef', self.gf('django.db.models.fields.related.OneToOneField')(related_name='featured_chef', unique=True, to=orm['auth.User'])),
            ('keywords', self.gf('mezzanine.generic.fields.KeywordsField')(object_id_field='object_pk', to=orm['generic.AssignedKeyword'], frozen_by_south=True)),
        ))
        db.send_create_signal('app', ['FeaturedChef'])

        # Adding model 'Ingredient'
        db.create_table('app_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('substitution1', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('substitution2', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('product_link', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('app', ['Ingredient'])

        # Adding model 'LessonIngredient'
        db.create_table('app_lessoningredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Ingredient'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Lesson'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(default='0')),
            ('measurement', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('prep', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
        ))
        db.send_create_signal('app', ['LessonIngredient'])

        # Adding model 'Tool'
        db.create_table('app_tool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('size', self.gf('django.db.models.fields.CharField')(default='', max_length=32, null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='', max_length=32, null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('substitution1', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('substitution2', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('product_link', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('app', ['Tool'])

        # Adding model 'LessonTool'
        db.create_table('app_lessontool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('tool', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Tool'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Lesson'])),
        ))
        db.send_create_signal('app', ['LessonTool'])

        # Adding model 'Category'
        db.create_table('app_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('app', ['Category'])

        # Adding model 'SubCategory'
        db.create_table('app_subcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subcategories', to=orm['app.Category'])),
        ))
        db.send_create_signal('app', ['SubCategory'])

        # Adding unique constraint on 'SubCategory', fields ['name', 'parent']
        db.create_unique('app_subcategory', ['name', 'parent_id'])

        # Adding model 'Profile'
        db.create_table('app_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('about', self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True)),
            ('professional_chef', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('website1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('website1_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('website2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('website2_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pinterest', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('youtube', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('googleplus', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('tumblr', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('testimonial1_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('testimonial1_src', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('testimonial1_link', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('testimonial2_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('testimonial2_src', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('testimonial2_link', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('testimonial3_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('testimonial3_src', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('testimonial3_link', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('personal_video', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('personal_video_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='profiles', null=True, to=orm['app.Video'])),
        ))
        db.send_create_signal('app', ['Profile'])

        # Adding M2M table for field ingredients on 'Profile'
        db.create_table('app_profile_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['app.profile'], null=False)),
            ('ingredient', models.ForeignKey(orm['app.ingredient'], null=False))
        ))
        db.create_unique('app_profile_ingredients', ['profile_id', 'ingredient_id'])

        # Adding M2M table for field tools on 'Profile'
        db.create_table('app_profile_tools', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['app.profile'], null=False)),
            ('tool', models.ForeignKey(orm['app.tool'], null=False))
        ))
        db.create_unique('app_profile_tools', ['profile_id', 'tool_id'])

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

        # Adding model 'Customer'
        db.create_table('app_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('customer_id', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('app', ['Customer'])

        # Adding model 'Video'
        db.create_table('app_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('app', ['Video'])

        # Adding model 'TranscodedVideo'
        db.create_table('app_transcodedvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(related_name='codecs', to=orm['app.Video'])),
            ('encoded', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('app', ['TranscodedVideo'])

        # Adding model 'Lesson'
        db.create_table('app_lesson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teaching', to=orm['auth.User'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('flavor_text', self.gf('django.db.models.fields.TextField')(default='')),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('serving_size', self.gf('django.db.models.fields.IntegerField')()),
            ('prep_time', self.gf('durationfield.db.models.fields.duration.DurationField')()),
            ('cooking_time', self.gf('durationfield.db.models.fields.duration.DurationField')()),
            ('kind', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='lessons', null=True, to=orm['app.Video'])),
            ('keywords', self.gf('mezzanine.generic.fields.KeywordsField')(object_id_field='object_pk', to=orm['generic.AssignedKeyword'], frozen_by_south=True)),
        ))
        db.send_create_signal('app', ['Lesson'])

        # Adding unique constraint on 'Lesson', fields ['teacher', 'title']
        db.create_unique('app_lesson', ['teacher_id', 'title'])

        # Adding M2M table for field followers on 'Lesson'
        db.create_table('app_lesson_followers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['app.lesson'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('app_lesson_followers', ['lesson_id', 'user_id'])

        # Adding M2M table for field primary_ingredients on 'Lesson'
        db.create_table('app_lesson_primary_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['app.lesson'], null=False)),
            ('ingredient', models.ForeignKey(orm['app.ingredient'], null=False))
        ))
        db.create_unique('app_lesson_primary_ingredients', ['lesson_id', 'ingredient_id'])

        # Adding M2M table for field course on 'Lesson'
        db.create_table('app_lesson_course', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['app.lesson'], null=False)),
            ('course', models.ForeignKey(orm['app.course'], null=False))
        ))
        db.create_unique('app_lesson_course', ['lesson_id', 'course_id'])

        # Adding M2M table for field cuisine on 'Lesson'
        db.create_table('app_lesson_cuisine', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['app.lesson'], null=False)),
            ('cuisine', models.ForeignKey(orm['app.cuisine'], null=False))
        ))
        db.create_unique('app_lesson_cuisine', ['lesson_id', 'cuisine_id'])

        # Adding M2M table for field restrictions on 'Lesson'
        db.create_table('app_lesson_restrictions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['app.lesson'], null=False)),
            ('dietaryrestrictions', models.ForeignKey(orm['app.dietaryrestrictions'], null=False))
        ))
        db.create_unique('app_lesson_restrictions', ['lesson_id', 'dietaryrestrictions_id'])

        # Adding model 'Step'
        db.create_table('app_step', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='steps', to=orm['app.Lesson'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('technique', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='technique', null=True, to=orm['app.Lesson'])),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('app', ['Step'])

        # Adding unique constraint on 'Step', fields ['lesson', 'order']
        db.create_unique('app_step', ['lesson_id', 'order'])

        # Adding M2M table for field ingredients on 'Step'
        db.create_table('app_step_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('step', models.ForeignKey(orm['app.step'], null=False)),
            ('lessoningredient', models.ForeignKey(orm['app.lessoningredient'], null=False))
        ))
        db.create_unique('app_step_ingredients', ['step_id', 'lessoningredient_id'])

        # Adding M2M table for field tools on 'Step'
        db.create_table('app_step_tools', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('step', models.ForeignKey(orm['app.step'], null=False)),
            ('lessontool', models.ForeignKey(orm['app.lessontool'], null=False))
        ))
        db.create_unique('app_step_tools', ['step_id', 'lessontool_id'])

        # Adding model 'LessonRating'
        db.create_table('app_lessonrating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratings', to=orm['auth.User'])),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratings', to=orm['app.Lesson'])),
            ('rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('app', ['LessonRating'])

        # Adding unique constraint on 'LessonRating', fields ['user', 'lesson']
        db.create_unique('app_lessonrating', ['user_id', 'lesson_id'])

        # Adding model 'LessonRequest'
        db.create_table('app_lessonrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('time_in_min', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('serving_size', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('need_by', self.gf('django.db.models.fields.DateField')()),
            ('kind', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('successfully_funded', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal('app', ['LessonRequest'])

        # Adding M2M table for field course on 'LessonRequest'
        db.create_table('app_lessonrequest_course', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lessonrequest', models.ForeignKey(orm['app.lessonrequest'], null=False)),
            ('course', models.ForeignKey(orm['app.course'], null=False))
        ))
        db.create_unique('app_lessonrequest_course', ['lessonrequest_id', 'course_id'])

        # Adding M2M table for field cuisine on 'LessonRequest'
        db.create_table('app_lessonrequest_cuisine', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lessonrequest', models.ForeignKey(orm['app.lessonrequest'], null=False)),
            ('cuisine', models.ForeignKey(orm['app.cuisine'], null=False))
        ))
        db.create_unique('app_lessonrequest_cuisine', ['lessonrequest_id', 'cuisine_id'])

        # Adding M2M table for field restrictions on 'LessonRequest'
        db.create_table('app_lessonrequest_restrictions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lessonrequest', models.ForeignKey(orm['app.lessonrequest'], null=False)),
            ('dietaryrestrictions', models.ForeignKey(orm['app.dietaryrestrictions'], null=False))
        ))
        db.create_unique('app_lessonrequest_restrictions', ['lessonrequest_id', 'dietaryrestrictions_id'])

        # Adding M2M table for field primary_ingredients on 'LessonRequest'
        db.create_table('app_lessonrequest_primary_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lessonrequest', models.ForeignKey(orm['app.lessonrequest'], null=False)),
            ('ingredient', models.ForeignKey(orm['app.ingredient'], null=False))
        ))
        db.create_unique('app_lessonrequest_primary_ingredients', ['lessonrequest_id', 'ingredient_id'])

        # Adding model 'LessonPledge'
        db.create_table('app_lessonpledge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('amount', self.gf('app.models.CurrencyField')(max_digits=7, decimal_places=2)),
            ('email', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('request', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pledges', to=orm['app.LessonRequest'])),
            ('date_pledged', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('successfully_billed', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('billed_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('app', ['LessonPledge'])

        # Adding unique constraint on 'LessonPledge', fields ['user', 'request']
        db.create_unique('app_lessonpledge', ['user_id', 'request_id'])

        # Adding model 'ChefPledge'
        db.create_table('app_chefpledge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('amount_required', self.gf('app.models.CurrencyField')(max_digits=7, decimal_places=2)),
            ('request', self.gf('django.db.models.fields.related.ForeignKey')(related_name='chefs', to=orm['app.LessonRequest'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('app', ['ChefPledge'])

        # Adding model 'Course'
        db.create_table('app_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('app', ['Course'])

        # Adding model 'Cuisine'
        db.create_table('app_cuisine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('cuisine', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('app', ['Cuisine'])

        # Adding model 'DietaryRestrictions'
        db.create_table('app_dietaryrestrictions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('restriction', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('app', ['DietaryRestrictions'])

    def backwards(self, orm):
        # Removing unique constraint on 'LessonPledge', fields ['user', 'request']
        db.delete_unique('app_lessonpledge', ['user_id', 'request_id'])

        # Removing unique constraint on 'LessonRating', fields ['user', 'lesson']
        db.delete_unique('app_lessonrating', ['user_id', 'lesson_id'])

        # Removing unique constraint on 'Step', fields ['lesson', 'order']
        db.delete_unique('app_step', ['lesson_id', 'order'])

        # Removing unique constraint on 'Lesson', fields ['teacher', 'title']
        db.delete_unique('app_lesson', ['teacher_id', 'title'])

        # Removing unique constraint on 'SubCategory', fields ['name', 'parent']
        db.delete_unique('app_subcategory', ['name', 'parent_id'])

        # Deleting model 'Home'
        db.delete_table('app_home')

        # Deleting model 'HomeBlock'
        db.delete_table('app_homeblock')

        # Deleting model 'About'
        db.delete_table('app_about')

        # Deleting model 'FeaturedChef'
        db.delete_table('app_featuredchef')

        # Deleting model 'Ingredient'
        db.delete_table('app_ingredient')

        # Deleting model 'LessonIngredient'
        db.delete_table('app_lessoningredient')

        # Deleting model 'Tool'
        db.delete_table('app_tool')

        # Deleting model 'LessonTool'
        db.delete_table('app_lessontool')

        # Deleting model 'Category'
        db.delete_table('app_category')

        # Deleting model 'SubCategory'
        db.delete_table('app_subcategory')

        # Deleting model 'Profile'
        db.delete_table('app_profile')

        # Removing M2M table for field ingredients on 'Profile'
        db.delete_table('app_profile_ingredients')

        # Removing M2M table for field tools on 'Profile'
        db.delete_table('app_profile_tools')

        # Removing M2M table for field course on 'Profile'
        db.delete_table('app_profile_course')

        # Removing M2M table for field cuisine on 'Profile'
        db.delete_table('app_profile_cuisine')

        # Removing M2M table for field restrictions on 'Profile'
        db.delete_table('app_profile_restrictions')

        # Deleting model 'Customer'
        db.delete_table('app_customer')

        # Deleting model 'Video'
        db.delete_table('app_video')

        # Deleting model 'TranscodedVideo'
        db.delete_table('app_transcodedvideo')

        # Deleting model 'Lesson'
        db.delete_table('app_lesson')

        # Removing M2M table for field followers on 'Lesson'
        db.delete_table('app_lesson_followers')

        # Removing M2M table for field primary_ingredients on 'Lesson'
        db.delete_table('app_lesson_primary_ingredients')

        # Removing M2M table for field course on 'Lesson'
        db.delete_table('app_lesson_course')

        # Removing M2M table for field cuisine on 'Lesson'
        db.delete_table('app_lesson_cuisine')

        # Removing M2M table for field restrictions on 'Lesson'
        db.delete_table('app_lesson_restrictions')

        # Deleting model 'Step'
        db.delete_table('app_step')

        # Removing M2M table for field ingredients on 'Step'
        db.delete_table('app_step_ingredients')

        # Removing M2M table for field tools on 'Step'
        db.delete_table('app_step_tools')

        # Deleting model 'LessonRating'
        db.delete_table('app_lessonrating')

        # Deleting model 'LessonRequest'
        db.delete_table('app_lessonrequest')

        # Removing M2M table for field course on 'LessonRequest'
        db.delete_table('app_lessonrequest_course')

        # Removing M2M table for field cuisine on 'LessonRequest'
        db.delete_table('app_lessonrequest_cuisine')

        # Removing M2M table for field restrictions on 'LessonRequest'
        db.delete_table('app_lessonrequest_restrictions')

        # Removing M2M table for field primary_ingredients on 'LessonRequest'
        db.delete_table('app_lessonrequest_primary_ingredients')

        # Deleting model 'LessonPledge'
        db.delete_table('app_lessonpledge')

        # Deleting model 'ChefPledge'
        db.delete_table('app_chefpledge')

        # Deleting model 'Course'
        db.delete_table('app_course')

        # Deleting model 'Cuisine'
        db.delete_table('app_cuisine')

        # Deleting model 'DietaryRestrictions'
        db.delete_table('app_dietaryrestrictions')

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
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'lessons'", 'blank': 'True', 'through': "orm['app.LessonTool']", 'to': "orm['app.Tool']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'users_who_rated': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'rated_lessons'", 'symmetrical': 'False', 'through': "orm['app.LessonRating']", 'to': "orm['auth.User']"}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'lessons'", 'null': 'True', 'to': "orm['app.Video']"})
        },
        'app.lessoningredient': {
            'Meta': {'object_name': 'LessonIngredient'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Ingredient']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Lesson']"}),
            'measurement': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
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
        'app.lessontool': {
            'Meta': {'object_name': 'LessonTool'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Lesson']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'tool': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Tool']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
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
            'video': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'profiles'", 'null': 'True', 'to': "orm['app.Video']"}),
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
            'technique': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'technique'", 'null': 'True', 'to': "orm['app.Lesson']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'steps'", 'blank': 'True', 'to': "orm['app.LessonTool']"}),
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
        'app.transcodedvideo': {
            'Meta': {'object_name': 'TranscodedVideo'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'encoded': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'codecs'", 'to': "orm['app.Video']"})
        },
        'app.video': {
            'Meta': {'object_name': 'Video'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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