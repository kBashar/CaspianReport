var generate_country = function (name) {
    $.getJSON("json/countries.json", function(json) {
        console.log(json); // this will show the info it in firebug console
    });
};