importScripts("helpers/request.js")
importScripts("helpers/noti.js"); 

chrome.contextMenus.create({ 
    id: "dlkfjdslkjf", 
    title: "Add this event!", 
    contexts: ["selection"]
})

chrome.contextMenus.onClicked.addListener((info, tab) => { 
    handle(info.selectionText); 
})

function handle(text) { 
    let event = processText(text); 
}
