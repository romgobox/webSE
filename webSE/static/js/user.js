////////////////////////////////////////////////////////////////////////////////
// User
////////////////////////////////////////////////////////////////////////////////

var User = function(data) {
    this.id = data['id'];
    this.name = data['name'];
    this.username = data['username'];
    this.role = data['role'];
    this.organisation = data['organisation'];
};

whObject.prototype.renderObjectTR = function() {
    return objectTR(this);
};

whObject.prototype.saveParams = function (params, meters) {
    var self = this;
    var meters = meters;
    var params = params;
    $.ajax({
        url: "/objects/"+self.id,
        type: "PUT",
        async: false,
        data: JSON.stringify(params),
        dataType: "json",
        contentType: "application/json",
        success: function(data){
            self.updateData(params, meters);
            var html = self.renderObjectTR();
            $("#obj_"+self.id).replaceWith(html);
            showStatusDialog('info', data['status'], 'Изменен объект учета');
        }
    });
};

whObject.prototype.updateData = function (data, meters) {
    this.id = data['id'];
    this.higher = data['higher'];
    this.obj_desc = data['obj_desc'];
};