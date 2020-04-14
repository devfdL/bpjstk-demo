Webcam.set({
    width: 620,
    height: 440,
    image_format: 'png',
    jpeg_quality: 100
});

Webcam.attach( '#my_camera' );
  
function take_snapshot() {

    // take snapshot and get image data
    
    Webcam.snap( function(data_uri) {
    // display results in page
    //console.log(data_uri);
    document.getElementById("facesign").value = data_uri;
    document.getElementById('results').innerHTML = 
    '<img src="'+data_uri+'" download/>';
    } );
    
}

