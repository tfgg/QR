from django.contrib import admin

import models

#class NarrativeAdmin(admin.ModelAdmin):
#  prepopulated_fields = {'slug': ('title',),}


admin.site.register(models.Poll)
admin.site.register(models.Option)

admin.site.register(models.Campaign)
admin.site.register(models.CampaignLink)
