// Handling submission event.
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

// AJAX for posting.
function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "/edit_info", // the endpoint
        type : "POST", // http method
        data : {
            'first_name':$('#first_name').val(),
            'sur_name':$('#sur_name').val(),
            'birth_date':$('#birth_date').val(),
            'bio':$('#bio').val(),
            'contacts':$('#contacts').val(),
            'photo': $('#photo').val(),
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            // remove the value from the input
            $('#first_name').val(''); 
            $('#sur_name').val(''); 
            $('#birth_date').val(''); 
            $('#bio').val('');
            $('#contacts').val('');
            $('#photo').val(''); 
            console.log(json); // log the returned json to the console
            console.log(json.status); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').css("display", "block"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

// Handling image preview.
function handleFiles(files) {

    preview.innerHTML = ''
    for (var i = 0; i < files.length; i++) {
        var file = files[i];
        var imageType = /^image\//;

        if (!imageType.test(file.type)) {
          continue;
        }

        var img = document.createElement("img");
        img.classList.add("obj");
        img.file = file;
        preview.appendChild(img); // Assuming that "preview" is the div output where the content will be displayed.

        var reader = new FileReader();
        reader.onload = (function(aImg) { return function(e) { aImg.src = e.target.result; }; })(img);
        reader.readAsDataURL(file);
    }
}


// CSRF Protection code.
$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});