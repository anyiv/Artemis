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
                $('#comentarios').modal('hide');
                $('#comentario').val('');
                swal({
                    title: "Resultado",
                    text: data.texto,
                    type: data.icono,
                    showCancelButton: false,
                    confirmButtonColor: "#58a05d",
                    confirmButtonText: "Aceptar",
                    closeOnConfirm: false,
                    closeOnCancel: false
                }, function (isConfirm) {
                    if (isConfirm) {
                        location.reload();
                    }
                });
            }
        });
    }
};