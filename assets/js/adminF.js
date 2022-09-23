

function adminF(a){
    var viewid = a.id;
  
    var mp = document.getElementById("pannel-in");
    if (typeof closeview === 'undefined' || closeview === null) {
    var seat = new XMLHttpRequest();
    seat.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            mp.innerHTML = this.responseText;
        }
    };
    seat.open("POST", "addbook");
    seat.send();
  }
  document.getElementById("mySidenav").style.width = "0%";

}