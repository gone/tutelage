# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipie'
        db.create_table('app_recipie', (
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
            ('tags', self.gf('django.db.models.fields.CharField')(default='', max_length=128)),
            ('keywords', self.gf('mezzanine.generic.fields.KeywordsField')(object_id_field='object_pk', to=orm['generic.AssignedKeyword'], frozen_by_south=True)),
        ))
        db.send_create_signal('app', ['Recipie'])

        # Adding field 'Lesson.flavor_text'
        db.add_column('app_lesson', 'flavor_text',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Removing M2M table for field tools on 'Lesson'
        db.delete_table('app_lesson_tools')

        # Removing M2M table for field ingredients on 'Lesson'
        db.delete_table('app_lesson_ingredients')

    def backwards(self, orm):
        # Deleting model 'Recipie'
        db.delete_table('app_recipie')

        # Deleting field 'Lesson.flavor_text'
        db.delete_column('app_lesson', 'flavor_text')

        # Adding M2M table for field tools on 'Lesson'
        db.create_table('app_lesson_tools', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['app.lesson'], null=False)),
            ('tool', models.ForeignKey(orm['app.tool'], null=False))
        ))
        db.create_unique('app_lesson_tools', ['lesson_id', 'tool_id'])

        # Adding M2M table for field ingredients on 'Lesson'
        db.create_table('app_lesson_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['app.lesson'], null=False)),
            ('ingredient', models.ForeignKey(orm['app.ingredient'], null=False))
        ))
        db.create_unique('app_lesson_ingredients', ['lesson_id', 'ingredient_id'])

    models = {
        'app.category': {
            'Meta': {'object_name': 'Category'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
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
        'app.home': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Home', '_ormbases': ['pages.Page']},
            'call_to_action': ('django.db.models.fields.TextField', [], {}),
            'hero': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        'app.homeblock': {
            'Meta': {'object_name': 'HomeBlock'},
            'body': ('django.db.models.fields.TextField', [], {}),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'app.lesson': {
            'Meta': {'unique_together': "(('teacher', 'title'),)", 'object_name': 'Lesson'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'flavor_text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lessons_taking'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': "orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'tags': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lessons_teaching'", 'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'users_who_rated': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'rated_lessons'", 'symmetrical': 'False', 'through': "orm['app.LessonRating']", 'to': "orm['auth.User']"}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
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
            'Meta': {'object_name': 'Profile'},
            'about': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'profiles'", 'symmetrical': 'False', 'to': "orm['app.Ingredient']"}),
            'phone': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'tools': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'profiles'", 'symmetrical': 'False', 'to': "orm['app.Tool']"}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'app.recipie': {
            'Meta': {'object_name': 'Recipie'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
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
            'tags': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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