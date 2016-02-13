////////////////////////////////////////////////////////////////////////////////
// UI elements
////////////////////////////////////////////////////////////////////////////////
function renderRequestsUI() {
    html = '<div class="panel panel-default">';
    html += '<div class="row">';
    html += '<div class="col-md-12">';
    html += '<div id="requests_menu" class="panel-body">';
    html += '<button class="channels_requests btn btn-info">Опрос по каналам</button> ';
    html += '</div></div></div></div>';
    html += '<div id="request_content"></div>';
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
function requestByChannelsDialog(meters) {
    var meters = meters;
    var html = '';
    html += '<table id="channels_check" class="table table-bordered table-hover">';
    for (var i in meters.channels) {
        var channel = meters.channels[i]
        if (channel.is_activ == 1) {
            html += '<tr>';
            html += '<td><input type="checkbox" value='+channel['id']+'></td>'
            html += '<td>'+channel['ch_desc']+' [ '+channel['ch_ip']+':'+channel['ch_port']+' ]</td>';
            html += '</td>';
        }
    }
    html += '</div>';
    function collectValues(tableID) {
        var channels = [];
        var result = {};
        $('#channels_check input[type="checkbox"]:checked').each(function() { 
            channels.push(parseInt($(this).val()));
        });
        result['channels'] = channels;
        result['alg_type'] = 'full';
        return result;
    }
    $("#request_by_channels_dialog").html(html);
    $("#request_by_channels_dialog").dialog({
        title: 'Выберете каналы для опроса',
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
                    var tableID = $("#channels_check");
                    var result = collectValues(tableID);
                    if (result['channels'].length) {
                        getRequestByChannel(result);
                        $(this).dialog("close");
                        $('#waiting').show();
                    }
                    else {
                        alert("Нужно выбрать хотя бы один канал");
                    }
                }
            }
          ]
    });

}

////////////////////////////////////////////////////////////////////////////////
// Requests Tables
////////////////////////////////////////////////////////////////////////////////
function renderRequestTable(data) {
    var data = data;
    var htmlFixdayTable = '<h4>Зафиксированные показания: </h4>';
    htmlFixdayTable += '<table id="fixday_values_table" class="table table-bordered table-hover">';
    htmlFixdayTable += '<tr><th>Дата</th><th>Значение</th>';
    htmlFixdayTable += '</table>';

    var htmlPPValueTable = '<h4>Профиль мощности: </h4>';
    htmlPPValueTable += '<table id="pp_values_table" class="table table-bordered table-hover">';
    htmlPPValueTable += '<tr><th>Дата</th><th>Значение</th>';
    htmlPPValueTable += '</table>';

    $("#request_content").append(htmlFixdayTable);
    $("#request_content").append(htmlPPValueTable);

    var fixDayTable = $('#fixday_values_table');
    var ppValueTable = $('#pp_values_table');

    var fixDayHtml = '';
    var ppValueHtml = '';
    for (var i in data) {
        for (var date in data[i]['fixDay']) {
            var value = data[i]['fixDay'][date];
            fixDayHtml += '<tr>';
            fixDayHtml += '<td>'+date+'</td><td>'+value+'</td>';
            fixDayHtml += '</tr>';
        }
        for (var date in data[i]['ppValue']) {
            var value = data[i]['ppValue'][date];
            ppValueHtml += '<tr>';
            ppValueHtml += '<td>'+date+'</td><td>'+value+'</td>';
            ppValueHtml += '</tr>';
        }
    }
    fixDayTable.append(fixDayHtml);
    ppValueTable.append(ppValueHtml);
    
}
