$(document).ready(function () {

    $('#inputText').change(check_textInput)
    $('#inputText').on('input',check_textInput)

    function check_textInput(){
        var text = $("#inputText").val();
        if(text.length > 0){
            $(".btn").prop("disabled", false);
        }else{
            $(".btn").prop("disabled", true);
        }
    }

    $('#downloadBtn').click(function(e){
        var serializedData = $('#textForm').serialize();
        $.ajax({
            type: "post",
            url: "/download",
            data: serializedData,
            success: function (response) {
                console.log(response);
                window.location.href = response.download_url
            }
        });
    })
});