
$(window).scroll(function(){

let position = $(this).scrollTop();

if(position >= 40){
    $('.nav-styles').addClass('nav-fade');
}else{
    $('.nav-styles').removeClass('nav-fade');
}

})


$(document).ready(function(){
   
    $('.nav-button').click(function(){
        $('.nav-button').toggleClass('change');
    })
})

