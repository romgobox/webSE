////////////////////////////////////////////////////////////////////////////////
// Requests handlers
////////////////////////////////////////////////////////////////////////////////

function getRequestByChannel(data) {
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
                    renderRequestTable(data);
                }
    });
}