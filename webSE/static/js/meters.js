////////////////////////////////////////////////////////////////////////////////
// Meters
////////////////////////////////////////////////////////////////////////////////

var Meters = function() {
    this.objects = {};
    this.protocols = {};
    this.channels = {};
    this.channels_type = {};
    // this.meters = {}
    this.meters = [];
    this.meters_type = {};
    this.user = {};
};

Meters.prototype.addUser = function(user) {
    this.user = user;
};

Meters.prototype.addObject = function(object) {
    this.objects[object.id] = object;
};

Meters.prototype.addProtocol = function(protocol) {
    this.protocols[protocol.id] = protocol;
};

Meters.prototype.addChannel = function(channel) {
    this.channels[channel.id] = channel;
};

Meters.prototype.addChannelType = function(channel_type) {
    this.channels_type[channel_type.id] = channel_type;
};

Meters.prototype.addMeter = function(meter) {
    // var id = meter.id;
    // this.meters[id] = meter;
    this.meters.push(meter);
    this.meters.sort(function(a,b) {
        return parseInt(a.object_id.id) - parseInt(b.object_id.id);
    });
};

Meters.prototype.addMeterType = function(meter_type) {
    this.meters_type[meter_type.id] = meter_type;
};

Meters.prototype.getUser = function() {
    var self = this;
    $.ajax({
        url: "/user",
        type: "GET",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    self.addUser(new User(data));
                }
    });
};

Meters.prototype.getObjects = function() {
    var self = this;
    $.ajax({
        url: "/objects",
        type: "GET",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    $.each(data, function(index, item) {
                        self.addObject(new whObject(item));
                    });
                }
    });
};

Meters.prototype.getProtocols = function() {
    var self = this;
    $.ajax({
        url: "/protocols",
        type: "GET",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    $.each(data, function(index, item) {
                        self.addProtocol(new Protocol(item));
                    });
                }
    });
};

Meters.prototype.getChannelsType = function() {
    var self = this;
    $.ajax({
        url: "/channels_type",
        type: "GET",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    $.each(data, function(index, item) {
                        self.addChannelType(new ChannelType(item));
                    });
                }
    });
};

Meters.prototype.getChannelsStatus = function() {
    var self = this;
    $.ajax({
        url: "/channels_status",
        type: "GET",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    $.each(data, function(index, item) {
                        var channel = self.returnChannel(item['channel_id']);
                        channel['status_code'] = item['status_code'];
                        channel['status_datetime'] = item['status_datetime'];
                        channel['status_string'] = item['status_string'];
                    });
                    self.renderChannelsStatusTable();
                }
    });
};

Meters.prototype.getChannels = function() {
    var self = this;
    $.ajax({
        url: "/channels",
        type: "GET",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    $.each(data, function(index, item) {
                        self.addChannel(new Channel(item, self));
                    });
                }
    });
};

Meters.prototype.getMeters = function() {
    var self = this;
    var meters = this;
    $.ajax({
        url: "/meters",
        type: "GET",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    $.each(data, function(index, item) {
                        self.addMeter(new Meter(item, self));
                    });
                }
    });
};

Meters.prototype.getMetersType = function() {
    var self = this;
    var meters = this;
    $.ajax({
        url: "/meters_type",
        type: "GET",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    $.each(data, function(index, item) {
                        self.addMeterType(new MeterType(item, self));
                    });
                }
    });
};

Meters.prototype.addNewMeter = function (data) {
    var self = this
    $.ajax({
        url: "/meters",
        type: "POST",
        async: false,
        data: JSON.stringify(data),
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            var meter = new Meter(data, self);
            self.addMeter(meter);
            self.renderMetersTable();
            showStatusDialog('success', data['status'], 'Добавлен прибор учета');
        }
    });
};

Meters.prototype.addNewChannel = function (data) {
    var self = this
    $.ajax({
        url: "/channels",
        type: "POST",
        async: false,
        data: JSON.stringify(data),
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            var channel = new Channel(data, self);
            self.addChannel(channel);
            html = channel.renderChannelTR();
            $("#ch_table tbody").append(html);
            showStatusDialog('success', data['status'], 'Добавлен канал опроса');
        }
    });
};

Meters.prototype.addNewObject = function (data) {
    var self = this
    $.ajax({
        url: "/objects",
        type: "POST",
        async: false,
        data: JSON.stringify(data),
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            var object = new whObject(data, self);
            self.addObject(object);
            html = object.renderObjectTR();
            $("#obj_table tbody").append(html);
            showStatusDialog('success', data['status'], 'Добавлен объект');
        }
    });
};

Meters.prototype.deleteMeter = function(whID) {
    var whID = whID;
    var self = this;
    $.ajax({
        url: "/meters/"+whID,
        type: "DELETE",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            $("#tr_wh_"+whID).remove();
            // delete self.meters[whID];
            for (var i = 0; i < self.meters.length; i++) {
                if (self.meters[i].id == whID) {
                    self.meters.splice(i, 1);
                };
            };
            showStatusDialog('warning', data['status'], 'Удален прибор учета');
        }
    });
};

Meters.prototype.deleteChannel = function(chID) {
    var chID = chID;
    var self = this;
    $.ajax({
        url: "/channels/"+chID,
        type: "DELETE",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            $("#ch_"+chID).remove();
            delete self.channels[chID];
            showStatusDialog('warning', data['status'], 'Удален канал опроса');
        }
    });
};

Meters.prototype.deleteObject = function(objID) {
    var objID = objID;
    var self = this;
    $.ajax({
        url: "/objects/"+objID,
        type: "DELETE",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            $("#obj_"+objID).remove();
            delete self.objects[objID];
            showStatusDialog('warning', data['status'], 'Удален объект учета');
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

Meters.prototype.renderChannelsTable = function() {
    var html = '';    
    for (var m in this.channels) {
        html += this.channels[m].renderChannelTR();
    };
    $("#ch_table tbody").html(html);
    return html;
};

Meters.prototype.renderChannelsStatusTable = function() {
    var html = '';    
    for (var m in this.channels) {
        html += this.channels[m].renderChannelStatusTR();
    };
    $("#channels_status_table tbody").html(html);
    return html;
};

Meters.prototype.renderObjectsTable = function() {
    var html = '';    
    for (var m in this.objects) {
        html += this.objects[m].renderObjectTR();
    };
    $("#obj_table tbody").html(html);
    return html;
};

Meters.prototype.renderUserTable = function() {
    var user = meters.user;
    $("#menu_user_holder").html(user['name']+' ('+user['username']+') ')
    $("#user_panel #user_name").html(user['name']);
    $("#user_panel #user_username").html(user['username']);
    $("#user_panel #user_role").html(user.role['name']);
    $("#user_panel #user_org_name").html(user.organisation['name']);
    $("#user_panel #user_org_inn").html(user.organisation['inn']);
    $("#user_panel #user_org_desc").html(user.organisation['desc']);
    $("#user_panel #user_org_email").html(user.organisation['email']);
    $("#user_panel #user_org_contacts").html(user.organisation['contacts']);
    return false;
};



Meters.prototype.returnMeter = function(id) {
    for (var m in this.meters) {
        if (this.meters[m]['id'] === id) {
            return this.meters[m];
        };
    };
};

Meters.prototype.returnChannel = function(id) {
    return this.channels[id];
};

Meters.prototype.returnObject = function(id) {
    return this.objects[id];
};