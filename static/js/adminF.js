

function adminF(a){
    var viewid = a.id;
  
    var mp = document.getElementById("bookarrg");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      mp.innerHTML = this.responseText;
    }
    };


    xhttp.open("POST", "bookview");

    xhttp.send(viewid);
  }
  

