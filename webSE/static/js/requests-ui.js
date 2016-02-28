////////////////////////////////////////////////////////////////////////////////
// UI elements
////////////////////////////////////////////////////////////////////////////////
function renderRequestsUI() {
    if ($("#requests_ui").is(":hidden")) {
        $("#meters_ui").hide();
        $("#reports_ui").hide();
        $("#requests_ui").show();
        $("#user_ui").hide();
    }
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
function requestByChannelsDialog(meters, reply) {
    var reply = reply || false;
    var meters = meters;
    var html = '';
    html += '<table id="channels_check" class="table table-bordered table-hover">';
    for (var i in meters.channels) {
        var channel = meters.channels[i]
        if (channel.is_active == 1) {
            html += '<tr>';
            html += '<td><input type="checkbox" checked value='+channel['id']+'></td>'
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
        result['reply'] = reply;
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
                    var channels = result['channels'];
                    if (channels.length) {
                        var busy_channels = '';
                        var free_channels = [];
                        for (var id in channels) {
                            var channel = meters.returnChannel(channels[id]);
                            channel.getStatus();
                            var code = channel.status_code;
                            if (code==1 || code==2 || code==3) {
                                busy_channels += '<br>'+channel['ch_desc'];
                            }
                            else {
                                free_channels.push(channels[id]);
                            }
                        }
                        if (busy_channels != '') {
                            showChannelsStatusDialog('warning', 'Канал(ы) занят(ы):'+busy_channels, 'Канал(ы) занят(ы)!');
                        }
                        if (free_channels.length) {
                            result['channels'] = free_channels;
                            getRequestByChannel(result);
                            $('#waiting').show();
                            showStatusDialog('info', 'Задание на опрос отправлено в очередь', 'Информация');
                        }
                        $(this).dialog("close");
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
    $("#request_content").html('');
    var data = data;
    var meters = window.meters;
    for (var i in data) {
        for (var j in data[i]) {

            var meter = meters.returnMeter(data[i][j]['id']);
            
            var meterTable = '<table id="meter_table_'+meter.id+'" class="table table-bordered table-hover">';
            meterTable += '<tr><th>'+meter['wh_desc']+' '+meter['wh_num']+'</th>';
            meterTable += '<th>';
            meterTable += '<button class="fixday_show_btn btn btn-primary btn-sm" wh_id="'+meter.id+'" >Зафиксированные показания</button>';
            meterTable += '<button class="ppvalue_show_btn btn btn-primary btn-sm" wh_id="'+meter.id+'" >Профиль мощности</button>';
            meterTable += '</th></tr></table>';

            var htmlFixdayTable = '<table hidden id="fixday_values_table_'+meter.id+'" class="table table-bordered table-hover">';
            htmlFixdayTable += '<tr><th>Дата</th><th>Значение</th></tr>';
            htmlFixdayTable += '</table>';

            var htmlPPValueTable = '<table hidden id="pp_values_table_'+meter.id+'" class="table table-bordered table-hover">';
            htmlPPValueTable += '<tr><th>Дата</th><th>Значение</th></tr>';
            htmlPPValueTable += '</table>';

            $("#request_content").append(meterTable);
            $("#request_content").append(htmlFixdayTable);
            $("#request_content").append(htmlPPValueTable);
    
            var fixDayTable = $('#fixday_values_table_'+meter.id);
            var ppValueTable = $('#pp_values_table_'+meter.id);

            var fixDayHtml = '';
            var ppValueHtml = '';

            var ppv_dates = [];
            for (var date in data[i][j]['ppValue']) {
                ppv_dates.push(date);
            }
            var fd_dates = [];
            for (var date in data[i][j]['fixDay']) {
                fd_dates.push(date);
            }

            ppv_dates.sort(function(a,b){
                var date1 = new Date(a.substr(0, 4), a.substr(5, 2)-1, a.substr(8, 2), a.substr(11, 2), a.substr(14, 2), a.substr(17, 2));
                var date2 = new Date(b.substr(0, 4), b.substr(5, 2)-1, b.substr(8, 2), b.substr(11, 2), b.substr(14, 2), b.substr(17, 2));
                return date1-date2;
            });
            fd_dates.sort(function(a,b){
                var date1 = new Date(a.substr(0, 4), a.substr(5, 2)-1, a.substr(8, 2), a.substr(11, 2), a.substr(14, 2), a.substr(17, 2));
                var date2 = new Date(b.substr(0, 4), b.substr(5, 2)-1, b.substr(8, 2), b.substr(11, 2), b.substr(14, 2), b.substr(17, 2));
                return date1-date2;
            });

            for (var date in fd_dates) {
                var value = data[i][j]['fixDay'][fd_dates[date]];
                var date = fd_dates[date];
                fixDayHtml += '<tr>';
                fixDayHtml += '<td>'+date+'</td><td>';
                fixDayHtml += '<ul>';
                fixDayHtml += '<li>Сумма: '+value['Sum']+'</li>';
                fixDayHtml += '<li>T1: '+value['T1']+'</li>';
                fixDayHtml += '<li>T2: '+value['T2']+'</li>';
                fixDayHtml += '</ul>';
                fixDayHtml += '</td>';
                fixDayHtml += '</tr>';
            }

            for (var date in ppv_dates) {
                var value = data[i][j]['ppValue'][ppv_dates[date]];
                var date = ppv_dates[date];
                ppValueHtml += '<tr>';
                ppValueHtml += '<td>'+date+'</td><td>'+value+'</td>';
                ppValueHtml += '</tr>';
            }

            fixDayTable.append(fixDayHtml);
            ppValueTable.append(ppValueHtml);
        }
    }
    $("#request_content").on('click', '.fixday_show_btn', function (e){
        e.stopImmediatePropagation();
        var wh_id = $(this).attr('wh_id');
        if ($("#fixday_values_table_"+wh_id).is(":hidden")) {
            $("#fixday_values_table_"+wh_id).show();
        }
        else {
            $("#fixday_values_table_"+wh_id).hide();
        }
        // $(this).off('click');
    });

    $("#request_content").on('click', '.ppvalue_show_btn', function (e){
        e.stopImmediatePropagation();
        var wh_id = $(this).attr('wh_id');
        if ($("#pp_values_table_"+wh_id).is(":hidden")) {
            $("#pp_values_table_"+wh_id).show();
        }
        else {
            $("#pp_values_table_"+wh_id).hide();
        }
        // $(this).off('click');
    });
}
