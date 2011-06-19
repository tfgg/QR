# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Campaign'
        db.create_table('core_campaign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('donate_link', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True)),
        ))
        db.send_create_signal('core', ['Campaign'])

        # Adding model 'CampaignLink'
        db.create_table('core_campaignlink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Campaign'])),
        ))
        db.send_create_signal('core', ['CampaignLink'])


    def backwards(self, orm):
        
        # Deleting model 'Campaign'
        db.delete_table('core_campaign')

        # Deleting model 'CampaignLink'
        db.delete_table('core_campaignlink')


    models = {
        'core.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'donate_link': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        'core.campaignlink': {
            'Meta': {'object_name': 'CampaignLink'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Campaign']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
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
