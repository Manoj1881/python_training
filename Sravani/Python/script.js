$(document).ready(function(){
    console.log("loaded");
    $.material.init();
    $(document).on("submit","#register-form",function(e)){
        e.preventDefault();
        console.log('form submitted').serialize();
        $.ajax({
            url:'/postregistration',
            type:'POST',
            data:form,
            succes:function(response){
                console.log(response);
            }
        });
    });
    
    
});