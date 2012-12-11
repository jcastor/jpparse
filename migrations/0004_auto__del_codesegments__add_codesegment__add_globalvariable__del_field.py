# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'codesegments'
        db.delete_table('jpparse_codesegments')

        # Adding model 'CodeSegment'
        db.create_table('jpparse_codesegment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stack', self.gf('django.db.models.fields.IntegerField')()),
            ('local', self.gf('django.db.models.fields.IntegerField')()),
            ('args_size', self.gf('django.db.models.fields.IntegerField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jpparse.Method'])),
        ))
        db.send_create_signal('jpparse', ['CodeSegment'])

        # Adding model 'GlobalVariable'
        db.create_table('jpparse_globalvariable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('classowner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jpparse.Class'])),
        ))
        db.send_create_signal('jpparse', ['GlobalVariable'])

        # Deleting field 'Method.codesegment'
        db.delete_column('jpparse_method', 'codesegment_id')

        # Removing M2M table for field variables on 'Method'
        db.delete_table('jpparse_method_variables')

        # Adding field 'Variable.method'
        db.add_column('jpparse_variable', 'method',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['jpparse.Method']),
                      keep_default=False)

        # Removing M2M table for field globalvariables on 'Class'
        db.delete_table('jpparse_class_globalvariables')


    def backwards(self, orm):
        # Adding model 'codesegments'
        db.create_table('jpparse_codesegments', (
            ('stack', self.gf('django.db.models.fields.IntegerField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('args_size', self.gf('django.db.models.fields.IntegerField')()),
            ('local', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('jpparse', ['codesegments'])

        # Deleting model 'CodeSegment'
        db.delete_table('jpparse_codesegment')

        # Deleting model 'GlobalVariable'
        db.delete_table('jpparse_globalvariable')

        # Adding field 'Method.codesegment'
        db.add_column('jpparse_method', 'codesegment',
                      self.gf('django.db.models.fields.related.OneToOneField')(default='none', to=orm['jpparse.codesegments'], unique=True),
                      keep_default=False)

        # Adding M2M table for field variables on 'Method'
        db.create_table('jpparse_method_variables', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('method', models.ForeignKey(orm['jpparse.method'], null=False)),
            ('variable', models.ForeignKey(orm['jpparse.variable'], null=False))
        ))
        db.create_unique('jpparse_method_variables', ['method_id', 'variable_id'])

        # Deleting field 'Variable.method'
        db.delete_column('jpparse_variable', 'method_id')

        # Adding M2M table for field globalvariables on 'Class'
        db.create_table('jpparse_class_globalvariables', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['jpparse.class'], null=False)),
            ('variable', models.ForeignKey(orm['jpparse.variable'], null=False))
        ))
        db.create_unique('jpparse_class_globalvariables', ['class_id', 'variable_id'])


    models = {
        'jpparse.class': {
            'Meta': {'object_name': 'Class'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'methods': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jpparse.Method']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
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