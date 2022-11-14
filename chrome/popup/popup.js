document.addEventListener("DOMContentLoaded", () => { 
    fetch("http://127.0.0.1:5000/extension/load_user")
        .then(response => response.json())
        .then(info => { 
            if(info.logged) { 
                document.getElementById("welcome").innerHTML = `Welcome back, ${info.username}`;
            }
            else {
                console.log("login link: "); 
                document.getElementById("welcome").innerHTML = "Click <a href='' id = 'login'>here</a> to log in";
                document.getElementById("login").addEventListener("click", () => { 
                    chrome.tabs.create({url:`${info.login_link}`}); 
                })
            } 
        });     
        console.log("ended: "); 
    }
); 
