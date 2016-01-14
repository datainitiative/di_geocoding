from django.contrib import admin

from geocodingapp.models import *

class StateAdmin(admin.ModelAdmin):
    fields = ['geoid','state']
    list_display = ['geoid','state']
admin.site.register(State,StateAdmin)

class CountyAdmin(admin.ModelAdmin):
    fields = ['geoid','county','state']
    list_display = ['geoid','county','state']
admin.site.register(County,CountyAdmin)

class CityAdmin(admin.ModelAdmin):
    fields = ['geoid','city','state']
    list_display = ['geoid','city','state']
admin.site.register(City,CityAdmin)

class PointAdmin(admin.ModelAdmin):
    fields = ['lat','lng']
admin.site.register(Point,PointAdmin)

class ProjectCategoryAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(ProjectCategory,ProjectCategoryAdmin)

class GeocoderAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(Geocoder,GeocoderAdmin)

class LocationTypeAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(LocationType,LocationTypeAdmin)

class MatchLevelAdmin(admin.ModelAdmin):
    fields = ['score','name']
admin.site.register(MatchLevel,MatchLevelAdmin)

class ConfidenceLevelAdmin(admin.ModelAdmin):
    fields = ['score','name']
    list_display= ['score','name']
admin.site.register(ConfidenceLevel,ConfidenceLevelAdmin)

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title','description','category','url','start_date','end_date']
admin.site.register(Project,ProjectAdmin)

class TaskAdmin(admin.ModelAdmin):
    fields = ['description','project','note','initiate_date','file','has_result']
    readonly_fields = ['initiate_date','has_result']
admin.site.register(Task,TaskAdmin)

class AddressAdmin(admin.ModelAdmin):
    fields = ['address','task','upload_table']
admin.site.register(Address,AddressAdmin)

task = models.ForeignKey('Task')
name = models.CharField(max_length=500,null=True,blank=True)
address = models.CharField(max_length=500,null=True,blank=True)
formatted_address = models.ForeignKey('FormattedAddress',null=True,blank=True)
location = models.ForeignKey('Point',null=True,blank=True)
geocoder = models.ForeignKey('Geocoder',null=True,blank=True)
confidence_level = models.ForeignKey('ConfidenceLevel',null=True,blank=True)
accuracy = models.CharField(max_length=100,null=True,blank=True)

class GeocodingResultAdmin(admin.ModelAdmin):
    fields = ['task','name','address','formatted_address','location','geocoder','confidence_level','accuracy']
    list_display = ['task','name','address','location','geocoder','confidence_level','accuracy']
admin.site.register(GeocodingResult,GeocodingResultAdmin)

class FormattedAddressAdmin(admin.ModelAdmin):
    fields = ['address','street_number','street_name','city','state','county','zip_code']
admin.site.register(FormattedAddress,FormattedAddressAdmin)