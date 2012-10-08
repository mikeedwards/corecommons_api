# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table('core_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('core', ['Language'])

        # Adding model 'GradeLevel'
        db.create_table('core_gradelevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('core', ['GradeLevel'])

        # Adding model 'LearningStandardItem'
        db.create_table('core_learningstandarditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Language'])),
            ('ref_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('document_ref_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent_ref_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.LearningStandardItem'], null=True, blank=True)),
            ('ref_URI', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('statement', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['LearningStandardItem'])

        # Adding M2M table for field grade_levels on 'LearningStandardItem'
        db.create_table('core_learningstandarditem_grade_levels', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('learningstandarditem', models.ForeignKey(orm['core.learningstandarditem'], null=False)),
            ('gradelevel', models.ForeignKey(orm['core.gradelevel'], null=False))
        ))
        db.create_unique('core_learningstandarditem_grade_levels', ['learningstandarditem_id', 'gradelevel_id'])

        # Adding model 'Standard'
        db.create_table('core_standard', (
            ('learningstandarditem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.LearningStandardItem'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('core', ['Standard'])

        # Adding model 'Component'
        db.create_table('core_component', (
            ('learningstandarditem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.LearningStandardItem'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('core', ['Component'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table('core_language')

        # Deleting model 'GradeLevel'
        db.delete_table('core_gradelevel')

        # Deleting model 'LearningStandardItem'
        db.delete_table('core_learningstandarditem')

        # Removing M2M table for field grade_levels on 'LearningStandardItem'
        db.delete_table('core_learningstandarditem_grade_levels')

        # Deleting model 'Standard'
        db.delete_table('core_standard')

        # Deleting model 'Component'
        db.delete_table('core_component')


    models = {
        'core.component': {
            'Meta': {'object_name': 'Component', '_ormbases': ['core.LearningStandardItem']},
            'learningstandarditem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.LearningStandardItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.gradelevel': {
            'Meta': {'object_name': 'GradeLevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'core.language': {
            'Meta': {'object_name': 'Language'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'core.learningstandarditem': {
            'Meta': {'object_name': 'LearningStandardItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'document_ref_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'grade_levels': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.GradeLevel']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Language']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.LearningStandardItem']", 'null': 'True', 'blank': 'True'}),
            'parent_ref_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ref_URI': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'statement': ('django.db.models.fields.TextField', [], {})
        },
        'core.standard': {
            'Meta': {'object_name': 'Standard', '_ormbases': ['core.LearningStandardItem']},
            'learningstandarditem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.LearningStandardItem']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core']