function llenarReporteFallas() {
    document.getElementById('donut_chart').innerHTML = "";
    var fechai = $("#fecha_i").val();
    var fechaf = $("#fecha_f").val();
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    if (fechai == '' || fechaf == '') {
        swal("Error", "Debe introducir ambas fechas para realizar la consulta.", "warning")
    } else {
        $.ajax({
            url: '/ajax/reporte/fallas/',
            type: 'POST',
            data: {
                'fechai': fechai,
                'fechaf': fechaf,
                'csrfmiddlewaretoken': token
            },
            dataType: 'json',
            success: function (data) {
                $("#reportes_fallas").css("display", "");
                if (data.resultado) {
                    swal("Error", data.resultado, "warning");
                    $("#reportes_fallas").css("display", "none");
                } else {
                    var colores = ["#d8a47f", "#88498f", "#fac85f", "#f06543", "#706c61", "#2f97c1"]
                    Morris.Donut({
                        element: 'donut_chart',
                        data: data,
                        colors: colores,
                        formatter: function (y) {
                            return y + '%'
                        }
                    });
                    var tabla = ""
                    data.forEach(function (categoria, indice, array) {
                        var color = "";
                        if (indice>colores.length){
                            color = colores[indice%colores.length-1];
                        } else {
                            color = colores[indice];
                        }
                        tabla +=
                            "<tr>" +
                            "<td>" + categoria.label + "</td>" +
                            "<td>" + categoria.conteo + "</td>" +
                            "<td>" +
                            "<div class=\"progress\">" +
                            "<div class=\"progress-bar\" role=\"progressbar\" aria-valuenow=\"" + categoria.value_int + "\"" +
                            "aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: " + categoria.value_int + "%;background-color:" + color + ";\"></div>" + categoria.value + "%" +
                            "</div>" +
                            "</td>" +
                            "</tr>"
                    });
                    document.getElementById('cuerpo_tabla_fallas').innerHTML = tabla;
                }
            }
        });
    }
}