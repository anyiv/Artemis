$('#respuestas').on('click', function () {
    var color = $(this).data('color');
    $('#responderCliente .modal-content').removeAttr('class').addClass('modal-content modal-col-' + color);
    $('#responderCliente').modal('show');
});

$('#asignar').on('click', function () {
    var color = $(this).data('color');
    $('#tecnicos .modal-content').removeAttr('class').addClass('modal-content modal-col-' + color);
    $('#tecnicos').modal('show');
});