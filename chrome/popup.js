let display = document.getElementById("display"); 
fetch('https://example-app-giap.herokuapp.com/').then(r => r.text()).then(text => {
    display.innerHTML = text; 
}); 