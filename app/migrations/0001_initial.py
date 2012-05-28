# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Ingredient'
        db.create_table('app_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('app', ['Ingredient'])

        # Adding model 'Tool'
        db.create_table('app_tool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('app', ['Tool'])

        # Adding model 'User'
        db.create_table('app_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('skill', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('about', self.gf('django.db.models.fields.TextField')(default='')),
            ('cc_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('cc_type', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('cc_exp_month', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('cc_exp_year', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('cc_last_4', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('cc_zip', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('cc_address_1', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('cc_address_2', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('cc_state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('cc_country', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('stripe_customer_id', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
        ))
        db.send_create_signal('app', ['User'])

        # Adding M2M table for field ingredients on 'User'
        db.create_table('app_user_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm['app.user'], null=False)),
            ('ingredient', models.ForeignKey(orm['app.ingredient'], null=False))
        ))
        db.create_unique('app_user_ingredients', ['user_id', 'ingredient_id'])

        # Adding M2M table for field tools on 'User'
        db.create_table('app_user_tools', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm['app.user'], null=False)),
            ('tool', models.ForeignKey(orm['app.tool'], null=False))
        ))
        db.create_unique('app_user_tools', ['user_id', 'tool_id'])

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

        # Adding model 'Lesson'
        db.create_table('app_lesson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lessons_teaching', to=orm['app.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('tags', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('app', ['Lesson'])

        # Adding unique constraint on 'Lesson', fields ['user', 'title']
        db.create_unique('app_lesson', ['user_id', 'title'])

        # Adding M2M table for field ingredients on 'Lesson'
        db.create_table('app_lesson_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['app.lesson'], null=False)),
            ('ingredient', models.ForeignKey(orm['app.ingredient'], null=False))
        ))
        db.create_unique('app_lesson_ingredients', ['lesson_id', 'ingredient_id'])

        # Adding M2M table for field tools on 'Lesson'
        db.create_table('app_lesson_tools', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['app.lesson'], null=False)),
            ('tool', models.ForeignKey(orm['app.tool'], null=False))
        ))
        db.create_unique('app_lesson_tools', ['lesson_id', 'tool_id'])

        # Adding M2M table for field followers on 'Lesson'
        db.create_table('app_lesson_followers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['app.lesson'], null=False)),
            ('user', models.ForeignKey(orm['app.user'], null=False))
        ))
        db.create_unique('app_lesson_followers', ['lesson_id', 'user_id'])

        # Adding model 'Step'
        db.create_table('app_step', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='steps', to=orm['app.Lesson'])),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('start_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('app', ['Step'])

        # Adding unique constraint on 'Step', fields ['lesson', 'order']
        db.create_unique('app_step', ['lesson_id', 'order'])

        # Adding model 'LessonRating'
        db.create_table('app_lessonrating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratings', to=orm['app.User'])),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratings', to=orm['app.Lesson'])),
            ('rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('app', ['LessonRating'])

        # Adding unique constraint on 'LessonRating', fields ['user', 'lesson']
        db.create_unique('app_lessonrating', ['user_id', 'lesson_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'LessonRating', fields ['user', 'lesson']
        db.delete_unique('app_lessonrating', ['user_id', 'lesson_id'])

        # Removing unique constraint on 'Step', fields ['lesson', 'order']
        db.delete_unique('app_step', ['lesson_id', 'order'])

        # Removing unique constraint on 'Lesson', fields ['user', 'title']
        db.delete_unique('app_lesson', ['user_id', 'title'])

        # Removing unique constraint on 'SubCategory', fields ['name', 'parent']
        db.delete_unique('app_subcategory', ['name', 'parent_id'])

        # Deleting model 'Ingredient'
        db.delete_table('app_ingredient')

        # Deleting model 'Tool'
        db.delete_table('app_tool')

        # Deleting model 'User'
        db.delete_table('app_user')

        # Removing M2M table for field ingredients on 'User'
        db.delete_table('app_user_ingredients')

        # Removing M2M table for field tools on 'User'
        db.delete_table('app_user_tools')

        # Deleting model 'Category'
        db.delete_table('app_category')

        # Deleting model 'SubCategory'
        db.delete_table('app_subcategory')

        # Deleting model 'Lesson'
        db.delete_table('app_lesson')

        # Removing M2M table for field ingredients on 'Lesson'
        db.delete_table('app_lesson_ingredients')

        # Removing M2M table for field tools on 'Lesson'
        db.delete_table('app_lesson_tools')

        # Removing M2M table for field followers on 'Lesson'
        db.delete_table('app_lesson_followers')

        # Deleting model 'Step'
        db.delete_table('app_step')

        # Deleting model 'LessonRating'
        db.delete_table('app_lessonrating')


    models = {
        'app.category': {
            'Meta': {'object_name': 'Category'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.lesson': {
            'Meta': {'unique_together': "(('user', 'title'),)", 'object_name': 'Lesson'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lessons_taking'", 'symmetrical': 'False', 'to': "orm['app.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lessons'", 'symmetrical': 'False', 'to': "orm['app.Ingredient']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lessons'", 'symmetrical': 'False', 'to': "orm['app.Tool']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lessons_teaching'", 'to': "orm['app.User']"}),
            'users_who_rated': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'rated_lessons'", 'symmetrical': 'False', 'through': "orm['app.LessonRating']", 'to': "orm['app.User']"}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'app.lessonrating': {
            'Meta': {'unique_together': "(('user', 'lesson'),)", 'object_name': 'LessonRating'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings'", 'to': "orm['app.Lesson']"}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings'", 'to': "orm['app.User']"})
        },
        'app.step': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('lesson', 'order'),)", 'object_name': 'Step'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': "orm['app.Lesson']"}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'start_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.user': {
            'Meta': {'object_name': 'User'},
            'about': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'cc_address_1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'cc_address_2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'cc_country': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'cc_exp_month': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'cc_exp_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'cc_last_4': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'cc_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'cc_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'cc_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'cc_zip': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users'", 'symmetrical': 'False', 'to': "orm['app.Ingredient']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'skill': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'stripe_customer_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users'", 'symmetrical': 'False', 'to': "orm['app.Tool']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['app']
