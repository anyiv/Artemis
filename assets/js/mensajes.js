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

function confirmarCambiarContraseña(){
    swal({
        title: "Confirmar",
        text: "¿Está seguro que desea cambiar la contraseña?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#58a05d",
        confirmButtonText: "Sí",
        cancelButtonText: "Cancelar",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (isConfirm) {
            formulario.submit();
        } else {
            swal("Cancelada", "El cambio ha sido cancelado.", "error");
        }
    });
}

function confirmarValoración(){
    swal({
        title: "Confirmar",
        text: "¿Está seguro que desea enviar la valoración?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#58a05d",
        confirmButtonText: "Sí",
        cancelButtonText: "Cancelar",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (isConfirm) {
            formulario.submit();
        } else {
            swal("Cancelada", "El envío ha sido cancelado.", "error");
        }
    });
}

function exitoValoracion() {
    swal("Enviada", "La valoración ha sido enviada con éxito.", "success");
};

function confirmarCopiarDatos(){
    swal({
        title: "Confirmar",
        text: "¿Está seguro que desea copiar los datos externos ahora?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#58a05d",
        confirmButtonText: "Sí",
        cancelButtonText: "Cancelar",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (isConfirm) {
            swal("Copiado", "La copia se ha realizado con éxito.", "success");
        } else {
            swal("Cancelada", "El proceso ha sido cancelado.", "error");
        }
    });
}

function confirmarDatosExternos(){
    swal({
        title: "Confirmar",
        text: "¿Está seguro que desea guardar los cambios ahora?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#58a05d",
        confirmButtonText: "Sí",
        cancelButtonText: "Cancelar",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (isConfirm) {
            swal("Guardado", "Los cambios se han realizado con éxito.", "success");
        } else {
            swal("Cancelada", "El proceso ha sido cancelado.", "error");
        }
    });
}

function confirmarEnvioReclamo() {
    if ($("#nombreusuario").val() != '') {
    swal({
        title: "Confirmar envío",
        text: "¿Está seguro que desea enviar el reclamo?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#58a05d",
        confirmButtonText: "Sí",
        cancelButtonText: "Cancelar",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (isConfirm) {
        if (isConfirm) {
            formulario.submit();
        } else {
            swal("Cancelada", "El reclamo no ha sido enviado.", "error");
        }
    });
    } else {
        swal("Error", "Debe cargar un cliente para poder enviar la petición y la identificación no puede estar vacía.", "warning");
    }
}

function exitoEnviarReclamo() {
    swal("Enviado", "El Reclamo ha sido enviado con éxito.", "success");
};