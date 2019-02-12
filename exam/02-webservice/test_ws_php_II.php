<script src="script/jquery-3.1.0.min.js">
    function get_webservice(){
        alert("test naja")
        var body_input = {
            msg : "test using webservice"
        };
        $.ajax({
            async : false,
            type : "POST",
            url : "http://70b51db4.ngrok.io/test-deploy",
            data : JSON.stringify(body_input),
            contentType : "application/json; charset=utf-8",
            dataType : "json",
            success : success,
            failure : function (response){
                alert(response.d);
            }
        });

        function sucess(response){
            alert(response.d);
        }
    }
    get_webservice();
</script>