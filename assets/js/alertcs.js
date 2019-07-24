function confirmarCerrarSesion() {
    swal({
        title: "Cerrar sesión",
        text: "¿Está seguro que desea cerrar sesión? Si tiene trabajo sin guardar este se perderá.",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#58a05d",
        confirmButtonText: "Sí",
        cancelButtonText: "Cancelar",
        closeOnConfirm: false,
        closeOnCancel: true
    }, function(isConfirm) {
        if (isConfirm) {
            location.href = "/logout/"
        }
    });
}