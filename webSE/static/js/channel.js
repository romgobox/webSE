////////////////////////////////////////////////////////////////////////////////
// Channel
////////////////////////////////////////////////////////////////////////////////

var Channel = function(data, meters) {
    this.id = data['id'];
    this.ch_desc = data['ch_desc'];
    this.ch_ip = data['ch_ip'];
    this.type_id = typeof meters.channels_type[data['type_id']] == 'undefined' ? {} : meters.channels_type[data['type_id']];
    this.ch_port = data['ch_port'];
    this.ch_settings = data['ch_settings'];
    this.is_active = data['is_active'];
};

Channel.prototype.renderChannelTR = function() {
    return channelTR(this);
};

Channel.prototype.saveParams = function (params, meters) {
    var self = this;
    var meters = meters;
    var params = params;
    $.ajax({
        url: "/channels/"+self.id,
        type: "PUT",
        async: false,
        data: JSON.stringify(params),
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            self.updateData(params, meters);
            var html = self.renderChannelTR();
            $("#ch_"+self.id).replaceWith(html);
            showStatusDialog('info', data['status'], 'Изменен канал опроса');
        }
    });
};

Channel.prototype.updateData = function (data, meters) {
    this.id = data['id'];
    this.ch_desc = data['ch_desc'];
    this.ch_ip = data['ch_ip'];
    this.type_id = typeof meters.channels_type[data['type_id']] == 'undefined' ? {} : meters.channels_type[data['type_id']];
    this.ch_port = data['ch_port'];
    this.ch_settings = data['ch_settings'];
    this.is_active = data['is_active'];
};


////////////////////////////////////////////////////////////////////////////////
// ChannelType
////////////////////////////////////////////////////////////////////////////////

var ChannelType = function(data) {
    this.id = data['id'];
    this.type = data['type'];
    this.short_type = data['short_type'];
};
