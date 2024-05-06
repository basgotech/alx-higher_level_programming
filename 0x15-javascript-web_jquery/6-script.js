// Add event listener when the DOM content is fully loaded
$(document).ready(function(){
    $('div#update_header').click(function(){
        $('header').text('New Header!!!');
    });
});
