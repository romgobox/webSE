////////////////////////////////////////////////////////////////////////////////
// Reports handlers
////////////////////////////////////////////////////////////////////////////////

function getReportByMeterID(data, meter) {
    var meter = data['meter'];
    var whID = data['wh_id'];
    var paramNum = data['param_num'];
    var reportType =  data['report_type'];
    $.ajax({
        url: "/reports/"+paramNum+"/"+whID,
        type: "POST",
        async: false,
        data: JSON.stringify(data),
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
                    renderReportTable(data, meter, reportType);
                }
    });
}