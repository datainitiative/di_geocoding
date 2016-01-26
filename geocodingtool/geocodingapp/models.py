from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from geocodingtool.settings import STORAGE_ROOTPATH

#==================
# Geography Models
#==================
class State(models.Model):
#    id = models.IntegerField(primary_key=True)
    geoid = models.CharField(max_length=2)
    state = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.state)

    class Meta:
        db_table = u'state'
        
class County(models.Model):
#    id = models.IntegerField(primary_key=True)
    geoid = models.CharField(max_length=5)
    county = models.CharField(max_length=100)
    state = models.ForeignKey('State')

    def __unicode__(self):
        return unicode(self.county)

    class Meta:
        db_table = u'county'
        ordering = ['geoid']

class City(models.Model):
#    id = models.IntegerField(primary_key=True)
    geoid = models.CharField(max_length=7)
    city = models.CharField(max_length=200)
    state = models.ForeignKey('State')

    def __unicode__(self):
        return unicode(self.city)

    class Meta:
        db_table = u'city'
        ordering = ['city']

class Point(models.Model):
#    id = models.IntegerField(primary_key=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = u'point'

#=================
# Core Models
#=================
# Model Project Category
class ProjectCategory(models.Model):
#    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        db_table = u'project_category'

# Model Geocoder (Geocoding Service/API)        
class Geocoder(models.Model):
#    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    limit = models.IntegerField(default=-1) # -1 stands for unlimited geocoding requests

    def __unicode__(self):
        return unicode(self.name)
    
    def previous(self):
        try:
            previous_records = Geocoder.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return Geocoder.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = Geocoder.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return Geocoder.objects.get(id=next_id)
        except:
            return None    

    class Meta:
        db_table = u'geocoder'
        ordering = ['id']
        
# Model Location Type
class LocationType(models.Model):
#    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        db_table = u'location_type'
        
# Model Match Level
class MatchLevel(models.Model):
#    id = models.IntegerField(primary_key=True)
    score = models.IntegerField()
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        db_table = u'match_level'

# Model Level of Confidence
class ConfidenceLevel(models.Model):
#    id = models.IntegerField(primary_key=True)
    score = models.IntegerField()
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        db_table = u'confidence_level'

# Model Project
class Project(models.Model):
#    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500,null=True,blank=True)
    category = models.ForeignKey('ProjectCategory')
    url = models.URLField(max_length=5000,null=True,blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __unicode__(self):
        return unicode(self.title)
    
    def previous(self):
        try:
            previous_records = Project.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return Project.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = Project.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return Project.objects.get(id=next_id)
        except:
            return None

    class Meta:
        db_table = u'project'
        ordering = ['id']

# Model Geocoding Task        
class Task(models.Model):
#    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=500)
    project = models.ForeignKey('Project')
    initiate_date = models.DateField(auto_now=True)
    note = models.TextField(max_length=500,null=True,blank=True)
    file = models.FileField(max_length=500,upload_to=STORAGE_ROOTPATH+"/upload/")
    has_result = models.BooleanField(default=False)
    
    def __unicode__(self):
        return str(self.id)
    
    def previous(self):
        try:
            previous_records = Task.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return Task.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = Task.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return Task.objects.get(id=next_id)
        except:
            return None
        
    class Meta:
        db_table = u'task'
        ordering = ['id']

# Model Original Address to Formatted Address
class AddressInventory(models.Model):
#    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    formatted_address = models.ForeignKey('FormattedAddress',null=True,blank=True)
    
    def __unicode__(self):
        return str(self.id)
    
    def previous(self):
        try:
            previous_records = AddressInventory.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return AddressInventory.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = AddressInventory.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return AddressInventory.objects.get(id=next_id)
        except:
            return None

    class Meta:
        db_table = u'address_inventory'
        ordering = ['id']

# Model Geocoding Results
# gocoding return geojson format example
#{
#    "geometry": {
#        "type": "Point",
#        "coordinates": [
#            -74.0059413,
#            40.7127837
#        ]
#    },
#    "type": "Feature",
#    "properties": {
#        "status": "OK",
#        "city": "New York",
#        "confidence": 1,
#        "ok": true,
#        "country": "United States",
#        "provider": "google",
#        "location": "New York City",
#        "state": "New York",
#        "address": "New York, NY, USA",
#        "lat": 40.7127837,
#        "lng": -74.0059413,
#        "quality": "locality",
#        "accuracy": "APPROXIMATE"
#    },
#    "bbox": [
#        -74.25908989999999,
#        40.4913686,
#        -73.70027209999999,
#        40.91525559999999
#    ]
#}
#
class GeocodingResult(models.Model):
#    id = models.IntegerField(primary_key=True)
    task = models.ForeignKey('Task')
    name = models.CharField(max_length=500,null=True,blank=True)
    address = models.CharField(max_length=500,null=True,blank=True)
    formatted_address = models.ForeignKey('FormattedAddress',null=True,blank=True)
    location = models.ForeignKey('Point',null=True,blank=True)
    geocoder = models.ForeignKey('Geocoder',null=True,blank=True)
    confidence_level = models.ForeignKey('ConfidenceLevel',null=True,blank=True)
    accuracy = models.CharField(max_length=100,null=True,blank=True)
#    location_type = models.ForeignKey('LocationType')
#    match_level = models.ForeignKey('MatchLevel')
    
    def __unicode__(self):
        return str(self.id)
    
    def previous(self):
        try:
            previous_records = GeocodingResult.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return GeocodingResult.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = GeocodingResult.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return GeocodingResult.objects.get(id=next_id)
        except:
            return None

    class Meta:
        db_table = u'geocoding_result'
        ordering = ['id']
        
# Model Formatted Address
class FormattedAddress(models.Model):
#    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=500,null=True,blank=True)
#    street_number = models.CharField(max_length=50,null=True,blank=True)
#    street_name = models.CharField(max_length=250,null=True,blank=True)
#    city = models.ForeignKey('City',null=True,blank=True)
#    state = models.ForeignKey('State',null=True,blank=True)
#    county = models.ForeignKey('County',null=True,blank=True)
#    zip_code = models.CharField(max_length=5,null=True,blank=True)
    point = models.ForeignKey('Point',null=True,blank=True)
    geocoder = models.ForeignKey('Geocoder',null=True,blank=True)
    confidence_level = models.ForeignKey('ConfidenceLevel',null=True,blank=True)
    
    def __unicode__(self):
        return str(self.id)
    
    def previous(self):
        try:
            previous_records = FormattedAddress.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return FormattedAddress.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = FormattedAddress.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return FormattedAddress.objects.get(id=next_id)
        except:
            return None

    class Meta:
        db_table = u'formatted_address'
        ordering = ['id']
        
# Geocoder Usage
class GeocoderUsage(models.Model):
#    id = models.IntegerField(primary_key=True)
    geocoder = models.ForeignKey('Geocoder')
    geocoding_record_num = models.IntegerField(default=0)
    last_geocoding_time = models.DateTimeField(auto_now=True)
    has_expired = models.BooleanField(default=False)
    
    def __unicode__(self):
        return str(self.id)
    
    def previous(self):
        try:
            previous_records = GeocoderUsage.objects.filter(id__lt=self.id)
            previous_id = previous_records.order_by('-id')[0].id
            return GeocoderUsage.objects.get(id=previous_id)
        except:
            return None
        
    def next(self):
        try:
            next_records = GeocoderUsage.objects.filter(id__gt=self.id)
            next_id = next_records.order_by('id')[0].id
            return GeocoderUsage.objects.get(id=next_id)
        except:
            return None

    class Meta:
        db_table = u'geocoder_usage'
        ordering = ['id']