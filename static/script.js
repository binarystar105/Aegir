//================================================

let $PH_Btn = $("#PH-btn"),
    $PH_low = $("#PH-low"),
    $PH_high = $("#PH-high");

$PH_Btn.on('click', function() {
    let PH_low = $PH_low.val(),
        PH_high = $PH_high.val();

    if (PH_high<PH_low) {
        alert('Could not Update. PH HIGH should be >= PH LOW');
    }
    else {
        $.ajax({
            type: 'POST',
            url: '/api/PH',
            data: {
                PH_low,
                PH_high
            },
            success: function(res) {
                console.log(res);
                if (res) {
                    alert('PH Thresholds updated successfuly!');
                } else {
                    alert('Error. Fields must not be empty');
                }
            }
        })
    }


});

//================================================

let $DO_Btn = $("#DO-btn"),
    $DO_low = $("#DO-low"),
    $DO_high = $("#DO-high");

$DO_Btn.on('click', function() {
    let DO_low = $DO_low.val(),
        DO_high = $DO_high.val();

    if (DO_high<DO_low) {
        alert('Could not Update. DO HIGH should be >= DO LOW');
    }
    else {
        $.ajax({
            type: 'POST',
            url: '/api/DO',
            data: {
                DO_low,
                DO_high
            },
            success: function(res) {
                console.log(res);
                if (res) {
                    alert('DO Thresholds updated successfuly!');
                } else {
                    alert('Error. Fields must not be empty');
                }
            }
        })
    }
});

//================================================

let $TMP_Btn = $("#TMP-btn"),
    $TMP_low = $("#TMP-low"),
    $TMP_high = $("#TMP-high");

$TMP_Btn.on('click', function() {
    let TMP_low = $TMP_low.val(),
        TMP_high = $TMP_high.val();

    if (TMP_high<TMP_low) {
        alert('Could not Update. TMP HIGH should be >= TMP LOW');
    }
    else {        
        $.ajax({
            type: 'POST',
            url: '/api/TMP',
            data: {
                TMP_low,
                TMP_high
            },
            success: function(res) {
                console.log(res);
                if (res) {
                    alert('TMP Thresholds updated successfuly!');
                } else {
                    alert('Error. Fields must not be empty');
                }
            }
        })
    }
});

//================================================

let $Stop_Btn = $("#Stop-btn");

$Stop_Btn.on('click', function() {
    let x = 1,
        y = 1;

    $.ajax({
        type: 'POST',
        url: '/api/shutdown',
        data: {
            x,
            y
        },
        success: function(res) {
            console.log(res);
            if (res) {
                alert('Server shudown successfuly!');
            } else {
                alert('error');
            }
        }
    })
});

//================================================

var id = setInterval(function() {
    let x = 1,
        y = 1;

    $.ajax({
        type: 'POST',
        url: '/api/cur_vals',
        data: {
            x,
            y
        },
        success: function(res) {
            var PH = res.PH_cur_val;
            var DO = res.DO_cur_val;
            var TMP = res.TMP_cur_val;
            $("#PH_value").text(PH);
            $("#DO_value").text(DO);
            $("#TMP_value").text(TMP);

            data.addRow([getCurrentTime(), PH, DO + 1, TMP + 2]);
            chart.draw(data, options);
        }
    })
}, 5000); // Read sensor value every x milliseconds

//================================================

var data,
    options,
    chart;

$(document).ready(function() {
    google.charts.load('current', {
        'packages': ['corechart']
    });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        data = google.visualization.arrayToDataTable([
            ['Year', 'PH', 'DO', 'TMP'],
            ['00:00', 0, 0, 0]
        ]);

        options = {
            title: 'Historical Data',
            curveType: 'function',
            legend: {
                position: 'bottom'
            }
        };

        // chart = new google.visualization.LineChart(document.getElementById('chart'));
        chart = new google.visualization.AreaChart(document.getElementById('chart'));

        chart.draw(data, options);
    }
});

function addZero(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

function getCurrentTime() {
    var d = new Date();
    var h = addZero(d.getHours());
    var m = addZero(d.getMinutes());
    // var s = addZero(d.getSeconds());
    var hh_mm = h + ":" + m;
    return hh_mm.toString();
}

//================================================

// Set NumPad defaults for jQuery mobile. 
// These defaults will be applied to all NumPads within this document!
$.fn.numpad.defaults.gridTpl = '<table class="table modal-content"></table>';
$.fn.numpad.defaults.backgroundTpl = '<div class="modal-backdrop in"></div>';
$.fn.numpad.defaults.displayTpl = '<input type="text" class="form-control" />';
$.fn.numpad.defaults.buttonNumberTpl = '<button type="button" class="btn btn-default" style="width: 100%;"></button>';
$.fn.numpad.defaults.buttonFunctionTpl = '<button type="button" class="btn btn-default" style="width: 100%;"></button>';
$.fn.numpad.defaults.onKeypadCreate = function() {
    $(this).find('.done').addClass('btn-primary');
};

$(".trigger-num").numpad({
    decimalSeparator: '.'
});