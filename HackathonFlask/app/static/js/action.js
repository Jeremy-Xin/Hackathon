var myChart = echarts.init(document.getElementById('main'));

function random() {
    var r = Math.round(Math.random() * 100);
    return r;
}

var arr = [];
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
arr = initDataArray(arr);


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
    legend: {
        data: ['Swimmers']
    },
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
        symbolSize: function(value) {
            if (value[0] < 0 || value[1] < 0) {
                return 0;
            }
            if (value && value[3]) {
                return 20;
            }
            return 12;
        },
        data: arr,
        itemStyle: {
            normal: {
                color: '#4a86e8',
                // shadowBlur: 10,
                // shadowColor: '#333'
            }
        }
    }]
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
    var swimmers = JSON.parse(data);
    for (var i = 0; i < swimmers.length; i++) {
        var s = swimmers[i];
        var id = parseInt(s.sid);
        var x = parseInt(s.x);
        var y = parseInt(s.y);
        var hb = parseInt(s.hb);
        var stp = s.stop;
        option.series[0].data[id][0] = x;
        option.series[0].data[id][1] = y;
        option.series[0].data[id][2] = hb;
        option.series[0].data[id][3] = stp;
    }
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
