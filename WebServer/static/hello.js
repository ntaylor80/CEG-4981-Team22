function sayHello() {
   alert("Hello World")
}

function request_lot(id){
$.ajax({
  type: "POST",
  contentType: "application/json; charset=utf-8",
  url: "/availability",
  data: JSON.stringify({lot: id}),
  success:  function(data, status){
        alert("Data: " + data.test + "\nStatus: " + status);
    },
  dataType: "json"
});
alert("request");
}
window.onload = function() {
    $('.' + 'dropdown-menu' + ' button').each(function () {
        var oid = this.id;
        document.getElementById(this.id).onclick = function () {
            request_lot(oid);
        }

    });
};