// Wait for the document to be fully loaded
$(document).ready(function(){
    // Add a click event listener to the DIV#red_header
    $('div#red_header').click(function(){
        // Update the text color of the <header> element to red (#FF0000)
        $('header').css('color', '#FF0000');
    });
});
