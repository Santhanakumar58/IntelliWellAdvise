$(document).ready (function () {
    $('submit').on('click', function(){
        $selectedassetname = $('selectedassetname').val();
        $selectedblockname = $('selectedblockname').val();
        $selectedfieldname = $('selectedfieldname').val();
        $selectedlayername = $('selectedlayername').val();
        $selectedsublayername = $('selectedsublayername').val();

        if($selectedassetname =="" || $selectedblockname =="" || $selectedfieldname=="" ||
        $selectedlayername == "" || $selectedsublayername=="")
        {
            alert("Please complete the fields");
        }
        else 
        {
            $.ajax ({
                type:"POST",
                url:'selectedfgi/insert',
                data: {
                    selectedassetname : $selectedassetname,
                    selectedblockname : $selectedblockname,
                    selectedfieldname : $selectedfieldname,
                    selectedlayername : $selectedlayername,
                    selectedsublayername: $selectedsublayername,
                    csrfmiddlewaretoken: $('input[name=csfrmiddlewaretoken]').val()
                },
                success : function (){
                    alert('Save Data');
                    $('#selectedassetname').val('');
                    $('#selectedblockname').val('');
                    $('#selectedfieldname').val('');
                    $('#selectedlayername').val('');
                    $('#selectedsublayername').val('');
                    window.location = "/";
                }
            });
        }
    });
});




