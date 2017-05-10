var myChart = echarts.init(document.getElementById('main'));

function random() {
    var r = Math.round(Math.random() * 100);
    return r;
}

var swimmings = [];
var drownings = [];
function initDataArray(arr) {
    var arr = [];
    var len = 10;
    var id = 0;
    while (len--) {
        arr.push([-1, -1,
            0,
            false
        ]);
    }
    return arr;
}
swimmings = initDataArray(swimmings);
drownings = initDataArray(drownings);

option = {
    tooltip: {
        trigger: 'item',
        formatter: function(params, ticket, callback) {
            data = params.data;
            return 'x:' + data[0] +
                '<br/> y:' + data[1] +
                '<br/> heartbeat:' + data[2];
        }
    },
    label: {
        show: true,
        position: 'top',
        // formatter: function(params) {
        //     data = params.data;
        //     return 'Swimmer';
        // }
        formatter: '{b}: {c}'
    },
    // legend: {
    //     data: ['Swimmers']
    // },
    xAxis: [{
        type: 'value',
        splitNumber: 1,
        scale: true,
        min: 0,
        max: 100
    }],
    yAxis: [{
        type: 'value',
        splitNumber: 4,
        scale: true,
        min: 0,
        max: 50
    }],
    animation: false,
    series: [{
        name: 'Swimmers',
        type: 'scatter',
        symbol: 'image://static/img/male_small.png',
        symbolSize: function(value) {
            if (value[0] < 0 || value[1] < 0) {
                return 0;
            }
            if (value && value[3]) {
                return [18,36];
            }
            return [18,36];
        },
        data: swimmings,
        itemStyle: {
            normal: {
                // color: '#4a86e8',
                label:
                {
                    show:true,
                    position: 'top',
                    formatter: function(params) {
                        data = params.data;
                        return data[4];
                    },
                    textStyle:{
                        color:'#000',
                        fontSize: 20
                    }
                }
            },
            emphasis:{
                label:{show:true}
            }
        }
    },
    {
        name: 'Drowning',
        type: 'scatter',
        symbolSize: function(value) {
            if (value[0] < 0 || value[1] < 0) {
                return 0;
            }
            if (value && value[3]) {
                return 15;
            }
            return 25;
        },
        data: drownings,
        label: {
            normal:{
                show: true,
                position: 'top',
                formatter: function(params) {
                    data = params.data;
                    return data[4];
                }
            }
        },
        itemStyle: {
            normal: {
                color: '#ff0000',
                
            },
            emphasis:{
                label:{show:true}
            },
            showEffectOn: 'render',
            rippleEffect: {
                brushType: 'stroke'
            },
            hoverAnimation: true,
            zlevel: 1,
        }
    }   
    ]
};
myChart.setOption(option);

setInterval(function() {
    $.ajax({
        url: "/swimmer_status",
        success: function(data) {
            updateChart(data);
        }
    });
}, 2000)

function updateChart(data) {
    swimmings = initDataArray(swimmings);
    drownings = initDataArray(drownings);
    var swimmers = JSON.parse(data);
    var sw = swimmers.swimming;
    var dr = swimmers.drowning;
    for (var i = 0; i < sw.length; i++) {
        var s = sw[i];
        var id = parseInt(s.sid);
        var x = parseInt(s.x);
        var y = parseInt(s.y);
        var hr = parseInt(s.hr);
        var stp = s.swimming_by_self;
        var name = s.name;
        swimmings[id][0] = x;
        swimmings[id][1] = y;
        swimmings[id][2] = hr;
        swimmings[id][3] = swimming_by_self;
        swimmings[id][4] = name;
    }
    option.series[0].data = swimmings;
    for (var i = 0; i < dr.length; i++) {
        var s = dr[i];
        var id = parseInt(s.sid);
        var x = parseInt(s.x);
        var y = parseInt(s.y);
        var hr = parseInt(s.hr);
        var swimming_by_self = s.swimming_by_self;
        var name = s.name;
        drownings[id][0] = x;
        drownings[id][1] = y;
        drownings[id][2] = hr;
        drownings[id][3] = swimming_by_self;
        drownings[id][4] = name;
    }
    option.series[1].data = drownings;
    myChart.setOption(option);
}

function onstart() {
    $.ajax({
        url: "/start_moving",
        success: function(data) {
            return;
        }
    });
}

function onstop() {
    $.ajax({
        url: "/stop_moving",
        success: function(data) {
            return;
        }
    });
}
