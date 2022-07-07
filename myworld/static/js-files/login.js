function check() {
  var email = document.getElementById("email").value;
  var x = new XMLHttpRequest();
  x.onload = function(){
    if(x.responseText=='ok'){
      window.location.replace("homepage");
    }
    else{
      window.alert(
            "Employee not found   email:  ahmed@gmail.com   password: 12345678"
          );
    }

  }
  x.open("POST","../validate",false);
  x.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  x.send("email="+email);
}
