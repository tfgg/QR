# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Poll.type'
        db.add_column('core_poll', 'type', self.gf('django.db.models.fields.TextField')(default='sms'), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Poll.type'
        db.delete_column('core_poll', 'type')


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
            'question': ('django.db.models.fields.TextField', [], {'default': "'placeholder question'"}),
            'type': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['core']
