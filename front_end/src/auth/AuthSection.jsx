import React, { useState } from 'react';
import { useEffect } from 'react';
import { login, registerUser } from '../api';

const loginMode = "Login", registerMode = "Register"
function reverseMode(formMode) { 
    return formMode === loginMode? registerMode: loginMode
}

function FormPage(props) { 
    const setUser = props.setUser
    const [formMode, changeFormMode] = [props.formMode, props.changeFormMode]
    
    const defaultFlashMessage = ""
    const registerFailed = "Username or email is invalid"
    const registerSucceeded = "Registration succeeded"
    const loginFailed = "Email or password is wrong"
    const [flashMessage, setFlashMessage] = useState(defaultFlashMessage)
    
    const defaultFormContent = {
        // ...(formMode == registerMode && {username: "John Doe"}), // ES6. I have not been able to use this since formContent does not change between renders
        username: "John Doe", 
        email: "johndoe@gmail.com", 
        password: "Random password"
    }

    const [formContent, setFormContent] = useState(defaultFormContent) // change this to empty as soons as not dev-ing anymore

    function handleSubmit(e) { 
        if (formMode === loginMode) { 
            let safeFormContent = formContent
            delete safeFormContent.username
            login(safeFormContent).then((result) => { 
                const [response_ok, user] = result
                if(response_ok) {
                    setUser(user)
                }
                else { 
                    setFlashMessage(loginFailed)
                }
            })   
        } 
        else { 
            console.log(formContent)
            registerUser(formContent).then(result => { 
                const response_ok = result
                if(response_ok) { 
                    setFlashMessage(registerSucceeded)
                    setFormContent(defaultFormContent)
                }
                else { 
                    setFlashMessage(registerFailed)
                }
            })
        }
        e.preventDefault(); 
    }

    function handleChange(e) { 
        const name = e.target.name, value = e.target.value
        let newFormContent = formContent
        newFormContent[name] = value
        console.log(newFormContent)
        setFormContent(newFormContent)
    }
    
    return (
        <form onSubmit={handleSubmit} onChange={handleChange} class = "rounded">
            {
                formMode === registerMode  && 
                <div class="form-group">
                    <label for="username">Username</label>
                    <input id="username" name = "username" type = "text" defaultValue = {defaultFormContent.username} placeholder = "John Doe" class="form-control"/>
                </div>
            }
            <div class="form-group">
                    <label for="email">Email</label>
                    <input id="email" name = "email" type = "email" defaultValue = {defaultFormContent.email} placeholder = "johndoe@gmail.com" class="form-control"/>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input id="password" name="password" type="password" defaultValue = {defaultFormContent.password} placeholder = "Random password" class="form-control"/>
            </div>
            <button type = "submit" class="btn btn-primary">{formMode}</button> 
        </form>    
    )
}

export default function AuthSection(props) {    
    const setUser = props.setUser

    const [formMode, setFormMode] = useState(registerMode)
    
    function changeFormMode() { 
        setFormMode(reverseMode(formMode))
    }
    
    return (
        <div>
            { 
                formMode == loginMode? 
                <FormPage setUser = {setUser} formMode={formMode} changeFormMode = {changeFormMode}/>: 
                <FormPage setUser = {setUser} formMode={formMode} changeFormMode = {changeFormMode}/>
            }
            <a onClick={() => changeFormMode()}>Back to {reverseMode(formMode)}</a>
        </div>
        // this looks super ugly, but the point is to make two sperated forms that use separated memory
    )
}