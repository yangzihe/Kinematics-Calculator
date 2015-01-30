function submit() {
    console.log("hi")
    var a = document.getElementById('acceleration');
    var x = document.getElementById('displacement');
    var v0 = document.getElementById('initVelocity');
    var v = document.getElementById('velocity');
    var t = document.getElementById('time');
    $.ajax({
        type: "POST",
        url: "/",
        data : { 
            'a': a.value,
            'x': x.value,
            'v0': v0.value,
            'v': v.value,
            't': t.value
        },
        success: function(results) {
            document.getElementById("answer").innerHTML = results;
        }
    });
}