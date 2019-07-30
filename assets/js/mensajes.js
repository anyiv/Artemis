function confirmarPeticion() {
    if ($("#nombreusuario").val() != '') {
        swal({
            title: "Confirmar envío",
            text: "¿Está seguro que desea enviar la petición?",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#58a05d",
            confirmButtonText: "Sí",
            cancelButtonText: "Cancelar",
            closeOnConfirm: false,
            closeOnCancel: false
        }, function(isConfirm) {
            if (isConfirm) {
                formulario.submit();
            } else {
                swal("Cancelada", "La petición no ha sido enviada.", "error");
            }
        });
    } else {
        swal("Error", "Debe cargar un cliente para poder enviar la petición", "warning");
    }
};

function exitoPeticion() {
    swal("Enviada", "La petición ha sido enviada con éxito.", "success");
};

function confirmarQueja() {
    if ($("#nombreusuario").val() != '') {
        swal({
            title: "Confirmar envío",
            text: "¿Está seguro que desea enviar la queja?",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#58a05d",
            confirmButtonText: "Sí",
            cancelButtonText: "Cancelar",
            closeOnConfirm: false,
            closeOnCancel: false
        }, function(isConfirm) {
            if (isConfirm) {
                formulario.submit();
            } else {
                swal("Cancelada", "La queja no ha sido enviada.", "error");
            }
        });
    } else {
        swal("Error", "Debe cargar un cliente para poder enviar la queja", "warning");
    }
};

function exitoQueja() {
    swal("Enviada", "La queja ha sido enviada con éxito.", "success");
};

function confirmarSugerencia() {
    if ($("#nombreusuario").val() != '') {
        swal({
            title: "Confirmar envío",
            text: "¿Está seguro que desea enviar la sugerencia?",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#58a05d",
            confirmButtonText: "Sí",
            cancelButtonText: "Cancelar",
            closeOnConfirm: false,
            closeOnCancel: false
        }, function(isConfirm) {
            if (isConfirm) {
                $("#formulario").submit();
            } else {
                swal("Cancelada", "La sugerencia no ha sido enviada.", "error");
            }
        });
    } else {
        swal("Error", "Debe cargar un cliente para poder enviar la sugerencia", "warning");
    }
};

function exitoSugerencia() {
    swal("Enviada", "La sugerencia ha sido enviada con éxito.", "success");
};