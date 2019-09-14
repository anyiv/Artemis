//Bootstrap datepicker plugin
$('#bs_datepicker_container input').datepicker({
    autoclose: true,
    container: '#bs_datepicker_container'
});

$('#bs_datepicker_component_container').datepicker({
    autoclose: true,
    container: '#bs_datepicker_component_container'
});
//
$('#bs_datepicker_range_container').datepicker({
    autoclose: true,
    container: '#bs_datepicker_range_container'
});



Morris.Donut({
    element: 'donut_chart',
    data: [{
        label: 'Chrome',
        value: 37
    }, {
        label: 'Firefox',
        value: 30
    }, {
        label: 'Safari',
        value: 18
    }, {
        label: 'Opera',
        value: 12
    },
    {
        label: 'Other',
        value: 3
    }],
    colors: ['rgb(233, 30, 99)', 'rgb(0, 188, 212)', 'rgb(255, 152, 0)', 'rgb(0, 150, 136)', 'rgb(96, 125, 139)'],
    formatter: function (y) {
        return y + '%'
    }
});
