document.addEventListener("DOMContentLoaded", () => { 
    document.getElementById("content").innerHTML = "Loading..."; 
    fetch("http://127.0.0.1:5000/extension/home")
        .then(response => response.text())
        .then(text => { 
            document.getElementById("content").innerHTML = text; 
        });     
    }
); 