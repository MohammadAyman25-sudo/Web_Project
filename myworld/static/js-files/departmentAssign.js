$(document).ready(
function(){
    var x = $(".levels");
    var y = $(".departments")
    var z = $(".set")
    var k = $(".dep")
    for (let i = 0; i<x.length; i++){
        if(x[i].innerHTML === "Third Level"){
            y[i].disabled = false;
            z[i].disabled = false;
            y[i].value = k[i].innerHTML;
        }
        else{
            y[i].disabled = true;
            z[i].disabled = true;
            y[i].value = k[i].innerHTML;
        }
    }
});