function finalizarpqs(codigo) {
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/ajax/finalizarpqs/',
        type: 'POST',
        data: {
            'codpqs': codigo,
            'csrfmiddlewaretoken': token
        },
        dataType: 'json',
        success: function (data) {
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

function confirmarSeleccion(codigo) {
    swal({
        title: "Confirmar",
        text: "¿Está seguro que desea finalizar?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#58a05d",
        confirmButtonText: "Sí",
        cancelButtonText: "Cancelar",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (isConfirm) {
            finalizarpqs(codigo);
        } else {
            swal("Cancelado", "Los cambios no han sido guardados.", "error");
        }
    });
}