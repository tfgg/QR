# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'SampleModel'
        db.delete_table('core_samplemodel')

        # Adding model 'Option'
        db.create_table('core_option', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Poll'])),
            ('text', self.gf('django.db.models.fields.TextField')(default='placeholder option')),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['Option'])

        # Adding model 'Poll'
        db.create_table('core_poll', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')(default='placeholder question')),
        ))
        db.send_create_signal('core', ['Poll'])


    def backwards(self, orm):
        
        # Adding model 'SampleModel'
        db.create_table('core_samplemodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['SampleModel'])

        # Deleting model 'Option'
        db.delete_table('core_option')

        # Deleting model 'Poll'
        db.delete_table('core_poll')


    models = {
        'core.option': {
            'Meta': {'object_name': 'Option'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Poll']"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "'placeholder option'"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.poll': {
            'Meta': {'object_name': 'Poll'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'default': "'placeholder question'"})
        }
    }

    complete_apps = ['core']
