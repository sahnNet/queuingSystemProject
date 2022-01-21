$(document).ready(function(){
    $('.nav-button').click(function(){
     $('.nav-button').toggleClass('change');
    })
 })
 
 
 
 $(window).scroll(function(){
     let location = $(this).scrollTop();
     console.log(location);
     if(location >=40){
         $('.nav-styles').addClass('nav-fade');
     }else{
         $('.nav-styles').removeClass('nav-fade');
     }
 })
 