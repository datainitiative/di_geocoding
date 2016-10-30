from geocodingapp.models import *
from table import Table
from table.columns import Column, LinkColumn, Link

class GeocodingResultTable(Table):
    zoom = LinkColumn(header=u'Zoom',links=[Link(text=u'<i class="fa fa-search-plus fa-lg"></i>',)])
    task = Column(field='task')
    name = Column(field='name')
    address = Column(field='address')
    formatted_address = Column(field='formatted_address')
    location = models.ForeignKey('Point',null=True,blank=True)
    geocoder = models.ForeignKey('Geocoder',null=True,blank=True)
    confidence_level = models.ForeignKey('ConfidenceLevel',null=True,blank=True)
    accuracy = models.CharField(max_length=100,null=True,blank=True)
    final_source = models.ForeignKey('FinalSource',default=1)

    class Meta:
        model = GeocodingResult
        
<td><a href="#panel-map" title="Zoom to on Map" class="record-zoom-to-map" id="{{r.location.lat}},{{r.location.lng}},{{r.name}}"></a></td>
<td>{{r.name}}</td>
<td>{{r.address}}</td>
<td>
	{% if r.location %}
		{{r.location.lat}},{{r.location.lng}}
	{% else %}
		None
	{% endif %}
</td>
<td>{{r.geocoder}}</td>
{% if r.confidence_level.score > 7 %}
	<td>{{r.confidence_level.score}}</td>
{% else %}
	<td><span class="text-danger"><strong>{{r.confidence_level.score}}</strong></span></td>
{% endif %}
{% if user|has_group:"Staff Admin" %}
	<td>{{r.accuracy}}</td>
	<td>{{r.final_source.name}}</td>
{% endif %}
<td>
	{% if r.location %}
		<a href="{% setting 'ROOT_APP_URL' %}/geocoding/get_cf_link?task={{task_id}}&lat={{r.location.lat}}&lng={{r.location.lng}}" target="_blank" class="record-cflink" title="View Neighborhood Summary on Community Facts"><i class="fa fa-bar-chart fa-lg"></i></a>
	{% endif %}
</td>
{% if user|has_group:"Staff Admin" %}
	<td><a href="{% url 'admin:index' %}geocodingapp/geocodingresult/{{r.id}}/" target="_blank" class="record-edit" title="Edit Record"><i class="fa fa-edit fa-lg"></i></a></td>
{% endif %}
