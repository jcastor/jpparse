# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Class.name'
        db.alter_column('jpparse_class', 'name', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'Method.name'
        db.alter_column('jpparse_method', 'name', self.gf('django.db.models.fields.CharField')(max_length=5000))

    def backwards(self, orm):

        # Changing field 'Class.name'
        db.alter_column('jpparse_class', 'name', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'Method.name'
        db.alter_column('jpparse_method', 'name', self.gf('django.db.models.fields.CharField')(max_length=1000))

    models = {
        'jpparse.class': {
            'Meta': {'object_name': 'Class'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'methods': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['jpparse.Method']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '5000'})
        },
        'jpparse.codesegment': {
            'Meta': {'object_name': 'CodeSegment'},
            'args_size': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'local': ('django.db.models.fields.IntegerField', [], {}),
            'method': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jpparse.Method']"}),
            'stack': ('django.db.models.fields.IntegerField', [], {})
        },
        'jpparse.globalvariable': {
            'Meta': {'object_name': 'GlobalVariable'},
            'classowner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jpparse.Class']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'jpparse.method': {
            'Meta': {'object_name': 'Method'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'jpparse.variable': {
            'Meta': {'object_name': 'Variable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jpparse.Method']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['jpparse']