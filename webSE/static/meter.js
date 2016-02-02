////////////////////////////////////////////////////////////////////////////////
// Meter
////////////////////////////////////////////////////////////////////////////////

var Meter = function(data, meters) {
    this.id = data['id'];
    this.wh_adr = data['wh_adr'];
    this.wh_num = data['wh_num'];
    this.wh_pass = data['wh_pass'];
    this.wh_object = meters.objects[data['obj_id']];
    this.wh_desc = data['wh_desc'];
    this.ppValue = data['wh_settings']['ppValue'];
    this.fixDay = data['wh_settings']['fixDay'];
    this.wh_protocol = meters.protocols[data['pr_id']];
    this.wh_channel = typeof meters.channels[data['ch_id']] == 'undefined' ? {} : meters.channels[data['ch_id']];
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
        url: "/meterinfo/"+self.id,
        type: "POST",
        async: false,
        data: JSON.stringify(params),
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            self.updateData(params, meters);
            var html = self.renderMeterTR();
            $("#wh_"+self.id).replaceWith(html);
            showStatusDialog('info', data['status'], 'Изменен прибор учета');
        }
    });
};

Meter.prototype.updateData = function (data, meters) {
    this.id = data['id'];
    this.wh_adr = data['wh_adr'];
    this.wh_num = data['wh_num'];
    this.wh_pass = data['wh_pass'];
    this.wh_object = meters.objects[data['obj_id']];
    this.wh_desc = data['wh_desc'];
    this.ppValue = data['wh_settings']['ppValue'];
    this.fixDay = data['wh_settings']['fixDay'];
    this.wh_protocol = meters.protocols[data['pr_id']];
    this.wh_channel = meters.channels[data['ch_id']];
}