# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SampleModel'
        db.create_table('core_samplemodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['SampleModel'])


    def backwards(self, orm):
        
        # Deleting model 'SampleModel'
        db.delete_table('core_samplemodel')


    models = {
        'core.samplemodel': {
            'Meta': {'object_name': 'SampleModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']
