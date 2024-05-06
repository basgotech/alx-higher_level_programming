// Add event listener when the DOM content is fully loaded
$(document).ready(function(){
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data){
        var characterName = data.name;
        $('div#character').text(characterName);
    });
});
