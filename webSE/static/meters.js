////////////////////////////////////////////////////////////////////////////////
// Meters
////////////////////////////////////////////////////////////////////////////////

var Meters = function() {
    this.meters = {}
    this.dialogs = {};
};

Meters.prototype.addMeter = function(meter) {
    this.meters[meter.id] = meter;
};

Meters.prototype.addNewMeter = function (data) {
    var self = this
    $.ajax({
        url: "/addmeter",
        type: "PUT",
        async: false,
        data: JSON.stringify(data),
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            var meter = new Meter(data);
            self.addMeter(meter);
            html = meter.renderMeterTR();
            $("#wh_table tbody").append(html);
            $("#data").html(data['status']);
        }
    });
};

Meters.prototype.deleteMeter = function(whID) {
    var whID = whID;
    var self = this;
    $.ajax({
        url: "/delmeter/"+whID,
        type: "POST",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            $("#wh_"+whID).remove();
            delete self.meters[whID];
            $("#data").html(data['status']);
        }
    });
}

Meters.prototype.getMeters = function() {
    var self = this;
    $.ajax({
        url: "/meters",
        type: "GET",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    var html = ''
                    var id = ''
                    $.each(data, function(index, item) {
                        self.addMeter(new Meter(item));
                    });
                }
    });
};

Meters.prototype.renderMetersTable = function() {
    var html = '';    
    for (var m in this.meters) {
        html += this.meters[m].renderMeterTR();
    };
    $("#wh_table tbody").html(html);
    return html;
};

Meters.prototype.returnMeter = function(id) {
    return this.meters[id];
};