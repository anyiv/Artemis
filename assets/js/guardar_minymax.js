function guardarminymax() {
    var valormin = $("#valormin").val();
    var valormax = $('#valormax').val();
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    if (valormax == '' || valormin=='') {
        swal("Error","Debe ingresar un valor","warning");
    } else {
        $.ajax({
            url: '/ajax/guardarminymax/',
            type: 'POST',
            data: {
                'valormin': valormin,
                'valormax': valormax,
                'csrfmiddlewaretoken': token
            },
            dataType: 'json',
            success: function (data) {
                swal("Resultado",data.texto,data.icono);
            }
        });
    }
};

function confirmarConfig(){
    swal({
        title: "Confirmar",
        text: "¿Está seguro que desea guardar?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#58a05d",
        confirmButtonText: "Sí",
        cancelButtonText: "Cancelar",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (isConfirm) {
            guardarminymax();
        } else {
            swal("Cancelada", "Los cambios han sido cancelados.", "error");
        }
    });
}