$(document).ready(function(){
    var x = $('#login');
    if(x.html() === "login"){
        var y = $("#homePage");
        y.attr("href","#");
        y = $("#homePageIcon")
        y.attr("href","#");
        y = $("#active_inactive");
        y.attr("href","#");
        y = $("#search");
        y.attr("href","#");
        y = $("#add");
        y.attr("href","#");
        y = $("#Greetings").html("");
        x.attr("href","login_screen");
    }else{
        var y = $("#homePage");
        y.attr("href","/");
        y = $("#homePageIcon")
        y.attr("href","/");
        y = $("#active_inactive");
        y.attr("href","active-inactive");
        y = $("#search");
        y.attr("href", "search");
        y = $("#add");
        y.attr("href", "addStudentPage");
        y = $("#Greetings").html("Welcome, ");
        x.attr("href", "#");
    }   
});
function postForm(){
    var y = $("#login");
    if(y.html() === "logout"){   
        var form = $("#form");
        form.attr("action", "log_out");
        form.submit();
    }
}

function Login_form(id){
    var x = $("#login").html();
    if(x === "login"){
        var y = $("#form");
        var i = $("#post");
        i.attr("value", id);
        y.attr("action", "whoLogedin");
        y.submit();
    }
}