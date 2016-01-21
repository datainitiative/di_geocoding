import os

from django.contrib import admin
from django.utils.html import mark_safe

from geocodingtool.settings import ADMIN_ROOT_URL, ROOT_APP_URL
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
    fields = ['name','limit']
    list_display = ['name','limit']
admin.site.register(Geocoder,GeocoderAdmin)

class LocationTypeAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(LocationType,LocationTypeAdmin)

class MatchLevelAdmin(admin.ModelAdmin):
    fields = ['score','name']
admin.site.register(MatchLevel,MatchLevelAdmin)

class ConfidenceLevelAdmin(admin.ModelAdmin):
    fields = ['score','name']
    list_display = ['score','name']
admin.site.register(ConfidenceLevel,ConfidenceLevelAdmin)

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    max_num = 0
    readonly_fields = ['description','project','file_name','initiate_date','has_result','change_link','geocoding_result_link']
    can_delete = False
    exclude = ('file','note',)
    
    def file_name(self, obj):
        return os.path.basename(obj.file.name)
    file_name.short_description = "File Name"
    
    def change_link(self, obj):
        return mark_safe('<a href="%s/admin/geocodingapp/task/%s/" target="_blank" title="Edit"><i class="fa fa-edit fa-lg"></i></a>' % (ADMIN_ROOT_URL,obj.id))
    change_link.short_description = "Edit"
    
    def geocoding_result_link(self, obj):
        if obj.has_result:
            return mark_safe('<a href="%s/geocoding/results?task=%s" target="_blank" title="View Geocoding Results"><i class="fa fa-map-marker fa-lg"></i></a>' % (ROOT_APP_URL,obj.id))
        else:
            return mark_safe('<a href="%s/geocoding/setup?task=%s" title="Go Geocoding"><i class="fa fa-arrow-circle-right fa-lg"></i></a>' % (ROOT_APP_URL,obj.id))
    geocoding_result_link.short_description = "Results"  

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title','description','category','url','start_date','end_date']
    list_display = ['title','description','category','start_date','end_date']
    list_filter = ['category']
    inlines = [TaskInline,]
admin.site.register(Project,ProjectAdmin)

class TaskAdmin(admin.ModelAdmin):
    fields = ['description','project','note','initiate_date','file','has_result']
    list_display = ['description','project','initiate_date','has_result','geocoding_result_link']
    list_filter = ['project','has_result']
    readonly_fields = ['initiate_date','has_result']
    
    def geocoding_result_link(self, obj):
        if obj.has_result:
            return mark_safe('<a href="%s/geocoding/results?task=%s" target="_blank" title="View Geocoding Results"><i class="fa fa-map-marker fa-lg"></i></a>' % (ROOT_APP_URL,obj.id))
        else:
            return mark_safe('<a href="%s/geocoding/setup?task=%s" title="Go Geocoding"><i class="fa fa-arrow-circle-right fa-lg"></i></a>' % (ROOT_APP_URL,obj.id))
    geocoding_result_link.short_description = "Results" 
    
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
    fields = ['address','point','confidence_level']
admin.site.register(FormattedAddress,FormattedAddressAdmin)

class GeocoderUsageAdmin(admin.ModelAdmin):
    fields = ['geocoder','geocoding_record_num','last_geocoding_time']
    readonly_fields = ['last_geocoding_time']
admin.site.register(GeocoderUsage,GeocoderUsageAdmin)