$(document).ready(function(){
    /**
     * face_detected is a JSON containing information
     * about face detection on each camera.
     */
    var faces_detected;

    var checkIfDetected = function() {
        $.ajax({
          url: '/face_detected',
          dataType: 'json',
          type: 'get',
          success: function(e) {
            faces_detected = e; 
            $('#detection').html('Detecting faces.');
          },
          error: function(e) {
            $('#detection').html('Error: Something went wrong! Check your connection to the host!');
          },
        });
      }

    window.setInterval(function(){
        checkIfDetected();
        $('#camera_info').empty();
        $.each(faces_detected, function(k, v) {
          if(v == true){
            var message = "Face/s detected!";
            $('#camera_info').append('<li class="warning">Camera #' + k + ': ' + message +'</li>')
          }
          else{
            var message = "No faces detected."
            $('#camera_info').append('<li class="normal">Camera #' + k + ': ' + message +'</li>')
          }
          
        });
    }, 1000);

});