////////////////////////////////////////////////////////////////////////////////
// Requests handlers
////////////////////////////////////////////////////////////////////////////////

function getRequestByChannel(data, reply) {
    var reply = data['reply'] || false;
    var data = data;
    $.ajax({
        url: "/requests/channels",
        type: "POST",
        async: true,
        data: JSON.stringify(data),
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    $('#waiting').hide();
                    if (reply) {
                        renderRequestTable(data['result']);
                    }
                    else {
                        showStatusDialog('info', data['message'], 'Информация');
                    }
                }
    });
}