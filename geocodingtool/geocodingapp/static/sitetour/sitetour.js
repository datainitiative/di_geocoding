var enjoyhint_script_steps_first_time_visitor_home_page = [{
		"next #site-name": "Welcome to Geocoding Tool!\n We noticed you are new! Let us walk you through.",
		"nextButton" : {className: "myNext", text: "Continue"},
		"skipButton" : {className: "mySkip", text: "No Thanks"},
	}];

var enjoyhint_script_steps_home_page = [
	{
		"next #start-single-task": "Click here to create a single geocoding task for batch geocoding addresses in a spreadsheet you upload.",
		"skipButton" : {className: "mySkip", text: "Exit"},
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
	},
	{
		"next #btn-geocode": "Click to start geocoding.",
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
		"click #btn-site-tour": "You can always come back to this tutorial by clicking the question mark here.",
		"showNext": false,
		"skipButton" : {className: "mySkip", text: "Got it!"},
	}
];

// Site Tour JS	
$("#btn-site-tour").click(function(){
	var enjoyhint_instance = new EnjoyHint({});
	enjoyhint_instance.set(enjoyhint_script_steps_home_page);
	enjoyhint_instance.run();
});