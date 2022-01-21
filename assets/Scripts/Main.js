
$(document).ready(function(){
   $('.nav-button').click(function(){
    $('.nav-button').toggleClass('change');
   })
})



$(window).scroll(function(){
    let location = $(this).scrollTop();
    if(location >= 200){
        $('.nav-styles').addClass('nav-fade');
    }else{
        $('.nav-styles').removeClass('nav-fade');
    }
})


$(document).ready(function(){

    $('.header-text').addClass('header-text-color');


})



$(window).scroll(function(){

    let position =$(this).scrollTop();
    if(position >= 460){

        $('.Search').addClass('Change-Color');
    }else{
      
        $('.Search').removeClass('Change-Color');

    }

})

$(window).scroll(function(){
let location = $(this).scrollTop();
if(location >=700){

    $('.Awards-Animation1').addClass('move-to-left');
    $('.Awards-Animation2').addClass('move-to-right');
}else{

    $('.Awards-Animation1').removeClass('move-to-left');
    $('.Awards-Animation2').removeClass('move-to-right');
}
})

$('.Gallery-item').click(function(){
   let optional = $(this).attr('data-active');
   $(this).addClass('active-item').siblings().removeClass('active-item');

   if(optional == 'total'){
    $('.General').show(400);

   }else{
       
       $('.General').not('.' + optional).hide(400);
       $('.General').filter('.' + optional).show(400);

   }
})

