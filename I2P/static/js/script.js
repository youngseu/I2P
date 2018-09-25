/**
 * Created by yang on 18-4-12.
 */
$(document).ready(function(){
    $("#login").click(function () {
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username": user, "password": pwd};
        $.ajax({
            type:"post",
            url:"/test",
            data:pd,
            cache:false,
            success:function (data) {
                alert(data);
            },
            error:function () {
                alert("error!");
            },
        });
    });
});