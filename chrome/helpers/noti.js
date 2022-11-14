function reportLoginRequired() { 
    chrome.notifications.create("Login required", { 
        type: "basic", 
        iconUrl: "assets/icon.png", 
        title: "EveB",
        message: "You have not logged in! Click on the icon in extension bar to login.", 
        buttons: [
            { title: "Login" }, 
            { title: "Cancel"}
        ]
    }, () => { 
        console.log("Last error:", chrome.runtime.lastError); 
    })
}

function askConfirmation(event) { 
    chrome.notifications.create("Confirmation", { 
        type: "basic", 
        iconUrl: "assets/icon.png", 
        title: "EveB",
        message: `Do you want to add this event?\n Event name: ${event.name}\n Time: ${event.time}\n Location: ${event.location}`,
        buttons: [
            { title: "Add" }, 
            { title: "Cancel"}
        ]
    }, () => { 
        console.log("Last error:", chrome.runtime.lastError); 
    })
}