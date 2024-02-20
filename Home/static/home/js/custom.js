$(document).ready(function(){
    $(".dateinput").datepicker({ changeYear:true, changeMonth: true})

    var events = $('#events');
        var table = $('#example').DataTable( {
            dom: 'Bfrtip',
            select: true,
             buttons: [
                {
                 text: 'Get selected data',
                 action: function () {
                     var count = table.rows( { selected: true } ).count();
  
                     events.prepend( '<div>'+count+' row(s) selected</div>' );
                 }
             }
            ]
        } );

});