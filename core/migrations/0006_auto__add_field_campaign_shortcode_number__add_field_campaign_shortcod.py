# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Campaign.shortcode_number'
        db.add_column('core_campaign', 'shortcode_number', self.gf('django.db.models.fields.CharField')(max_length=256, null=True), keep_default=False)

        # Adding field 'Campaign.shortcode_content'
        db.add_column('core_campaign', 'shortcode_content', self.gf('django.db.models.fields.CharField')(max_length=256, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Campaign.shortcode_number'
        db.delete_column('core_campaign', 'shortcode_number')

        # Deleting field 'Campaign.shortcode_content'
        db.delete_column('core_campaign', 'shortcode_content')


    models = {
        'core.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'donate_link': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'short_link': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'shortcode_content': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'shortcode_number': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
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
