

$(document).ready(function() {
bindAccountMenuBox();
bindInputRegisterForm();
    
});

function bindAccountMenuBox(){
    $('.navBarItem').each(function() {
        $(this).on('click', function(e) {
            var top = $(this).offset().top;
            var left = $(this).offset().left;
            if (this.dataset.trigger == "account"){
                let accountBox = $('.account');
                $(accountBox).offset({ top : top + 12,  left: left - 30});
                $(accountBox).toggleClass("show");
                accBoxMouseListener();
            }
        });
    });
}

function accBoxMouseListener() {
    let accountBox = $('.account');
    $( accountBox ).mouseleave(function() {
        setTimeout(() => {
            accountBox.removeClass("show");
        }, 150);
    });
} 

function bindInputRegisterForm(){
    $( ".registerForm .fieldWrapper input" ).each(function() {
        $(this).on('click', function(){
            $(this).closest('.fieldWrapper').children('label').addClass( "labelOnFocus" );
            $(this).closest('.fieldWrapper').children('label').removeClass("labelNoFocus");
                $(this).focusout(function(){
                    if(!$(this).val()){
                        $(this).closest('.fieldWrapper').children('label').addClass( "labelNoFocus" );
                        $(this).closest('.fieldWrapper').children('label').removeClass("labelOnFocus");
                    }
                });

        });
      });
}