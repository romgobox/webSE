////////////////////////////////////////////////////////////////////////////////
// Meter
////////////////////////////////////////////////////////////////////////////////

var Meter = function(data) {
    this.id = data['id'];
    this.wh_desc = data['wh_desc'];
    this.wh_num = data['wh_num'];
    this.wh_adr = data['wh_adr'];
    this.ppValue = data['wh_settings']['ppValue']['depth'];
    this.fixDay = data['wh_settings']['fixDay']['depth'];
    this.channel_id = data['channel_id'];
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

Meter.prototype.saveParams = function (params) {
    var self = this;
    var params = params;
    $.ajax({
        url: "/meterinfo/"+self.id,
        type: "POST",
        async: false,
        data: JSON.stringify(params),
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            self.updateData(params);
            html = self.renderMeterTR();
            $("#wh_"+self.id).replaceWith(html);
            $("#data").html(data['status']);
        }
    });
};

Meter.prototype.updateData = function (data) {
    this.id = data['id'];
    this.wh_desc = data['wh_desc'];
    this.wh_num = data['wh_num'];
    this.wh_adr = data['wh_adr'];
    this.ppValue = data['wh_settings']['ppValue']['depth'];
    this.fixDay = data['wh_settings']['fixDay']['depth'];
    this.channel_id = data['channel_id'];
}