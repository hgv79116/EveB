import React, { useState } from 'react';
import { LoginPage, MainPage, RegisterPage} from "./index.jsx";

export default function Wrapper() { 
    const [page, setPage] = useState("LoginPage");
    return ( // return value need a wrapper element
        <div> 
            {page == "LoginPage" && <LoginPage update={setPage}></LoginPage>}
            {page == "RegisterPage" && <RegisterPage update={setPage}></RegisterPage>}
            {page == "MainPage" && <MainPage update={setPage}></MainPage>}
        </div>
    )
}

