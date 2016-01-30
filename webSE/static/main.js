
$(document).ready(function() {
    var meters = new Meters();
    window.meters = meters;
    meters.getMeters();
    meters.renderMetersTable();
    registerClick();
});

////////////////////////////////////////////////////////////////////////////////
// Handlers
////////////////////////////////////////////////////////////////////////////////
function registerClick() {
    $("#wh_table").on('click', ".edit_info_wh", function (e){
        e.preventDefault();
        var whID = parseInt($(this).attr('wh_id'));
        var meter = meters.returnMeter(whID);
        editMeterDialog(meter);
    });
    $("#wh_table").on('click', ".delete_wh", function (e){
        e.preventDefault();
        var whID = parseInt($(this).attr('wh_id'));
        var meter = meters.returnMeter(whID);
        delMeterDialog(meter, meters);
    });
    $("#wh_menu").on('click', ".add_wh", function (e){
        e.preventDefault();
        addMeterDialog(meters);
    });
};









