function onClickedCheck() {

    var prediction = document.getElementById("modal-result");
    var title = document.getElementById("title").value;
    var author = document.getElementById("author").value;

    var url = "http://127.0.0.1:5000/predict_fake";

    $.post(url, {
        title: title,
        author: author,
    }, function(data, status) {
        var result = data.label;
        var message;

        if (result == '1') {
            message = "<h1 style='color:#ee1a1a;'>❌ FAKE ❌</h1>";
        } else {
            message = "<h1 style='color:green;'>✅ REAL ✅</h1>";
        }

        prediction.innerHTML = message;
        console.log(status);
    });
}
