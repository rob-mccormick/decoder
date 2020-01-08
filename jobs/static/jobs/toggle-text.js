$('.continue-link').click(function(){
    $(this).text(function(i,old){
        return old=='Continue reading...' ?  'Click to hide text' : 'Continue reading...';
    });
});

$('.list-link').click(function(){
    $(this).text(function(i,old){
        return old=='click here' ?  'click to close' : 'click here';
    });
});
