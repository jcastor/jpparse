# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Method'
        db.create_table('jpparse_method', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('codesegment', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['jpparse.codesegments'], unique=True)),
        ))
        db.send_create_signal('jpparse', ['Method'])

        # Adding M2M table for field variables on 'Method'
        db.create_table('jpparse_method_variables', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('method', models.ForeignKey(orm['jpparse.method'], null=False)),
            ('variable', models.ForeignKey(orm['jpparse.variable'], null=False))
        ))
        db.create_unique('jpparse_method_variables', ['method_id', 'variable_id'])

        # Adding model 'Variable'
        db.create_table('jpparse_variable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('jpparse', ['Variable'])

        # Adding model 'Class'
        db.create_table('jpparse_class', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('jpparse', ['Class'])

        # Adding M2M table for field methods on 'Class'
        db.create_table('jpparse_class_methods', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['jpparse.class'], null=False)),
            ('method', models.ForeignKey(orm['jpparse.method'], null=False))
        ))
        db.create_unique('jpparse_class_methods', ['class_id', 'method_id'])

        # Adding M2M table for field globalvariables on 'Class'
        db.create_table('jpparse_class_globalvariables', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['jpparse.class'], null=False)),
            ('variable', models.ForeignKey(orm['jpparse.variable'], null=False))
        ))
        db.create_unique('jpparse_class_globalvariables', ['class_id', 'variable_id'])

        # Adding model 'codesegments'
        db.create_table('jpparse_codesegments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stack', self.gf('django.db.models.fields.IntegerField')()),
            ('local', self.gf('django.db.models.fields.IntegerField')()),
            ('args_size', self.gf('django.db.models.fields.IntegerField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('jpparse', ['codesegments'])


    def backwards(self, orm):
        # Deleting model 'Method'
        db.delete_table('jpparse_method')

        # Removing M2M table for field variables on 'Method'
        db.delete_table('jpparse_method_variables')

        # Deleting model 'Variable'
        db.delete_table('jpparse_variable')

        # Deleting model 'Class'
        db.delete_table('jpparse_class')

        # Removing M2M table for field methods on 'Class'
        db.delete_table('jpparse_class_methods')

        # Removing M2M table for field globalvariables on 'Class'
        db.delete_table('jpparse_class_globalvariables')

        # Deleting model 'codesegments'
        db.delete_table('jpparse_codesegments')


    models = {
        'jpparse.class': {
            'Meta': {'object_name': 'Class'},
            'globalvariables': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jpparse.Variable']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'methods': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jpparse.Method']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'jpparse.codesegments': {
            'Meta': {'object_name': 'codesegments'},
            'args_size': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'local': ('django.db.models.fields.IntegerField', [], {}),
            'stack': ('django.db.models.fields.IntegerField', [], {})
        },
        'jpparse.method': {
            'Meta': {'object_name': 'Method'},
            'codesegment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['jpparse.codesegments']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'variables': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jpparse.Variable']", 'symmetrical': 'False'})
        },
        'jpparse.variable': {
            'Meta': {'object_name': 'Variable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['jpparse']