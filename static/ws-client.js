$(document).ready(function(){
    var WEBSOCKET_ROUTE = "/ws";

    if(window.location.protocol == "http:"){
        //localhost
        var ws = new WebSocket("ws://" + window.location.host + WEBSOCKET_ROUTE);
        }
    else if(window.location.protocol == "https:"){
        //Dataplicity
        var ws = new WebSocket("wss://" + window.location.host + WEBSOCKET_ROUTE);
        }

    ws.onopen = function(evt) {
        $("#ws-status").html("Połączono");
        setInterval(function() {
            window.location.reload();
          },30000); 
        };

    ws.onmessage = function(evt) {
        window.location.reload();
        };

    ws.onclose = function(evt) {
        $("#ws-status").html("Rozłączono");
        };

    $("#radio-yes").click(function(){
        if ($("#radio-yes").prop("checked") == true){
            ws.send("switch_1_open");
            window.location.reload();
        }
        else
            ws.send("switch_1_offenbach");
            window.location.reload();
    });
    $("#radio-neutral").click(function(){
        if ($("#radio-neutral").prop("checked") == true){
            ws.send("STOP");
            window.location.reload();
        }
        else
            ws.send("stop sie wywalil");
            window.location.reload();
    });
    $("#radio-neutral2").click(function(){
        if ($("#radio-neutral2").prop("checked") == true){
            ws.send("abort");
            window.location.reload();
        }
        else
            ws.send("stop sie wywalil");
            window.location.reload();
    });
    $("#radio-no").click(function(){
        if ($("#radio-no").prop("checked") == true){
            ws.send("switch_1_close");
            window.location.reload();
        }
        else
            ws.send("switch_1_offenbachv2")
            window.location.reload();
    });
    $("#radio-yes2").click(function(){
        if ($("#radio-yes2").prop("checked") == true){
            ws.send("switch_2_open");
            window.location.reload();
        }
        else
            ws.send("switch_2_offenbach");
            window.location.reload();
    });
    $("#radio-no2").click(function(){
        if ($("#radio-no2").prop("checked") == true){
            ws.send("switch_2_close");
            window.location.reload();
        }
        else
            ws.send("switch_2_offenbachv2")
            window.location.reload();
    });
    

    $("#switch-3").click(function(){
        if ($("#switch-3").prop("checked") == true){
            ws.send("switch_3_on");
            window.location.reload();
        }
        else
            ws.send("switch_3_off");
            window.location.reload();
    });

    $("#switch-4").click(function(){
        if ($("#switch-4").prop("checked") == true){
            ws.send("switch_4_on");
            window.location.reload();
        }
        else
            ws.send("switch_4_off")
            window.location.reload();
    });

    $("#switch-5").click(function(){
        if ($("#switch-5").prop("checked") == true){
            ws.send("switch_5_on");
            window.location.reload();
        }
        else 
            ws.send("switch_5_off")
            window.location.reload();
    });

    $("#switch-6").click(function(){
        if ($("#switch-6").prop("checked") == true){
            ws.send("switch_6_on");
            window.location.reload();
        }
        else
            ws.send("switch_6_off");
            window.location.reload();
    });

    $("#button_1_start_temp").click(function(){
        var temp = $("#switch_1_start_temp").val();
        ws.send("switch_1_start_temp " + temp);
        window.location.reload();
    });
    $("#button_1_end_temp").click(function(){
    var temp = $("#switch_1_end_temp").val();
    ws.send("switch_1_end_temp " + temp);
    window.location.reload();
    });
    $("#button_2_start_temp").click(function(){
        var temp = $("#switch_2_start_temp").val();
        ws.send("switch_2_start_temp " + temp);
        window.location.reload();
    });
    $("#button_2_end_temp").click(function(){
    var temp = $("#switch_2_end_temp").val();
    ws.send("switch_2_end_temp " + temp);
    window.location.reload();
    });
    
    $("#button_3_time").click(function(){
         var time = $("#switch_3_time").val();
         ws.send("switch_3_time " + time);
         window.location.reload();
    });
    $("#button_3_duration").click(function(){
        var duration = $("#switch_3_duration").val();
        ws.send("switch_3_duration " + duration);
        window.location.reload();
   });    
   $("#button_4_time").click(function(){
         var time = $("#switch_4_time").val();
         ws.send("switch_4_time " + time);
         window.location.reload();
    });
    $("#button_4_duration").click(function(){
        var duration = $("#switch_4_duration").val();
        ws.send("switch_4_duration " + duration);
        window.location.reload();
   });
   $("#button_5_time").click(function(){
    var time = $("#switch_5_time").val();
    ws.send("switch_5_time " + time);
    window.location.reload();
    });
    $("#button_5_duration").click(function(){
    var duration = $("#switch_5_duration").val();
    ws.send("switch_5_duration " + duration);
    window.location.reload();
    });
    $("#button_6_time").click(function(){
        var time = $("#switch_6_time").val();
        ws.send("switch_6_time " + time);
        window.location.reload();
    });
    $("#button_6_duration").click(function(){
       var duration = $("#switch_6_duration").val();
       ws.send("switch_6_duration " + duration);
       window.location.reload();
    });

  });