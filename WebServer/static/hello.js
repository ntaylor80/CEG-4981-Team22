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

      if (status == "success"){
        document.getElementById("lot").innerHTML = "Showing information for lot " + id;
        document.getElementById("studentParking").value = data.student;
        document.getElementById("facultyParking").value = data.faculty;
        document.getElementById("scanTime").value = data.date;
      }else{
          alert("connection error")
      }


    },
  dataType: "json"
});
}
window.onload = function() {
    $('.' + 'dropdown-menu' + ' button').each(function () {
        var oid = this.id;
        document.getElementById(this.id).onclick = function () {
            request_lot(oid);
        }

    });
};