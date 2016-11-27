$('#webus').on('click', function() {
    function loadSubmissions() {
        $.get('/load_submissions', {
            'problem_id': $('#problem_id').val()
        }).done(function(data) {
            var table = $('#submissions');
            table.html('');
            data.submissions.forEach(function (s) {
                var row = $('<tr>');
                row.append($('<td>').text(s.id));
                row.append($('<td>').text(s.user));
                row.append($('<td>').html($('<pre>').text(s.code)));
                row.append($('<td>').text(s.status));
                row.append($('<td>').text(s.info));
                table.prepend(row);
            });
            table.prepend($('<tr> <th>#</th> <th>Пользователь</th> <th>Код</th> <th>Статус</th> <th>Комментарий</th> </tr>'));
        });
    }

    loadSubmissions();


})();



$('.web2').click(function(){
  alert('Вы нажали на элемент "foo"');
});
