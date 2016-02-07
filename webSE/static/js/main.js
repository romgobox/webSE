
$(document).ready(function() {
    // Инициализириуем глобальный объект
    var meters = new Meters();
    window.meters = meters;
    // Запрашиваем объекты, протоколы, каналы, счетчики
    meters.getObjects();
    meters.getProtocols();
    meters.getChannels();
    meters.getMeters();
    // Рисуем таблицы объектов, протоколов, каналов, счетчиков
    meters.renderMetersTable();
    meters.renderChannelsTable();
    meters.renderObjectsTable();
    registerClick();
});

////////////////////////////////////////////////////////////////////////////////
// Handlers
////////////////////////////////////////////////////////////////////////////////
function registerClick() {

    ////////////////////////////////////////////////////////////////////////////
    // Main menu
    ////////////////////////////////////////////////////////////////////////////
    $("#main_menu").on('click', "#reports", function (e){
        e.preventDefault();
        renderReportsUI();
        registerClick();
    });

    ////////////////////////////////////////////////////////////////////////////
    // Reports menu
    ////////////////////////////////////////////////////////////////////////////
    $("#reports_menu").on('click', ".fixday_report", function (e){
        e.preventDefault();
        ReportByMeterIDDialog(meters, 1, 'dates_list');
        registerClick();
    });

    $("#reports_menu").on('click', ".fixday_diff_report", function (e){
        e.preventDefault();
        ReportByMeterIDDialog(meters, 1, 'dates_diff');
        registerClick();
    });

    $("#reports_menu").on('click', ".ppvalue_report", function (e){
        e.preventDefault();
        ReportByMeterIDDialog(meters, 2, 'dates_list');
        registerClick();
    });

    $("#select_object").on('change', function(e){
        e.preventDefault();
        metersSelectByObject(meters);
    });

    ////////////////////////////////////////////////////////////////////////////
    // Datepicker
    ////////////////////////////////////////////////////////////////////////////
    $.datepicker.regional['ru'] = { 
        closeText: 'Закрыть', 
        prevText: '&#x3c;Пред', 
        nextText: 'След&#x3e;', 
        currentText: 'Сегодня', 
        monthNames: ['Январь','Февраль','Март','Апрель','Май','Июнь', 
        'Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'], 
        monthNamesShort: ['Янв','Фев','Мар','Апр','Май','Июн', 
        'Июл','Авг','Сен','Окт','Ноя','Дек'], 
        dayNames: ['воскресенье','понедельник','вторник','среда','четверг','пятница','суббота'], 
        dayNamesShort: ['вск','пнд','втр','срд','чтв','птн','сбт'], 
        dayNamesMin: ['Вс','Пн','Вт','Ср','Чт','Пт','Сб'], 
        dateFormat: 'yy-mm-dd', 
        firstDay: 1, 
        isRTL: false 
    }; 
    $.datepicker.setDefaults($.datepicker.regional["ru"]);
    $(".datepicker").datepicker();
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









