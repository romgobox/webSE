////////////////////////////////////////////////////////////////////////////////
// Object
////////////////////////////////////////////////////////////////////////////////

var whObject = function(data) {
    this.id = data['id'];
    this.obj_desc = data['obj_desc'];
};

whObject.prototype.renderObjectTR = function() {
    return objectTR(this);
};

whObject.prototype.saveParams = function (params, meters) {
    var self = this;
    var meters = meters;
    var params = params;
    $.ajax({
        url: "/objectinfo/"+self.id,
        type: "POST",
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
    this.obj_desc = data['obj_desc'];
};