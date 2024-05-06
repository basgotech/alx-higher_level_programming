// Add event listener when the DOM content is fully loaded
$(document).ready(function(){
    $('div#add_item').click(function(){
        var newItem = $('<li>Item</li>');
        $('ul.my_list').append(newItem);
    });
});
