import React, { useState } from 'react';
import { login } from '../api';
const loginMode = "Login", registerMode = "Register"; 
console.log(process.env)


export default function AuthSection(props) {
    const setUser = props.setUser
    const [mode, setMode] = useState(loginMode)
    const reverseMode = mode === loginMode? registerMode: loginMode

    const [formContent, setFormContent] = useState({})

    function handleSubmit(e) { 
        login(formContent).then((result) => { 
            const [response_ok, user] = result
            if(response_ok) {
                setUser(user)
            }
        })    
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
        <div>
            <form onSubmit={handleSubmit} onChange={handleChange}>
                {mode === registerMode && <label>
                    Username
                    <input name = "username" type = "text" defaultValue = "John Doe"></input>
                </label>}
                <label>
                    Email
                    <input name = "email" type = "email" defaultValue = "johndoe@gmail.com"></input>
                </label>
                <label>
                    Password
                    <input name = "password" type = "text" defaultValue = "Random password"></input>
                </label>
                <button type = "submit">Submit</button> 
            </form>    

            <button onClick={() => setMode(reverseMode)}>Back to {reverseMode}</button>
        </div>  
    )
}