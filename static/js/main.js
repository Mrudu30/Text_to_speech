$(document).ready(function () {

    $('#inputText').change(check_textInput)
    $('#inputText').on('input',check_textInput)

    function check_textInput(){
        var text = $("#inputText").val();
        if(text.length > 0){
            $(".submitBtn").prop("disabled", false);
        }else{
            $(".submitBtn").prop("disabled", true);
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

    $('#generateBtn').click(function(e){
        $.ajax({
            type: "post",
            url: "/sample_file",
            success: function (response) {
                console.log(response)
                $('#inputText').val(response.file_text)
                check_textInput()
            }
        });
    })
});