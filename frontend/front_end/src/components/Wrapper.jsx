import React, { useEffect, useState } from 'react';
import { MainPage, AuthPage} from "./index.jsx";
import loadUser from "../api/request.js"

export default function Wrapper() { 
    const [user, setUser] = useState(null);
    useEffect(() => { 
        setUser(loadUser()); 
    })
    return ( // return value need a wrapper element
        <div> 
            {user !== null && <MainPage user={user} update={setUser}></MainPage>}
            {user === null && <AuthPage update={setUser}></AuthPage>}
        </div>
    )
}

