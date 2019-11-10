function asignarTecnico() {
    var reclamo = $("#codReclamo").val();
    var tecnico = $('#responsableReclamo').val();
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    if (tecnico == '-') {
        swal("Error","Debe seleccionar un técnico","warning");
    } else {
        $.ajax({
            url: '/ajax/asignar_tecnico/',
            type: 'POST',
            data: {
                'cod_reclamo': reclamo,
                'id_tecnico': tecnico,
                'csrfmiddlewaretoken': token
            },
            dataType: 'json',
            success: function (data) {
                swal("Resultado",data.respuesta,data.icono);
                $('#tecnicos').modal('hide');
                $('#tecnicoAsignado').val(data.tecnico);
            }
        });
    }
};