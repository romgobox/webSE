////////////////////////////////////////////////////////////////////////////////
// UI elements
////////////////////////////////////////////////////////////////////////////////
function renderMetersUI() {
    if ($("#meters_ui").is(":hidden")) {
        $("#meters_ui").show();
        $("#reports_ui").hide();
        $("#requests_ui").hide();
    }
}
////////////////////////////////////////////////////////////////////////////////
// Dialogs
////////////////////////////////////////////////////////////////////////////////
function showStatusDialog(status, data, title) {
    var status = status || 'success';
    var data = data || 'Что-то произошло, а что непонятно!';
    var title = title || 'Добавлен прибора учета';
    html = '<div class="alert alert-'+status+'">'+data+'</div>'
    $("#status_dialog").html(html);
    $("#status_dialog").dialog({
        title: title,
        height: 200,
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
                    $(this).dialog("close");
                }
            }
          ]
    });
}

function showChannelsStatusDialog(status, data, title) {
    var status = status || 'success';
    var data = data || 'Что-то произошло, а что непонятно!';
    var title = title || 'Добавлен прибора учета';
    html = '<div class="alert alert-'+status+'">'+data+'</div>'
    $("#channel_status_dialog").html(html);
    $("#channel_status_dialog").dialog({
        title: title,
        height: 200,
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
                    $(this).dialog("close");
                }
            }
          ]
    });
}

////////////////////////////////////////////////////////////////////////////////
// Meters dialogs
////////////////////////////////////////////////////////////////////////////////
function addMeterDialog(meters) {
    var meters = meters;
    var html = '';
    html += '<table id="wh_add" class="table table-bordered table-hover">';
    html += '<tr><td>Объект</td><td><select id="object_id">';
    for (var obj in meters.objects) {
        html += '<option value="'+meters.objects[obj].id+'">'+meters.objects[obj].obj_desc+'</option>'
    };
    html += '</select></td></tr>';
    html += '<tr><td>Описание</td><td><input id="wh_desc" type="text" value=""></td></tr>';
    html += '<tr><td>Тип</td><td><select id="type_id">';
    for (var type in meters.meters_type) {
        html += '<option value="'+meters.meters_type[type].id+'">'+meters.meters_type[type].type+'</option>'
    };
    html += '</select></td></tr>';
    html += '<tr><td>Номер</td><td><input id="wh_num" type="text" value=""></td></tr>';
    html += '<tr><td>Адрес</td><td><input id="wh_adr" type="text" value=""></td></tr>';
    html += '<tr><td>Пароль</td><td><input id="wh_pass" type="text" value=""></td></tr>';
    html += '<tr><td>К-т трансформации тока</td><td><input id="wh_KI" type="text" value="1"></td></tr>';
    html += '<tr><td>К-т трансформации напряжения</td><td><input id="wh_KU" type="text" value="1"></td></tr>';
    html += '<tr><td>Кол-во импульсов</td><td><input id="wh_IMPL" type="text" value="1"></td></tr>';
    html += '<tr><td>Профиль глубина</td><td><input id="ppValue" type="text" value="1"></tr>';
    html += '<tr><td>Показания глубина</td><td><input id="fixDay" type="text" value="1"></td></tr>';
    html += '<tr><td>Канал опроса</td><td><select id="channel_id">';
    for (var ch in meters.channels) {
        html += '<option value="'+meters.channels[ch].id+'">'+meters.channels[ch].ch_desc+'</option>'
    };
    html += '</select></td></tr>';
    html += '<tr><td>Активен</td><td><select id="is_active">';
    html += '<option value="1">Да</option>';
    html += '<option value="0">Нет</option>';
    html += '</td></tr>';
    html += '</table>';
    function collectValues(tableID) {
        var result = {};
        result['object_id'] = $(tableID).find("#object_id").val();
        result['wh_desc'] = $(tableID).find("#wh_desc").val();
        result['type_id'] = $(tableID).find("#type_id").val();
        result['wh_num'] = $(tableID).find("#wh_num").val();
        result['wh_adr'] = $(tableID).find("#wh_adr").val();
        result['wh_pass'] = $(tableID).find("#wh_pass").val();
        result['wh_KI'] = $(tableID).find("#wh_KI").val();
        result['wh_KU'] = $(tableID).find("#wh_KU").val();
        result['wh_IMPL'] = $(tableID).find("#wh_IMPL").val();
        var ppV = $(tableID).find("#ppValue").val();
        var fixD = $(tableID).find("#fixDay").val();
        result['wh_settings'] = {fixDay:fixD, ppValue:ppV};
        result['channel_id'] = $(tableID).find("#channel_id").val();
        result['is_active'] = $(tableID).find("#is_active").val();
        return result;
    }
    $("#wh_add_dialog").html(html);
    $("#wh_add_dialog").dialog({
        title: 'Добавление прибора учета',
        height: 560,
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

function editMeterDialog(meter, meters) {
    var self = meter;
    var meters = meters;
    var html = '';
    html += '<table id="wh_edit_'+self.id+'" class="table table-bordered table-hover">';
    html += '<tr><td>Объект</td><td><select id="object_id">';
    for (var obj in meters.objects) {
        if (self.object_id.id === meters.objects[obj].id) {
            html += '<option selected value="'+meters.objects[obj].id+'">'+meters.objects[obj].obj_desc+'</option>';  
        }
        else {
            html += '<option value="'+meters.objects[obj].id+'">'+meters.objects[obj].obj_desc+'</option>';
        }
    };
    html += '</select></td></tr>';
    html += '<tr><td>Описание</td><td><input id="wh_desc" type="text" value="'+self.wh_desc+'"></td></tr>';
    html += '<tr><td>Тип</td><td><select id="type_id">';
    for (var type in meters.meters_type) {
        if (self.type_id.id === meters.meters_type[type].id) {
            html += '<option selected value="'+meters.meters_type[type].id+'">'+meters.meters_type[type].type+'</option>';  
        }
        else {
            html += '<option value="'+meters.meters_type[type].id+'">'+meters.meters_type[type].type+'</option>';
        }
    };
    html += '</select></td></tr>';
    html += '</select></td></tr>';
    html += '<tr><td>Номер</td><td><input id="wh_num" type="text" value="'+self.wh_num+'"></td></tr>';
    html += '<tr><td>Адрес</td><td><input id="wh_adr" type="text" value="'+self.wh_adr+'"></td></tr>';
    html += '<tr><td>Пароль</td><td><input id="wh_pass" type="text" value="'+self.wh_pass+'"></td></tr>';
    html += '<tr><td>К-т трансформации тока</td><td><input id="wh_KI" type="text" value="'+self.wh_KI+'"></td></tr>';
    html += '<tr><td>К-т трансформации напряжения</td><td><input id="wh_KU" type="text" value="'+self.wh_KU+'"></td></tr>';
    html += '<tr><td>Кол-во импульсов</td><td><input id="wh_IMPL" type="text" value="'+self.wh_IMPL+'"></td></tr>';
    html += '<tr><td>Профиль глубина</td><td><input id="ppValue" type="text" value="'+self.ppValue+'"></tr>';
    html += '<tr><td>Показания глубина</td><td><input id="fixDay" type="text" value="'+self.fixDay+'"></td></tr>';
    html += '<tr><td>Канал опроса</td><td><select id="channel_id">';
    for (var ch in meters.channels) {
        if (self.channel_id.id === meters.channels[ch].id) {
            html += '<option selected value="'+meters.channels[ch].id+'">'+meters.channels[ch].ch_desc+'</option>'
        }
        else {
            html += '<option value="'+meters.channels[ch].id+'">'+meters.channels[ch].ch_desc+'</option>'
        }
    };
    html += '</select></td></tr>';
    html += '<tr><td>Активен</td><td><select id="is_active">';
    if (self.is_active == 1) {
        html += '<option selected value="1">Да</option>';
        html += '<option value="0">Нет</option>';
    }
    else if (self.is_active == 0) {
        html += '<option value="1">Да</option>';
        html += '<option selected value="0">Нет</option>';
    }
    else {
        html += '<option value="1">Да</option>';
        html += '<option value="0">Нет</option>';
    }
    
    html += '</td></tr>';
    html += '</table>';
    function collectValues(tableID) {
        var result = {};
        result['id'] = self.id;
        result['object_id'] = $(tableID).find("#object_id").val();
        result['wh_desc'] = $(tableID).find("#wh_desc").val();
        result['type_id'] = $(tableID).find("#type_id").val();
        result['wh_num'] = $(tableID).find("#wh_num").val();
        result['wh_adr'] = $(tableID).find("#wh_adr").val();
        result['wh_pass'] = $(tableID).find("#wh_pass").val();
        result['wh_KI'] = $(tableID).find("#wh_KI").val();
        result['wh_KU'] = $(tableID).find("#wh_KU").val();
        result['wh_IMPL'] = $(tableID).find("#wh_IMPL").val();
        var ppV = $(tableID).find("#ppValue").val();
        var fixD = $(tableID).find("#fixDay").val();
        result['wh_settings'] = {fixDay:fixD, ppValue:ppV};
        result['channel_id'] = $(tableID).find("#channel_id").val();
        result['is_active'] = $(tableID).find("#is_active").val();
        return result;
    }
    $("#wh_edit_dialog").html(html);
    $("#wh_edit_dialog").dialog({
        title: 'Редактирование прибора учета',
        height: 560,
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
                    self.saveParams(params, meters);
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

////////////////////////////////////////////////////////////////////////////////
// Channels dialogs
////////////////////////////////////////////////////////////////////////////////
function addChannelDialog(meters) {
    var meters = meters;
    var html = '';
    html += '<table id="ch_add" class="table table-bordered table-hover">';
    html += '<tr><td>Тип</td><td><select id="type_id">';
    for (var type in meters.channels_type) {
        html += '<option value="'+meters.channels_type[type].id+'">'+meters.channels_type[type].type+'</option>';
    };
    html += '</select></td></tr>';
    html += '<tr><td>Описание</td><td><input id="ch_desc" type="text" value=""></td></tr>';
    html += '<tr><td>IP адрес</td><td><input id="ch_ip" type="text" value=""></td></tr>';
    html += '<tr><td>IP порт</td><td><input id="ch_port" type="text" value=""></td></tr>';
    html += '<tr><td>Настройки</td><td><input id="ch_settings" type="text" value=""></td></tr>';
    html += '<tr><td>Активен</td><td><select id="ch_active">';
    html += '<option value="1">Да</option>';
    html += '<option value="0">Нет</option>';
    html += '</td></tr>';
    html += '</table>';
    function collectValues(tableID) {
        var result = {};
        result['id'] = self.id;
        result['type_id'] = $(tableID).find("#type_id").val();
        result['ch_desc'] = $(tableID).find("#ch_desc").val();
        result['ch_ip'] = $(tableID).find("#ch_ip").val();
        result['ch_port'] = $(tableID).find("#ch_port").val();
        var settings = $(tableID).find("#ch_settings").val();
        result['ch_settings'] = {settings: settings};
        result['is_active'] = $(tableID).find("#ch_active").val();
        return result;
    }
    $("#ch_add_dialog").html(html);
    $("#ch_add_dialog").dialog({
        title: 'Добавление канала опроса',
        height: 560,
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
                    var tableID = $("#ch_add");
                    var params = collectValues(tableID);
                    meters.addNewChannel(params);
                    $(this).dialog("close");
                }
            }
          ]
    });
}

function editChannelDialog(channel, meters) {
    var self = channel;
    var meters = meters;
    var html = '';
    html += '<table id="ch_edit_'+self.id+'" class="table table-bordered table-hover">';
    html += '<tr><td>Тип</td><td><select id="type_id">';
    for (var type in meters.channels_type) {
        if (self.type_id.id === meters.channels_type[type].id) {
            html += '<option selected value="'+meters.channels_type[type].id+'">'+meters.channels_type[type].type+'</option>';  
        }
        else {
            html += '<option value="'+meters.channels_type[type].id+'">'+meters.channels_type[type].type+'</option>';
        }
    };
    html += '</select></td></tr>';
    html += '<tr><td>Описание</td><td><input id="ch_desc" type="text" value="'+self.ch_desc+'"></td></tr>';
    html += '<tr><td>IP адрес</td><td><input id="ch_ip" type="text" value="'+self.ch_ip+'"></td></tr>';
    html += '<tr><td>IP порт</td><td><input id="ch_port" type="text" value="'+self.ch_port+'"></td></tr>';
    html += '<tr><td>Настройки</td><td><input id="ch_settings" type="text" value="'+self.ch_settings.settings+'"></tr>';
    html += '<tr><td>Активен</td><td><select id="ch_active">';
    if (self.is_active == 1) {
        html += '<option selected value="1">Да</option>';
        html += '<option value="0">Нет</option>';
    }
    else if (self.is_active == 0) {
        html += '<option value="1">Да</option>';
        html += '<option selected value="0">Нет</option>';
    }
    else {
        html += '<option value="1">Да</option>';
        html += '<option value="0">Нет</option>';
    }
    
    html += '</td></tr>';
    html += '</table>';
    function collectValues(tableID) {
        var result = {};
        result['id'] = self.id;
        result['type_id'] = $(tableID).find("#type_id").val();
        result['ch_desc'] = $(tableID).find("#ch_desc").val();
        result['ch_ip'] = $(tableID).find("#ch_ip").val();
        result['ch_port'] = $(tableID).find("#ch_port").val();
        var settings = $(tableID).find("#ch_settings").val();
        result['ch_settings'] = {settings: settings};
        result['is_active'] = $(tableID).find("#ch_active").val();
        return result;
    }
    $("#ch_edit_dialog").html(html);
    $("#ch_edit_dialog").dialog({
        title: 'Редактирование канала опроса',
        height: 450,
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
                    var tableID = $("#ch_edit_"+self.id);
                    var params = collectValues(tableID);
                    self.saveParams(params, meters);
                    $(this).dialog("close");
                }
            }
          ]
    });
}

function delChannelDialog(channel, meters) {
    var meters = meters;
    var channel = channel;
    var html = '';
    html += '<h4>Вы уверены, что хотите удалить канал опроса?</h4>'
    html += '<table id="ch_del" class="table table-bordered table-hover">';
    html += '<tr><th>#ID</th><th>Канал опроса</th></tr>';
    html += '<tr><td>'+channel.id+'</td><td>'+channel.ch_desc+'</td></tr>';
    html += '</table>';
    $("#ch_delete_dialog").html(html);
    $("#ch_delete_dialog").dialog({
        title: 'Удаление канала опроса',
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
                    meters.deleteChannel(channel.id)
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

////////////////////////////////////////////////////////////////////////////////
// Objects dialogs
////////////////////////////////////////////////////////////////////////////////
function addObjectDialog(meters) {
    var meters = meters;
    var html = '';
    html += '<table id="obj_add" class="table table-bordered table-hover">';
    html += '<tr><td>Описание</td><td><input id="obj_desc" type="text" value=""></td></tr>';
    html += '</table>';
    function collectValues(tableID) {
        var result = {};
        result['id'] = self.id;
        result['higher'] = 0;
        result['obj_desc'] = $(tableID).find("#obj_desc").val();
        return result;
    }
    $("#obj_add_dialog").html(html);
    $("#obj_add_dialog").dialog({
        title: 'Добавление объекта учета',
        height: 560,
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
                    var tableID = $("#obj_add");
                    var params = collectValues(tableID);
                    meters.addNewObject(params);
                    $(this).dialog("close");
                }
            }
          ]
    });
}

function editObjectDialog(object, meters) {
    var self = object;
    var meters = meters;
    var html = '';
    html += '<table id="obj_edit_'+self.id+'" class="table table-bordered table-hover">';
    html += '<tr><td>Описание</td><td><input id="obj_desc" type="text" value="'+self.obj_desc+'"></td></tr>';
    html += '</table>';
    function collectValues(tableID) {
        var result = {};
        result['id'] = self.id;
        result['higher'] = 0;
        result['obj_desc'] = $(tableID).find("#obj_desc").val();
        return result;
    }
    $("#obj_edit_dialog").html(html);
    $("#obj_edit_dialog").dialog({
        title: 'Редактирование объекта учета',
        height: 450,
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
                    var tableID = $("#obj_edit_"+self.id);
                    var params = collectValues(tableID);
                    self.saveParams(params, meters);
                    $(this).dialog("close");
                }
            }
          ]
    });
}

function delObjectDialog(object, meters) {
    var meters = meters;
    var object = object;
    var html = '';
    html += '<h4>Вы уверены, что хотите удалить канал опроса?</h4>'
    html += '<table id="obj_del" class="table table-bordered table-hover">';
    html += '<tr><th>#ID</th><th>Объект учета</th></tr>';
    html += '<tr><td>'+object.id+'</td><td>'+object.obj_desc+'</td></tr>';
    html += '</table>';
    $("#obj_delete_dialog").html(html);
    $("#obj_delete_dialog").dialog({
        title: 'Удаление объекта учета',
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
                    meters.deleteObject(object.id)
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


////////////////////////////////////////////////////////////////////////////////
// Table TR
////////////////////////////////////////////////////////////////////////////////
function meterTR(meter) {
    var html = '';
    html += '<tr id="tr_wh_'+meter.id+'"><td width="50">'+meter.id+'</td>';
    html += '<td id="object_id">'+meter.object_id['obj_desc']+'</td>';
    html += '<td id="wh_desc">'+meter.wh_desc+'</td>';
    html += '<td id="type_id">'+meter.type_id['type']+'</td>';
    html += '<td id="wh_num">'+meter.wh_num+'</td>';
    html += '<td id="wh_adr">'+meter.wh_adr+'</td>';
    html += '<td id="channel_id">'+meter.channel_id['ch_desc']+'</td>';
    html += '<td width="400" align="center"><div class="btn-group">';
    html += '<button class="edit_info_wh btn btn-primary btn-sm" wh_id="'+meter.id+'" >';
    html += '<span class="glyphicon glyphicon-pencil"></span> Редактировать</button>';
    html += '<button class="delete_wh btn btn-danger btn-sm" wh_id="'+meter.id+'" >';
    html += '<span class="glyphicon glyphicon-trash"></span> Удалить</button></div></td></tr>'
    return html;
}

function channelTR(channel) {
    var html = '';
    if (channel.is_active == 0) {
        html += '<tr style="background-color:grey;" id="ch_'+channel.id+'"><td width="50">'+channel.id+'</td>';
    }
    else {
        html += '<tr id="ch_'+channel.id+'"><td width="50">'+channel.id+'</td>';
    }
    html += '<td id="ch_type">'+channel.type_id['type']+'</td>';
    html += '<td id="ch_desc">'+channel.ch_desc+'</td>';
    html += '<td id="ch_ip">'+channel.ch_ip+'</td>';
    html += '<td id="ch_port">'+channel.ch_port+'</td>';
    html += '<td width="400" align="center"><div class="btn-group">';
    html += '<button class="edit_info_ch btn btn-primary btn-sm" ch_id="'+channel.id+'" >';
    html += '<span class="glyphicon glyphicon-pencil"></span> Редактировать</button>';
    html += '<button class="delete_ch btn btn-danger btn-sm" ch_id="'+channel.id+'" >';
    html += '<span class="glyphicon glyphicon-trash"></span> Удалить</button></div></td></tr>'
    return html;
}

function channelStatusTR(channel) {
    var html = '';
    var meters = window.meters;
    html += '<tr id="ch_'+channel.id+'"><td width="50">'+channel.id+'</td>';
    html += '<td id="ch_desc">'+channel.ch_desc+'</td>';
    html += '<td id="ch_type">'+channel.type_id['type']+'</td>';
    html += '<td id="status_datetime">'+channel.status_datetime+'</td>';
    html += '<td id="status_string">'+channel.status_string+'</td>';
    if (channel.status_code==1 || channel.status_code==2 || channel.status_code==3) {
        html += '<td align="center"><div id="channel_processing"><img src="'+meters.staticUrl+'images/channel_status_processing.gif"></div></td>';
    }
    html += '</tr>';
    return html;
}

function objectTR(object) {
    var html = '';
    html += '<tr id="obj_'+object.id+'"><td width="50">'+object.id+'</td>';
    html += '<td id="obj_desc">'+object.obj_desc+'</td>';
    html += '<td width="400" align="center"><div class="btn-group">';
    html += '<button class="edit_info_obj btn btn-primary btn-sm" obj_id="'+object.id+'" >';
    html += '<span class="glyphicon glyphicon-pencil"></span> Редактировать</button>';
    html += '<button class="delete_obj btn btn-danger btn-sm" obj_id="'+object.id+'" >';
    html += '<span class="glyphicon glyphicon-trash"></span> Удалить</button></div></td></tr>'
    return html;
}