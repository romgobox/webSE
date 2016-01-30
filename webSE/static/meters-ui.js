////////////////////////////////////////////////////////////////////////////////
// UI elements
////////////////////////////////////////////////////////////////////////////////

// Dialogs
function addMeterDialog(meters) {
    var meters = meters;
    var html = '';
    html += '<table id="wh_add" class="table table-bordered table-hover">';
    html += '<tr><td>Описание</td><td><input id="wh_desc" type="text" value=""></td></tr>';
    html += '<tr><td>Номер</td><td><input id="wh_num" type="text" value=""></td></tr>';
    html += '<tr><td>Адрес</td><td><input id="wh_adr" type="text" value=""></td></tr>';
    html += '<tr><td>Профиль глубина</td><td><input id="ppValue" type="text" value=""></tr>';
    html += '<tr><td>Показания глубина</td><td><input id="fixDay" type="text" value=""></td></tr>';
    html += '<tr><td>Канал учета</td><td><input id="channel_id" type="text" value=""></td></tr>';
    html += '</table>';
    function collectValues(tableID) {
        var result = {};
        result['wh_desc'] = $(tableID).find("#wh_desc").val();
        result['wh_num'] = $(tableID).find("#wh_num").val();
        result['wh_adr'] = $(tableID).find("#wh_adr").val();
        var ppV = $(tableID).find("#ppValue").val();
        var fixD = $(tableID).find("#fixDay").val();
        result['wh_settings'] = {fixDay:{depth:fixD}, ppValue:{depth:ppV}};
        result['channel_id'] = $(tableID).find("#channel_id").val();
        return result;
    }
    $("#wh_add_dialog").html(html);
    $("#wh_add_dialog").dialog({
        title: 'Добавление прибора учета',
        height: 470,
        width: 450,
        modal: true,
        resizable: true,
        buttons: [
            {
                text: "Ok",
                icons: {
                    primary: "ui-icon-circle-plus"
                },
            click: function () {
                    var tableID = $("#wh_add");
                    var params = collectValues(tableID);
                    meters.addNewMeter(params);
                    $(this).dialog("close");
                }
            }
          ]
    });
}

function editMeterDialog(meter) {
    var self = meter;
    var html = '';
    html += '<table id="wh_edit_'+self.id+'" class="table table-bordered table-hover">';
    html += '<tr><td>#ID</td><td id="wh_edit_id">'+self.id+'</td></tr>';
    html += '<tr><td>Описание</td><td><input id="wh_desc" type="text" value="'+self.wh_desc+'"></td></tr>';
    html += '<tr><td>Номер</td><td><input id="wh_num" type="text" value="'+self.wh_num+'"></td></tr>';
    html += '<tr><td>Адрес</td><td><input id="wh_adr" type="text" value="'+self.wh_adr+'"></td></tr>';
    html += '<tr><td>Профиль глубина</td><td><input id="ppValue" type="text" value="'+self.ppValue+'"></tr>';
    html += '<tr><td>Показания глубина</td><td><input id="fixDay" type="text" value="'+self.fixDay+'"></td></tr>';
    html += '<tr><td>Канал учета</td><td><input id="channel_id" type="text" value="'+self.channel_id+'"></td></tr>';
    html += '</table>';
    function collectValues(tableID) {
        var result = {};
        result['id'] = self.id;
        result['wh_desc'] = $(tableID).find("#wh_desc").val();
        result['wh_num'] = $(tableID).find("#wh_num").val();
        result['wh_adr'] = $(tableID).find("#wh_adr").val();
        var ppV = $(tableID).find("#ppValue").val();
        var fixD = $(tableID).find("#fixDay").val();
        result['wh_settings'] = {fixDay:{depth:fixD}, ppValue:{depth:ppV}};
        result['channel_id'] = $(tableID).find("#channel_id").val();
        return result;
    }
    $("#wh_edit_dialog").html(html);
    $("#wh_edit_dialog").dialog({
        title: 'Редактирование прибора учета',
        height: 470,
        width: 450,
        modal: true,
        resizable: true,
        buttons: [
            {
                text: "Ok",
                icons: {
                    primary: "ui-icon-circle-plus"
                },
            click: function () {
                    var tableID = $("#wh_edit_"+self.id);
                    var params = collectValues(tableID);
                    self.saveParams(params);
                    $(this).dialog("close");
                }
            }
          ]
    });
}

function delMeterDialog(meter, meters) {
    var meters = meters;
    var meter = meter;
    var html = '';
    html += '<h4>Вы уверены, что хотите удалить прибор учета?</h4>'
    html += '<table id="wh_del" class="table table-bordered table-hover">';
    html += '<tr><th>#ID</th><th>Номер</th></tr>';
    html += '<tr><td>'+meter.id+'</td><td>'+meter.wh_num+'</td></tr>';
    html += '</table>';
    $("#wh_delete_dialog").html(html);
    $("#wh_delete_dialog").dialog({
        title: 'Удаление прибора учета',
        height: 300,
        width: 450,
        modal: true,
        resizable: true,
        buttons: [
            {
                text: "Да",
                icons: {
                    primary: "ui-icon-circle-plus"
                },
                click: function () {
                    meters.deleteMeter(meter.id)
                    $(this).dialog("close");
                }
            },
            {
                text: "Отмена",
                icons: {
                    primary: "ui-icon-circle-plus"
                },
                click: function () {
                    $(this).dialog("close");
                }
            }
          ]
    });
}

function meterTR(meter) {
    var html = '';
    html += '<tr id="wh_'+meter.id+'"><td>'+meter.id+'</td>';
    html += '<td id="wh_desc">'+meter.wh_desc+'</td>';
    html += '<td id="wh_num">'+meter.wh_num+'</td>';
    html += '<td id="wh_adr">'+meter.wh_adr+'</td>';
    html += '<td id="wh_settings">Профиль глубина: <span id="ppValue">' + meter.ppValue + '</span><br>';
    html += 'Показания глубина: <span id="fixDay">'+meter.fixDay+'</span></td>';
    html += '<td id="channel_id">'+meter.channel_id+'</td>';
    html += '<td align="center"><div class="btn-group">';
    html += '<button class="edit_info_wh btn btn-primary btn-sm" wh_id="'+meter.id+'" >';
    html += '<span class="glyphicon glyphicon-pencil"></span> Редактировать</button>';
    html += '<button class="delete_wh btn btn-danger btn-sm" wh_id="'+meter.id+'" >';
    html += '<span class="glyphicon glyphicon-trash"></span> Удалить</button></div></td></tr>'
    return html;
}