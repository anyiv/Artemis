var tabla = $('#tabla-atcli').DataTable({
    responsive: {
        details: {
            display: $.fn.dataTable.Responsive.display.modal({
                header: function(row) {
                    var data = row.data();
                    return 'Detalles de ' + data[1] + ' ' + data[0];
                }
            }),
            render: $.fn.dataTable.Responsive.renderer.tableAll({
                tableClass: 'table'
            })
        }

    },
    "dom": '<"toolbar">frtip',
    "language": {
        "sProcessing": "Procesando...",
        "sLengthMenu": "Mostrar _MENU_ registros",
        "sZeroRecords": "No se encontraron resultados",
        "sEmptyTable": "Ningún dato disponible en esta tabla",
        "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "sInfoEmpty": "No hay registros que mostrar",
        "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
        "sInfoPostFix": "",
        "sSearch": "Buscar:",
        "sUrl": "",
        "sInfoThousands": ",",
        "sLoadingRecords": "Cargando...",
        "oPaginate": {
            "sFirst": "Primero",
            "sLast": "Último",
            "sNext": 'Siguiente',
            "sPrevious": 'Anterior',
        },
        "oAria": {
            "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
        }
    }
});

$('div.toolbar').empty(); // clears the content generated    
$('.dataTables_filter').empty(); // clears the content generated    

$('div.toolbar').append("<div class='col-sm-12 col-sm-4'><span style='color:black'><b>Mostrar <select id='tamano' class='form-group' data-width='fit'><option>10</option><option>20</option><option>50</option><option>100</option></select> Registros</b></span></div>" +
    "<div class='col-sm-12 col-sm-4'><label style='color:black;margin-bottom:5px;'><b>Filtrar por: <b></label><select id='tipopqrs' class='form-group' data-width='fit'><option>Todos</option><option>Petición</option><option>Queja</option><option>Reclamo</option><option>Sugerencia</option></select></div>" +
    "<div class='col-sm-12 col-sm-4'><label for='filtro' style='color:black;margin-left:35px;margin-top:5px;'>Buscar: </label><input id='filtro' class='form-control' style='width:70%; float:right;'></input></div>")

$('#filtro').keyup(function() {
    tabla.search(this.value).draw();
});

$('#tipopqrs').on('change', function() {
    if (this.value == 'Todos') {
        tabla.search('').draw();
    } else {
        tabla.search(this.value).draw();
    }
});

$('#tamano').on('change', function() {
    tabla.page.len(this.value).draw();
});

//Exportable table
$('.js-exportable').DataTable({
    dom: 'Bfrtip',
    responsive: true,
    buttons: [
        'copy', 'csv', 'excel', 'pdf', 'print'
    ]
});