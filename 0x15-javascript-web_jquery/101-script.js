// Wait for the document to be fully loaded
$(document).ready(function(){
    $('div#add_item').click(function(){
        var newItem = $('<li>Item</li>');
        $('ul.my_list').append(newItem);
    });

    $('div#remove_item').click(function(){
        $('ul.my_list li:last-child').remove();
    });

    $('div#clear_list').click(function(){
        $('ul.my_list').empty();
    });
});
