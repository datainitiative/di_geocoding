// Home Page
var enjoyhint_script_steps_first_time_visitor_home_page = [{
		"next #site-name": "Welcome to Geocoding Tool!\n We noticed you are new! Let us walk you through.",
		"nextButton" : {className: "myNext", text: "Continue"},
		"skipButton" : {className: "mySkip", text: "No Thanks"},
	}];

var enjoyhint_script_steps_home_page = [
	{
		"next #start-single-task": "Click here to create a single geocoding task for batch geocoding addresses from a spreadsheet you upload.",
		"skipButton" : {className: "mySkip", text: "Exit"},
		"nextButton" : {className: "myNext2Line", text: "Next"},
	},
	{
		"next #start-new-project": "Click here to start a brand new project where you can add geocoding tasks to it.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #panel-instant-geocoding": "Instant Geocoding allows you to find the location of an address on the map.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #input-address": "Enter an address here, including street address, city, state, and zip code. Zip code is optional, but is requried if city and state are not specified.",
		"skipButton" : {className: "mySkip", text: "Exit"},
		"nextButton" : {className: "myNext2Line", text: "Next"},
	},
	{
		"click #btn-geocode": "Press 'Enter' or click this button to start geocoding.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #map": "A marker will be dropped on the map at the location of the address.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #input-point-coord": "Here is the latitude-longitude coordinates of the address location.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #copy-coordinates": "Click here to copy coordinates to clipboard.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #panel-geocoder-usage": "Some of the online geocoders have limits on API queris.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #table-geocoder-usage": "Check online geoocder allowence here.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #btn-site-tour-home-page": "You can always come back to this tutorial by clicking the question mark here.",
		"nextButton" : {className: "myNext", text: "Got it!"},
		"showSkip": false,
	}
];

// Home Page Admin View Button Click
$("#btn-site-tour-home-page").click(function(){
	var enjoyhint_instance = new EnjoyHint({});
	enjoyhint_instance.set(enjoyhint_script_steps_home_page);
	enjoyhint_instance.run();
});

var enjoyhint_script_steps_home_page_2 = [
	{
		"next #panel-welcome": "The summary of your geocoding tasks can be found here in the Welcome Panel.",
		"skipButton" : {className: "mySkip", text: "Exit"},
		"nextButton" : {className: "myNext2Line", text: "Next"},
	},
	{
		"next #start-single-task": "Click here to create a geocoding task for geocoding addresses from a spreadsheet you upload.",
		"skipButton" : {className: "mySkip", text: "Exit"},
		"nextButton" : {className: "myNext2Line", text: "Next"},
	},
	{
		"next #start-instant-geocoding": "Click here to loate an address on the map.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #panel-instant-geocoding": "Instant Geocoding allows you to find the location of an address on the map.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #input-address": "Enter an address here, including street address, city, state, and zip code. Zip code is optional, but is requried if city and state are not specified.",
		"skipButton" : {className: "mySkip", text: "Exit"},
		"nextButton" : {className: "myNext2Line", text: "Next"},
	},
	{
		"click #btn-geocode": "Press 'Enter' or click this button to start geocoding.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #map": "A marker will be dropped on the map at the location of the address.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #input-point-coord": "Here is the latitude-longitude coordinates of the address location.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #copy-coordinates": "Click here to copy coordinates to clipboard.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"click #balanceswitch": "Some of the online geocoders have limits on API queris. Click here to check current balance.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #balance-panel": "Balance for the usage of each geocoder is shown here.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #btn-site-tour-home-page-2": "You can always come back to this tutorial by clicking the question mark here.",
		"nextButton" : {className: "myNext", text: "Got it!"},
		"showSkip": false,
	}
];

// Home Page User View Button Click
$("#btn-site-tour-home-page-2").click(function(){
	var enjoyhint_instance = new EnjoyHint({});
	enjoyhint_instance.set(enjoyhint_script_steps_home_page_2);
	enjoyhint_instance.run();
});


// Add Project
var enjoyhint_script_steps_add_project = [
	{
		"next #id_title": "Enter the title of your project. This field is requried.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #id_description": "Description of your project. (Optional)",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #id_category": "Select a category. (Required)",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #id_url": "URL to your project website. (Optional)",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"click #id_start_date": "Click to enter project start date. (Required)",
		"showSkip": false,
	},
	{
		"next #id_start_date + .datetimeshortcuts": "Click the calendar icon to select a date, or click today.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"click #id_end_date": "Click to enter project due date. (Required)",
		"showSkip": false,
	},
	{
		"next #id_end_date + .datetimeshortcuts": "Click the calendar icon to select a date, or click today.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next input[name='_continue']": "Click here to save your project.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #btn-site-tour-add-project": "You can always come back to this tutorial by clicking the question mark here.",
		"nextButton" : {className: "myNext", text: "Got it!"},
		"showSkip": false,
	}
];

// Add Project Button Click
$("#btn-site-tour-add-project").click(function(){
	var enjoyhint_instance = new EnjoyHint({});
	enjoyhint_instance.set(enjoyhint_script_steps_add_project);
	enjoyhint_instance.run();
});

// Post-Add Project
var enjoyhint_script_steps_post_add_project = [
	{
		"next #panel-task-list": "Here is a list of geocoding tasks added to this project.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #add-new-geocoding-task": "Click here to add a geocoding task to this project.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #btn-site-tour-post-add-project": "You can always come back to this tutorial by clicking the question mark here.",
		"nextButton" : {className: "myNext", text: "Got it!"},
		"showSkip": false,
	}
];

// Post-Add Project Button Click
$("#btn-site-tour-post-add-project").click(function(){
	var enjoyhint_instance = new EnjoyHint({});
	enjoyhint_instance.set(enjoyhint_script_steps_post_add_project);
	enjoyhint_instance.run();
});

// Add Task
var enjoyhint_script_steps_add_task = [
	{
		"next #id_description": "Describe the geocoding task here. This field is requried.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #id_project": "Select the project that new task will be added to. The project will be preselected if you come from the project page.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #id_note": "Add note for the task. (Optional)",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #id_file": "Choose the address file to uplaod. Excel spreadsheet and CSV file are supported.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next input[name='_continue']": "Click here to save your task.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #btn-site-tour-add-task": "You can always come back to this tutorial by clicking the question mark here.",
		"nextButton" : {className: "myNext", text: "Got it!"},
		"showSkip": false,
	}
];

// Add Task Button Click
$("#btn-site-tour-add-task").click(function(){
	var enjoyhint_instance = new EnjoyHint({});
	enjoyhint_instance.set(enjoyhint_script_steps_add_task);
	enjoyhint_instance.run();
});


// Post-Add Task
var enjoyhint_script_steps_post_add_task = [
	{
		"next #btn-setup-geocoding": "Click here to setup geocoding configuration before geocoding process.",
		"nextButton" : {className: "myNext", text: "Got it!"},
		"showSkip": false,
	},
];

var enjoyhint_script_steps_post_add_task_view_results = [
	{
		"next #btn-view-geocoding-results": "Click here to view geocoding results.",
		"nextButton" : {className: "myNext", text: "Got it!"},
		"showSkip": false,
	},
];

// Post-Add Project Button Click
$("#btn-site-tour-post-add-task").click(function(){
	var enjoyhint_instance = new EnjoyHint({});
	if ($("#btn-setup-geocoding").length){
		enjoyhint_instance.set(enjoyhint_script_steps_post_add_task);}
	else {
		enjoyhint_instance.set(enjoyhint_script_steps_post_add_task_view_results);}
	enjoyhint_instance.run();
});


// Setup Geocoding
var enjoyhint_script_steps_setup_geocoding = [
	{
		"next #panel-field-mapping-header": "Mapping the 'columns' in address file to the 'fields' required by the geocoder.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #panel-table-preview": "For reference, you can preview the first 10 rows of the address file here.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #sel-address": "Select the column that contains street address. This field is required.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #sel-city": "Select the column that contains city name. This field is required if zip code is not specified. If city is already included in street address column, leave this field as 'None'.",
		"skipButton" : {className: "mySkip", text: "Exit"},
		"nextButton" : {className: "myNext2Line", text: "Next"},
	},
	{
		"next #sel-state": "Select the column that contains state name. This field is required if zip code is not specified. If state is already included in street address column, leave this field as 'None'.",
		"skipButton" : {className: "mySkip", text: "Exit"},
		"nextButton" : {className: "myNext2Line", text: "Next"},
	},
	{
		"next #sel-zip": "Select the column that contains zip code. This field is required if city and state are not specified.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #sel-label": "Select the column that contains the unique identifier or the name of the address, eg. business name, school name, etc. This field is required.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #geocoding_url": "Click here to start geocoding. The process takes seconds to minutes depending on the number of addresses to be geocoded. Please don't close this page while it's processing. ",
		"skipButton" : {className: "mySkip", text: "Exit"},
		"nextButton" : {className: "myNext2Line", text: "Next"},
	},
	{
		"next #btn-site-tour-setup-geocoding": "You can always come back to this tutorial by clicking the question mark here.",
		"nextButton" : {className: "myNext", text: "Got it!"},
		"showSkip": false,
	}
];

// Setup Geocoding Button Click
$("#btn-site-tour-setup-geocoding").click(function(){
	var enjoyhint_instance = new EnjoyHint({});
	enjoyhint_instance.set(enjoyhint_script_steps_setup_geocoding);
	enjoyhint_instance.run();
});


// Geocoding Result
var enjoyhint_script_steps_geocoding_result = [
	{
		"next #btn-download-csv": "You can download geocoding results as a CSV file from here.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #mapview": "The address locations are displayed on the map. Locations are clustered with numbers shown on the marker. By clicking the cluster marker or zooming-in closer, the points will spread out.",
		"skipButton" : {className: "mySkip", text: "Exit"},
		"nextButton" : {className: "myNext2Line", text: "Next"},
	},
	{
		"next .leaflet-control-layers": "Use layer control to switch between Cluster Map visualization and Heat Map visualization.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #div-size-slider": "User this slider to change cluster size. Map points will become more clustered as the cluster size increase.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #div-size-slider": "When Heat Map layer is selected, use this slider to change radius size.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"click #geocodingresultswitch": "Click to show Geocoding result table.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #dataTables-example_filter": "You can search for result that contains certain text.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #tbheader-confidence": "Geocoding results are sorted by confidence level in ascending order. Location with confidence level LOWER THAN 8 should be used with caution.",
		"skipButton" : {className: "mySkip", text: "Exit"},
		"nextButton" : {className: "myNext2Line", text: "Next"},
	},
	{
		"next .record-edit": "Click here to edit Geocoding result to fix any inaccurate or incorrect location.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next .record-cflink": "Click here to see neighborhood summary of this location on Community Facts website.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next .record-zoom-to-map": "Click here to zoom to the location on the map",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"click #geocodingresultswitch": "Click to hide Geocoding result table.",
		"skipButton" : {className: "mySkip", text: "Exit"},
	},
	{
		"next #btn-site-tour-geocoding-result": "You can always come back to this tutorial by clicking the question mark here.",
		"nextButton" : {className: "mySkip", text: "Got it!"},
		"showSkip": false,
	}
];

// Setup Geocoding Button Click
$("#btn-site-tour-geocoding-result").click(function(){
	var enjoyhint_instance = new EnjoyHint({});
	enjoyhint_instance.set(enjoyhint_script_steps_geocoding_result);
	enjoyhint_instance.run();
});