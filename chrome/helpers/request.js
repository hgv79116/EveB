const serverUrl = "http://127.0.0.1:5000/event"; 
function processText(text) { 
    fetch(serverUrl + "/parse", { 
        method: "POST", 
        headers: {
            'content-Type': 'text/html'
        },
        body: text
    })
        .then(response => response.json())
        .then(info => { 
            if(info.status == "Success") { 
                askConfirmation(info.event); 
                console.log(info.event)
            }
            else if(info.status == "Login required") { 
                reportLoginRequired(); 
            }
        }); 
}
