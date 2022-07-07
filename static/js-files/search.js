function change(){
    var search = document.getElementById("Search_select");
    var but = document.getElementById("but");
    var ser = document.getElementById("ser");
    var p = document.getElementById("para")
    if (search.value === ""){
        but.disabled = true;
        ser.disabled = true;
        p.innerHTML = "Enter:";
    }
    else{
        but.disabled = false;
        ser.disabled = false;
        p.innerHTML = "Enter "+search.value+": ";
    }
}