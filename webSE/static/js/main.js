
$(document).ready(function() {
    // Инициализириуем глобальный объект
    $("#waiting").show();
    var meters = new Meters();
    window.meters = meters;
    window.meters.staticUrl = staticUrl;
    meters.getObjects();
    meters.getProtocols();
    meters.getChannelsType();
    meters.getChannels();
    meters.getChannelsStatus();
    meters.getMetersType();
    meters.getMeters();
    meters.getUser();

    // Рисуем интерфейс
    renderMetersUI();
    // Рисуем таблицы объектов, протоколов, каналов, счетчиков
    meters.renderMetersTable();
    meters.renderChannelsTable();
    meters.renderObjectsTable();
    meters.renderUserTable();
    registerClick();
    $("#waiting").hide();
});

////////////////////////////////////////////////////////////////////////////////
// Handlers
////////////////////////////////////////////////////////////////////////////////
function registerClick() {

    ////////////////////////////////////////////////////////////////////////////
    // Main menu
    ////////////////////////////////////////////////////////////////////////////
    $("#main_menu").on('click', "#configurator", function (e){
        e.preventDefault();
        renderMetersUI();
        $("#configurator").toggleClass("active");
        $("#reports").removeClass("active");
        $("#requests").removeClass("active");
        $("#user").removeClass("active");
    });

    $("#main_menu").on('click', "#reports", function (e){
        e.preventDefault();
        renderReportsUI();
        $("#configurator").removeClass("active");
        $("#reports").toggleClass("active");
        $("#requests").removeClass("active");
        $("#user").removeClass("active");
    });

    $("#main_menu").on('click', "#requests", function (e){
        e.preventDefault();
        renderRequestsUI();
        $("#configurator").removeClass("active");
        $("#reports").removeClass("active");
        $("#requests").toggleClass("active");
        $("#user").removeClass("active");
    });

    $("#main_menu").on('click', "#user", function (e){
        e.preventDefault();
        renderUserUI();
        $("#configurator").removeClass("active");
        $("#reports").removeClass("active");
        $("#requests").removeClass("active");
        $("#user").toggleClass("active");
    });

    ////////////////////////////////////////////////////////////////////////////
    // Requests menu
    ////////////////////////////////////////////////////////////////////////////
    $("#requests_menu").on('click', ".channels_requests", function (e){
        e.preventDefault();
        requestByChannelsDialog(meters, false);
    });

    $("#requests_menu").on('click', ".channels_requests_queue", function (e){
        e.preventDefault();
        requestByChannelsDialog(meters, true);
    });

    $("#channels_status").on('click', ".channels_status_refresh", function (e){
        e.stopImmediatePropagation();
        var meters = window.meters;
        if ($("#channels_status .channels_status_refresh").html() == 'Вкл. автообновление') {
            meters.channelStatusRefresh = setInterval(function() { meters.getChannelsStatus() }, 3000);
            $("#channels_status .channels_status_refresh").html("Выкл. автообновление");
        }
        else {
            clearInterval(meters.channelStatusRefresh); 
            $("#channels_status .channels_status_refresh").html("Вкл. автообновление");
        }
    });

    ////////////////////////////////////////////////////////////////////////////
    // Reports menu
    ////////////////////////////////////////////////////////////////////////////
    $("#reports_menu").on('click', ".fixday_report", function (e){
        e.preventDefault();
        ReportByMeterIDDialog(meters, 1, 'dates_list');
    });

    $("#reports_menu").on('click', ".fixday_diff_report", function (e){
        e.preventDefault();
        ReportByMeterIDDialog(meters, 1, 'dates_diff');
    });

    $("#reports_menu").on('click', ".ppvalue_report", function (e){
        e.preventDefault();
        ReportByMeterIDDialog(meters, 2, 'dates_list');
    });

    ////////////////////////////////////////////////////////////////////////////
    // Meters menu
    ////////////////////////////////////////////////////////////////////////////
    $("#meters_menu").on('click', ".add_wh", function (e){
        e.preventDefault();
        addMeterDialog(meters);
    });

    $("#meters_menu").on('click', ".add_ch", function (e){
        e.preventDefault();
        addChannelDialog(meters);
    });

    $("#meters_menu").on('click', ".add_obj", function (e){
        e.preventDefault();
        addObjectDialog(meters);
    });

    ////////////////////////////////////////////////////////////////////////////
    // Meters table
    ////////////////////////////////////////////////////////////////////////////
    $("#wh_table").on('click', ".edit_info_wh", function (e){
        e.preventDefault();
        var whID = parseInt($(this).attr('wh_id'));
        var meter = meters.returnMeter(whID);
        editMeterDialog(meter, meters);
    });
    $("#wh_table").on('click', ".delete_wh", function (e){
        e.preventDefault();
        var whID = parseInt($(this).attr('wh_id'));
        var meter = meters.returnMeter(whID);
        delMeterDialog(meter, meters);
    });

    ////////////////////////////////////////////////////////////////////////////
    // Channels table
    ////////////////////////////////////////////////////////////////////////////
    $("#ch_table").on('click', ".edit_info_ch", function (e){
        e.preventDefault();
        var chID = parseInt($(this).attr('ch_id'));
        var channel = meters.returnChannel(chID);
        editChannelDialog(channel, meters);
    });
    $("#ch_table").on('click', ".delete_ch", function (e){
        e.preventDefault();
        var chID = parseInt($(this).attr('ch_id'));
        var channel = meters.returnChannel(chID);
        delChannelDialog(channel, meters);
    });

    ////////////////////////////////////////////////////////////////////////////
    // Objects table
    ////////////////////////////////////////////////////////////////////////////
    $("#obj_table").on('click', ".edit_info_obj", function (e){
        e.preventDefault();
        var objID = parseInt($(this).attr('obj_id'));
        var object = meters.returnObject(objID);
        editObjectDialog(object, meters);
    });
    $("#obj_table").on('click', ".delete_obj", function (e){
        e.preventDefault();
        var objID = parseInt($(this).attr('obj_id'));
        var object = meters.returnObject(objID);
        delObjectDialog(object, meters);
    });
    
};









