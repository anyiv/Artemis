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
                success: function(data) {
                    if (data.cliente_existe) {
                        if (data.usuario_existe) {
                            $("#nombreusuario").val(data.nombre_usuario);
                            $("#nombre").val(data.nombre);
                            $("#apellido").val(data.apellido);
                            $("#direccion").val(data.direccion);
                            swal("Existe", "El cliente se encuentra en la base de datos y ha sido cargado con éxito", "success");
                        } else {
                            $("#formulario").trigger("reset");
                            swal("Existe, pero...", "El cliente se encuentra en la base de datos pero no tiene un usuario registrado en el sistema", "warning");
                        }
                    } else {
                        $("#formulario").trigger("reset");
                        swal("No existe", "El cliente no se ha encontrado en la BD.", "info");
                    }
                }
            });
        }
    };