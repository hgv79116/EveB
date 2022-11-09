const ParseEventId = "eventParser"; 
const dataBaseName = "eventDataBase"; 
const objectStoreName = "eventStore"; 

chrome.runtime.onInstalled.addListener(async () => {
  createContextMenusItem(); 
});

function createContextMenusItem() { 
  chrome.contextMenus.create({
    id: ParseEventId,
    title: "Parse event",
    contexts: ['selection']
  }); 
}

chrome.contextMenus.onClicked.addListener( (info, tab) => { 
  if(info.menuItemId === ParseEventId) { 
    console.log("Received click", Date.now()); 
    process(info.selectionText); 
  }
}); 

function process(text) { 
  console.log("start processing", Date.now()); 
  console.log("processing text: ", text); 
  fetch("https://example-app-giap.herokuapp.com/update", { 
    method: "POST", 
    body: text
  }).then((res) => res.text()).then((text) => console.log(text)); 
  chrome.notifications.create('NOTFICATION_ID', {
    type: 'basic',
    iconUrl: 'resources/random.png',
    title: 'parsing event!',
    message: 'parsing event!',
    priority: 2,
  }); 
  console.log("done notifying"); 
}

// chrome.runtime.onMessage.addListener( (message, sender, sendResponse) => { 
//   if(message == "get-all-data") { 
//     sendResponse(get_all_data()); 
//   }
// }); 

// dsfdsg;

// kdkfjldsjf; 
