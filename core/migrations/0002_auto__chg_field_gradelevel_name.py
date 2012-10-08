# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GradeLevel.name'
        db.alter_column('core_gradelevel', 'name', self.gf('django.db.models.fields.CharField')(max_length=6))

    def backwards(self, orm):

        # Changing field 'GradeLevel.name'
        db.alter_column('core_gradelevel', 'name', self.gf('django.db.models.fields.CharField')(max_length=4))

    models = {
        'core.component': {
            'Meta': {'object_name': 'Component', '_ormbases': ['core.LearningStandardItem']},
            'learningstandarditem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.LearningStandardItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.gradelevel': {
            'Meta': {'object_name': 'GradeLevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '6'})
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