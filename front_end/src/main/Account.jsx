import React, { useState } from "react";
import { useEffect } from "react";
import { getUserInfo, updateUserInfo } from "../api";
const updateInfo = "updateInfo", updatePassword = "updatePassword"

function capitalize(name) { 
    return name.charAt(0).toUpperCase() + name.slice(1)
}

function UpdateInfoForm(props) {     
    const defaultFlashMessage = ""
    const updateSucceeded = "Saved successfully"
    const updateFailed = "Save failed"
    const [flashMessage, setFlashMessage] = useState(defaultFlashMessage)
    const [userInfo, setUserInfo] = useState({})
    
    useEffect(() => { 
        getUserInfo().then((result) => {
            const [response_ok, user_info] = result
            console.log(result)
            if(!response_ok) { 
                setFlashMessage("Failed to load user info")
            }
            else { 
                setUserInfo(user_info)
            }
        })
    }, [])

    function handleSubmit(e) { 
        console.log(userInfo)
        updateUserInfo(userInfo).then(result => { 
            const response_ok = result
            if(response_ok) { 
                setFlashMessage(updateSucceeded)
            }
            else { 
                setFlashMessage(updateFailed)
            }
        })
        e.preventDefault(); 
    }

    function handleChange(e) { 
        const name = e.target.name, value = e.target.value
        let newUserInfo = userInfo
        newUserInfo[name] = value
        console.log(newUserInfo)
        setUserInfo(newUserInfo)
    }
    
    let other_form_groups = []
    for(let key of Object.keys(userInfo)) { 
        if(key == "username" 
            || key == "password" 
            || key == "email"
            || key == "id"
            ) continue
            other_form_groups.push(
            <div class="form-group">
                <label for={key}>{capitalize(key)}</label>
                <input id={key} name={key} type="text" defaultValue = {userInfo[key]} class="form-control"/>
            </div>
        )
    }

return (
        <form onSubmit={handleSubmit} onChange={handleChange} class = "rounded">
            <div class="form-group">
                <label for="username">Username</label>
                <input id="username" name = "username" type = "text" defaultValue = {userInfo.username} class="form-control"/>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input id="email" name = "email" type = "email" defaultValue = {userInfo.email} class="form-control"/>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input id="password" name="password" type="password" defaultValue = {userInfo.password} class="form-control"/>
            </div>
            {other_form_groups}
            <button type = "submit" class="btn btn-primary">Update</button> 
        </form>    
    )

    return "hello"
}

export default function Account() {

  
  return <UpdateInfoForm/>
}

