var generate_country = function (name) {
    var vids = $('#videos');
    vids.html('');
    $('#country').html(name);
    $.getJSON("json/countries.json", function(json) {
        var videos = json[name];
        $('#country').html(name);
        for (var id in videos) {
            vids.append("<tr>");
            vids.append("<th>" + id + "</th>");
            vids.append("<th>" + videos[id] + "</th>");
            vids.append("</tr>");
        }
    });
};