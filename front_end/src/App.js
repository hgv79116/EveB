import React, { useState } from "react";
import MainPage from "./main/MainPage"
import AuthPage from "./auth/AuthPage"
import { loadUser } from "./api"
import { useEffect } from "react";

export default function App() {
  const [user, setUser] = useState(null)
  

  useEffect(() => { 
    loadUser().then((result)  => { 
      const [status, user] = result
      if(user != null) {
        setUser(user)
      }
    })
  }, [])

  return (
    user == null? 
      <AuthPage setUser = {setUser}></AuthPage>: 
      <MainPage user = {user} setUser = { setUser }></MainPage>
  )
}

