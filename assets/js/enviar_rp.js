function obtenerRespuesta() {
    var resp = $("#respuestaP").val();
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    if (resp == '-') {
        $("#descripcionRP").val("")
    } else {
        $.ajax({
            url: '/ajax/obtener_respuesta/',
            type: 'POST',
            data: {
                'cod': resp,
                'csrfmiddlewaretoken': token
            },
            dataType: 'json',
            success: function (data) {
                $("#descripcionRP").val(data.descripcion);
            }
        });
    }
};

function enviarRespuesta() {
    var resp = $("#descripcionRP").val();
    var codresp = $("#respuestaP").val();
    var codrec = $("#codReclamo").val();
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    if (resp == '') {
        swal("Error", "Debe introducir o seleccionar una respuesta.", "warning")
    } else {
        $.ajax({
            url: '/ajax/enviar_rp/',
            type: 'POST',
            data: {
                'resp': resp,
                'codresp': codresp,
                'codrec': codrec,
                'csrfmiddlewaretoken': token
            },
            dataType: 'json',
            success: function (data) {
                swal("Resultado", data.texto, data.icono)
                $('#responderCliente').modal('hide');
                $("#descripcionRP").val("");
                $("#respuestaP").val("-");
                $('#respuestaP').selectpicker('refresh');
                $('#respuestaP').selectpicker('render');
            }
        });
    }
};

function obt_rp_pqs() {
    var resp_pqs = $("#respuesta_pqs").val();
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    if (resp_pqs == '-') {
        $("#descripcion_rp").val("")
    } else {
        $.ajax({
            url: '/ajax/obtener_rp_pqs/',
            type: 'POST',
            data: {
                'cod': resp_pqs,
                'csrfmiddlewaretoken': token
            },
            dataType: 'json',
            success: function (data) {
                $("#descripcion_rp").val(data.descripcion);
            }
        });
    }
};

function enviar_rp_pqs() {
    var resp = $("#descripcion_rp").val();
    var codresp = $("#respuesta_pqs").val();
    var codpqs = $("#codPQS").val();
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    if (resp == '') {
        swal("Error", "Debe introducir o seleccionar una respuesta.", "warning")
    } else {
        $.ajax({
            url: '/ajax/enviar_rp_pqs/',
            type: 'POST',
            data: {
                'resp': resp,
                'codresp': codresp,
                'codpqs': codpqs,
                'csrfmiddlewaretoken': token
            },
            dataType: 'json',
            success: function (data) {
                swal("Resultado", data.texto, data.icono)
                $('#resp_pqs').modal('hide');
                $("#descripcion_rp").val("");
                $("#respuesta_pqs").val("-");
                $('#respuesta_pqs').selectpicker('refresh');
                $('#respuesta_pqs').selectpicker('render');
            }
        });
    }
};