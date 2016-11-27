$('.wow').click(function() {
    function forEach(data, callback){
      for(var key in data){
        if(data.hasOwnProperty(key)){
          callback(key, data[key]);
        }
      }
    }

    $.ajax({
        url: '/load_calc',
        dataType: 'json',
        success: function(data){
            var str = [];
            data.uslugi1.forEach(function(key,value) {
                str.push('<b>' + key + '</b> = ' + value);
            });
            $('div').html( str.join('<br>') );
        }
    });
    return false;
});



function NeedratingList() {
    $('.ajaxProgress').show();
    $.ajax({
        type: "GET",
        url: "/NeedratingList",
        dataType: "json",
        async:true,
        data: {csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (json) {
            $('#output').html(json.message);
            $('.ajaxProgress').hide();
            GetRating(json.message);
        }
    });
}



$('#yes').click(function(){
    $.getJSON("/hello", function(data){
        var vfs = [];
        $.each(data, function(key, value){

            $("ul.vfs").append("<li>"+value.fields.title+" - "+value.fields.price+" р. </li>" );


        });

    });
});

$('<div class="ye"></div>').click(function(){
  alert('Вы нажали на элемент "foo"');
});

$('.calcutta').click(function(){
    $.getJSON("/calcutta", function(data){
        var dmw = [];
        $.each(data, function(key, value){

            $("ul.dmw").append("<li>  - "+data.title+" р. </li>" );


        });

    });
});

