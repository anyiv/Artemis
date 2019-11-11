function anadir_comentario() {
    var reclamo = $("#codReclamo").val();
    var comentario = $('#comentario').val();
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    if (comentario == '') {
        swal("Error","Debe escribir un comentario.","warning");
    } else {
        $.ajax({
            url: '/ajax/anadir_comentario/',
            type: 'POST',
            data: {
                'cod_reclamo': reclamo,
                'comentario': comentario,
                'csrfmiddlewaretoken': token
            },
            dataType: 'json',
            success: function (data) {
                swal("Resultado",data.texto,data.icono);
                $('#comentarios').modal('hide');
                window.location.reload();
            }
        });
    }
};