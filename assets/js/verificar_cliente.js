function validarIdentidad() {
    var identificacion = $("#identificacion").val();
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    if (identificacion == '') {
        swal("Error", "Debe introducir una Cédula de Identidad o un RIF.", "warning")
    } else {
        $.ajax({
            url: '/ajax/validar_identidad/',
            type: 'POST',
            data: {
                'identificacion': identificacion,
                'csrfmiddlewaretoken': token
            },
            dataType: 'json',
            success: function (data) {
                if (data.cliente_existe) {
                    if (data.usuario_existe) {
                        $("#nombreusuario").val(data.nombre_usuario);
                        $("#nombre").val(data.nombre);
                        $("#apellido").val(data.apellido);
                        $("#direccion").val(data.direccion);
                        if (document.getElementById('id_codDetContrato') != null) {
                            $('#id_codDetContrato').empty();
                            $.each(data.servicios, function (indice, servicio) {
                                opc = new Option(servicio[1], servicio[0]);
                                document.getElementById('id_codDetContrato').add(opc);
                            });
                            document.getElementById('id_codDetContrato').disabled = false
                            $('#id_codDetContrato').selectpicker('refresh');
                            $('#id_codDetContrato').selectpicker('render');
                        }
                        swal("Existe", "El cliente se encuentra registrado y ha sido cargado con éxito", "success");
                    } else {
                        $("#formulario").trigger("reset");
                        swal("Existe, pero...", "El cliente se ha encontrado pero no tiene un usuario registrado en el sistema", "warning");
                    }
                } else {
                    $("#formulario").trigger("reset");
                    swal("No existe", "El cliente no se ha encontrado.", "info");
                }
            }
        });
    }
};