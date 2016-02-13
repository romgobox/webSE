////////////////////////////////////////////////////////////////////////////////
// UI elements
////////////////////////////////////////////////////////////////////////////////
function renderReportsUI() {
    html = '<div class="panel panel-default">';
    html += '<div class="row">';
    html += '<div class="col-md-12">';
    html += '<div id="reports_menu" class="panel-body">';
    html += '<button class="fixday_report btn btn-info">Зафиксированные показания</button> ';
    html += '<button class="fixday_diff_report btn btn-info">Расход за период</button> ';
    html += '<button class="ppvalue_report btn btn-info">Профиль мощности</button> ';
    html += '</div></div></div></div>';
    html += '<div id="report_content"></div>';
    $("#content").html(html);
}
////////////////////////////////////////////////////////////////////////////////
// Dialogs
////////////////////////////////////////////////////////////////////////////////()
function metersSelectByObject(meters) {
    var meters = meters['meters'];
    var obj_id = parseInt($("#select_object").val());
    var wh_list = '';
    for (var i = 0; i < meters.length; i++) {
        if (meters[i]['object_id']['id'] == obj_id) {
            wh_list += '<option value="'+meters[i]['id']+'">'+meters[i]['wh_desc']+' - '+meters[i]['wh_num']+'</option>'
        }
    };
    $("#select_meter").html(wh_list);
}
function ReportByMeterIDDialog(meters, param_num, reportType) {
    var reportType = reportType;
    var param_num = param_num;
    var objects = meters['objects'];
    var meters = meters;
    var html = '';
    html += '<table id="report_table" class="table table-bordered table-hover">';
    html += '<tr><td>Выберете объект</td>';
    html += '<td><select id="select_object">';
    html += '<option value="0"> --- </option>';
    for (obj in objects) {
        html += '<option value="'+objects[obj]['id']+'">'+objects[obj]['obj_desc']+'</option>';
    };
    html += '</select></td></tr>';
    html += '<tr><td>Выберете прибор учета</td>';
    html += '<td><select id="select_meter">';
    html += '<option value="0"> --- </option>';
    html += '</select></td></tr>';
    html += '<tr><td>Дата начала: </td><td><input type="text" class="datepicker" id="date_start"></td></tr>';
    html += '<tr><td>Дата окончания: </td><td><input type="text" class="datepicker" id="date_end"></td></tr>';
    html += '</table>';
    function collectValues(tableID) {
        var result = {};
        result['wh_id'] = parseInt($(tableID).find("#select_meter").val());
        result['meter'] = meters.returnMeter(result['wh_id']);
        result['param_num'] = param_num;
        result['report_type'] = reportType;
        result['date_start'] = $(tableID).find("#date_start").val() + ' 00:00:00';
        result['date_end'] = $(tableID).find("#date_end").val() + ' 00:00:00';
        return result;
    }
    $("#fixday-report-dialog").html(html);
    $("#fixday-report-dialog").dialog({
        title: 'Выберете прибор учета и даты',
        height: 600,
        width: 500,
        modal: true,
        resizable: true,
        buttons: [
            {
                text: "Ok",
                icons: {
                    primary: "ui-icon-circle-plus"
                },
            click: function () {
                    var tableID = $("#report_table");
                    var params = collectValues(tableID);
                    getReportByMeterID(params);
                    $(this).dialog("close");
                }
            }
          ]
    });

}

////////////////////////////////////////////////////////////////////////////////
// Reports Tables
////////////////////////////////////////////////////////////////////////////////
function renderReportTable(data, meter, reportType) {
    var meter = meter;
    var reportType = reportType;
    var html = '';
    if (reportType == 'dates_list') {
        html += '<p>Прибор учета: '+meter['object_id']['obj_desc']+' '+meter['wh_desc']+' '+meter['wh_num']+'</p>'
        html += '<table class="table table-bordered table-hover">';
        html += '<tr><th>Дата</th><th>Значение</th>';
        for (var i = 0; i < data.length; i++) {
            html += '<tr><td>'+data[i]['datetime_value']+'</td><td>'+data[i]['value']+'</td></tr>'
        }
        html += '</table>';
    }
    else if (reportType == 'dates_diff') {
        html += '<p>Прибор учета: '+meter['object_id']['obj_desc']+' '+meter['wh_desc']+' '+meter['wh_num']+'</p>'
        html += '<table class="table table-bordered table-hover">';
        html += '<tr>';
        html += '<th>Показания на '+data[0]['datetime_value']+'</th>';
        html += '<th>Показания на '+data[1]['datetime_value']+'</th>';
        html += '<th>Расход</th>';
        html += '</tr>';
        html += '<tr>';
        html += '<td>'+data[0]['value']+'</td>';
        html += '<td>'+data[1]['value']+'</td>';
        var diff = data[1]['value'] - data[0]['value'];
        html += '<td>'+diff+'</td>';
        html += '</tr>';
        html += '</table>';
    }
    $("#report_content").html(html);
}
