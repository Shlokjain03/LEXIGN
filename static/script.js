let cameraOn = false;

function toggleCamera() {
    const videoStream = document.getElementById("videoStream");
    const placeholder = document.getElementById("cameraPlaceholder");
    const button = document.getElementById("toggleCameraBtn");

    if (cameraOn) {
        // Turn camera OFF
        videoStream.style.display = "none";
        videoStream.src = "";
        placeholder.style.display = "flex";
        button.textContent = "Start Camera";
        cameraOn = false;
    } else {
        // Turn camera ON
        videoStream.src = videoStream.getAttribute("data-src") || videoStream.src;
        videoStream.style.display = "block";
        placeholder.style.display = "none";
        button.textContent = "Stop Camera";
        cameraOn = true;
    }
}
