function marcar_notificacion(id, cod, limpiar = true) {
    $.ajax({
        url: '/inbox/notifications/mark-as-read/' + id + '/',
        type: 'GET',
        success: function (data) {
            var cant_not = document.getElementById('cant_not');
            var actuales = parseInt(cant_not.innerHTML);
            var nuevos_actuales = actuales - 1;
            cant_not.innerHTML = nuevos_actuales;
            if (limpiar) {
                document.getElementById('noti-' + id).innerHTML = "";
            }
            console.log(cod.substring(0, 3));
            if (cod.substring(0, 3) == 'REC') {
                window.location.replace('/reclamo/cliente/consultar/' + cod + '/');
            } else if (cod.substring(0, 3) == 'PQS') {
                window.location.replace('/pqs/consulta/' + cod + '/');
            }
        }
    });
}

function marcar_notificacion_no_redirect(id) {
    $.ajax({
        url: '/inbox/notifications/mark-as-read/' + id + '/',
        type: 'GET',
        success: function (data) {
            document.getElementById('marcarl-' + id).innerHTML = ""
            document.getElementById('icomail-' + id).innerHTML = "mail_outline"
            $.notify({
                message: "Notificación marcada como leída."
            },
                {
                    type: "bg-black",
                    newest_on_top: true,
                    timer: 5000,
                    placement: {
                        from: "bottom",
                        align: "left"
                    },
                    template: '<div data-notify="container" class="bootstrap-notify-container alert alert-dismissible {0}\" role="alert">' +
                        '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
                        '<span data-notify="icon"></span> ' +
                        '<span data-notify="title">{1}</span> ' +
                        '<span data-notify="message">{2}</span>' +
                        '<div class="progress" data-notify="progressbar">' +
                        '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
                        '</div>' +
                        '<a href="{3}" target="{4}" data-notify="url"></a>' +
                        '</div>'
                });
        }
    });
}

function llenar_notificaciones(data) {
    var notx = document.getElementById('notificaciones');
    var cant_not = document.getElementById('cant_not');
    var actuales = parseInt(cant_not.innerHTML);
    var nuevos = parseInt(data.unread_count);
    var diferencia = nuevos - actuales;
    if (nuevos != actuales) {
        cant_not.innerHTML = nuevos;
        var nuevo_menu = "";
        data.unread_list.forEach(function (notificacion, indice, datos) {
            if (nuevos > actuales) {
                if (indice < diferencia && diferencia > 0) {
                    $.notify({
                        message: notificacion.actor + ": " + notificacion.description
                    },
                        {
                            type: "bg-black",
                            newest_on_top: true,
                            timer: 5000,
                            placement: {
                                from: "bottom",
                                align: "left"
                            },
                            template: '<div data-notify="container" class="bootstrap-notify-container alert alert-dismissible {0}\" role="alert">' +
                                '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
                                '<span data-notify="icon"></span> ' +
                                '<span data-notify="title">{1}</span> ' +
                                '<span data-notify="message">{2}</span>' +
                                '<div class="progress" data-notify="progressbar">' +
                                '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
                                '</div>' +
                                '<a href="{3}" target="{4}" data-notify="url"></a>' +
                                '</div>'
                        });
                }
            }
            var fecha_registro = new Date(notificacion.timestamp);
            var ahorita = new Date(Date.now());
            var dif = ahorita - fecha_registro;
            var dif_segundos = Math.round(dif / 1000);
            var dif_minutos = Math.round(dif_segundos / 60);
            var dif_horas = Math.round(dif_minutos / 60);
            var dif_dias = Math.round(dif_horas / 24);
            var hace = "";
            if (dif_segundos < 60) {
                hace = dif_segundos.toString() + " segundos.";
            } else if (dif_segundos == 60) {
                hace = "1 minuto.";
            } else if (dif_segundos > 60) {
                console.log("mayor que un minuto");
                if (dif_minutos < 60) {
                    hace = dif_minutos.toString() + " minutos.";
                } else if (dif_minutos == 60) {
                    hace = "1 hora.";
                } else if (dif_minutos > 60) {
                    if (dif_horas < 24) {
                        hace = dif_horas.toString() + " horas.";
                    } else if (dif_horas < 24 && dif_horas < 48) {
                        hace = "1 día.";
                    } else {
                        hace = dif_dias.toString() + " días.";
                    }
                }
            }
            nuevo_menu +=
                "<li>" +
                "<a onclick=\"marcar_notificacion(" + notificacion.slug + ",'" + notificacion.actor + "')\" class=\" waves-effect waves-block\" id=\"noti-" + notificacion.slug + "\">" +
                "<div class=\"icon-circle bg-light-green\">" +
                "<i class=\"material-icons\">mail</i>" +
                "</div>" +
                "<div class=\"menu-info\">" +
                "<h4>" + notificacion.actor + ": " + notificacion.description + "</h4>" +
                "<p>" +
                "<i class=\"material-icons\">access_time</i> " + hace +
                "</p>" +
                "</div>" +
                "</a>" +
                "</li>"
        });
        notx.innerHTML = nuevo_menu;
    }
}

function marcar_todas() {
    $.ajax({
        url: '/inbox/notifications/mark-all-as-read/',
        type: 'GET',
        success: function (data) {
            $.notify({
                message: "Todas las notificaciones han sido marcadas como leídas."
            },
                {
                    type: "bg-black",
                    newest_on_top: true,
                    timer: 5000,
                    placement: {
                        from: "bottom",
                        align: "left"
                    },
                    template: '<div data-notify="container" class="bootstrap-notify-container alert alert-dismissible {0}\" role="alert">' +
                        '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
                        '<span data-notify="icon"></span> ' +
                        '<span data-notify="title">{1}</span> ' +
                        '<span data-notify="message">{2}</span>' +
                        '<div class="progress" data-notify="progressbar">' +
                        '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
                        '</div>' +
                        '<a href="{3}" target="{4}" data-notify="url"></a>' +
                        '</div>'
                });
            setTimeout(function () {
                window.location.reload()
            }, 2000);
        }
    });
}