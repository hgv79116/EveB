import React, { useState } from "react";
import Home from "./Home";
import Events from "./Events";
import Account from "./Account";

const home = "Home", account = "Account", events = 'Events'

function Menu(props) { 
  const setSection = props.setSection
  return (
    <nav class="navbar navbar-expand-lg navbar-light bg-light px-2">
      <a class="navbar-brand" href="#" onClick = {() => setSection(home)}>EveB</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-item nav-link" href="#" onClick = {() => setSection(home)}>Home</a>
          <a class="nav-item nav-link" href="#" onClick = {() => setSection(events)}>My events</a>
          <a class="nav-item nav-link" href="#" onClick = {() => setSection(account)}>My account</a>
          <a class="nav-item nav-link disabled" href="#">Disabled</a>
        </div>
      </div>
    </nav>
  )
}

export default function MainPage() {
  const [section, setSection] = useState("Home")
  return (
    <div class = "container-fluid">
      <Menu setSection={setSection}/>
      <div class= "container-fluid w-100 h-100 d-flex justify-content-center align-items-center">
        {
          section == home && 
          <Home/>
        }
        {
          section == events && 
          <Events/>
        }
        {
          section == account && 
          <Account/>
        }
      </div>
    </div>
  )
}

