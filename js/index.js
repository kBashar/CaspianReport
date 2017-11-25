var generate_country = function (name) {
    var vids = $('#videos');
    vids.html('');
    $('#country').html(name);
    $.getJSON("json/countries.json", function(json) {
        var videos = json[name];
        $('#country').html(name);
        for (var id in videos) {
            vids.append("<p>" + id + "</p>")
        }
    });
};