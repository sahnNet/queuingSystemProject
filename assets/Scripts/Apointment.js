
$(window).scroll(function(){

    let location = $(this).scrollTop();
 
    if(location >= 49){
        $('.navbar-styles').addClass('nav-fade');
    }else {
        $('.navbar-styles').removeClass('nav-fade');
    }
})

$(document).ready(function(){
    $('.nav-button').click(function(){
     $('.nav-button').toggleClass('change');
    })
 })

$(document).ready(function(){

   $('.botton').click(function(){
       
    $(this).addClass('btn-change').siblings().removeClass('btn-change');
   })
})