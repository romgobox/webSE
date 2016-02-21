////////////////////////////////////////////////////////////////////////////////
// Meter
////////////////////////////////////////////////////////////////////////////////

var Meter = function(data, meters) {
    this.id = data['id'];
    this.type_id = typeof meters.meters_type[data['type_id']] == 'undefined' ? {} : meters.meters_type[data['type_id']];
    this.wh_adr = data['wh_adr'];
    this.wh_num = data['wh_num'];
    this.wh_pass = data['wh_pass'];
    this.wh_desc = data['wh_desc'];
    this.wh_KI = data['wh_KI'];
    this.wh_KU = data['wh_KU'];
    this.wh_IMPL = data['wh_IMPL'];
    this.ppValue = data['wh_settings']['ppValue'];
    this.fixDay = data['wh_settings']['fixDay'];
    this.object_id = typeof meters.objects[data['object_id']] == 'undefined' ? {} : meters.objects[data['object_id']];
    this.channel_id = typeof meters.channels[data['channel_id']] == 'undefined' ? {} : meters.channels[data['channel_id']];
    this.is_active = data['is_active'];
};

Meter.prototype.getParams = function () {
    $.ajax({
        url: "/meterinfo/"+this.id,
        type: "GET",
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                   console.log(data);
    }});
};

Meter.prototype.renderMeterTR = function() {
    return meterTR(this);
};

Meter.prototype.saveParams = function (params, meters) {
    var self = this;
    var meters = meters;
    var params = params;
    $.ajax({
        url: "/meters/"+self.id,
        type: "PUT",
        async: false,
        data: JSON.stringify(params),
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            self.updateData(params, meters);
            var html = self.renderMeterTR();
            $("#tr_wh_"+self.id).replaceWith(html);
            showStatusDialog('info', data['status'], 'Изменен прибор учета');
        }
    });
};

Meter.prototype.updateData = function (data, meters) {
    this.id = data['id'];
    this.type_id = typeof meters.meters_type[data['type_id']] == 'undefined' ? {} : meters.meters_type[data['type_id']];
    this.wh_adr = data['wh_adr'];
    this.wh_num = data['wh_num'];
    this.wh_pass = data['wh_pass'];
    this.wh_desc = data['wh_desc'];
    this.wh_KI = data['wh_KI'];
    this.wh_KU = data['wh_KU'];
    this.wh_IMPL = data['wh_IMPL'];
    this.ppValue = data['wh_settings']['ppValue'];
    this.fixDay = data['wh_settings']['fixDay'];
    this.object_id = typeof meters.objects[data['object_id']] == 'undefined' ? {} : meters.objects[data['object_id']];
    this.channel_id = typeof meters.channels[data['channel_id']] == 'undefined' ? {} : meters.channels[data['channel_id']];
    this.is_active = data['is_active'];
};

////////////////////////////////////////////////////////////////////////////////
// MeterType
////////////////////////////////////////////////////////////////////////////////

var MeterType = function(data, meters) {
    this.id = data['id'];
    this.type = data['type'];
    this.short_type = data['short_type'];
    this.protocol_id = typeof meters.protocols[data['protocol_id']] == 'undefined' ? {} : meters.protocols[data['protocol_id']];
};