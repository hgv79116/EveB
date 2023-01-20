import React, { useState } from "react";
import { Home } from "./Home";
import { PastEvents, UpcomingEvents, CreateEvent} from "./Events";
import { ChangePassword, ChangeInfo, Setting} from   "./Account";

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

const modes = { 
  home: 'home', 
  events: { 
    upcomingEvents: 'upcomingEvents', 
    pastEvents: 'pastEvents', 
    createEvent: 'createEvent'
  }, 
  account: { 
    changePassword: 'changePassword', 
    changeInfo: 'changeInfo', 
    setting: 'setting', 
  }
}

function Menu(props) { 
  const setUser = props.setUser
  const setSection = props.setSection
  
  return (
    <Navbar className="navbar-expand-lg navbar-light bg-light px-2 w-100">
      <Navbar.Brand onClick = {() => setSection(modes.home)}>EveB</Navbar.Brand>
      <Navbar.Toggle data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" />
      <Navbar.Collapse className="collapse" id="navbarNavAltMarkup">
        <Nav>
          <Nav.Link onClick = {() => setSection(modes.home)}>Home</Nav.Link>
          
          <NavDropdown title="My Events">
            
            <NavDropdown.Item onClick={() => setSection(modes.events.upcomingEvents)}> 
              Upcoming events 
            </NavDropdown.Item>
            
            <NavDropdown.Item onClick={() => setSection(modes.events.pastEvents)}> 
              Past events
            </NavDropdown.Item>

            <NavDropdown.Divider />

            <NavDropdown.Item onClick={() => setSection(modes.events.createEvent)}> 
              Create a new event 
            </NavDropdown.Item>

          </NavDropdown>
          
          <NavDropdown title="My Account">
            <NavDropdown.Item onClick={() => setSection(modes.account.changeInfo)}> 
              Change information
            </NavDropdown.Item>
            
            <NavDropdown.Item onClick={() => setSection(modes.account.changePassword)}> 
              Change password
            </NavDropdown.Item>

            <NavDropdown.Item onClick={() => setSection(modes.account.setting)}> 
              Settings 
            </NavDropdown.Item>

            <NavDropdown.Divider />

            <NavDropdown.Item onClick={() => setUser(null)}> 
              Logout 
            </NavDropdown.Item>
          </NavDropdown>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  )
}

export default function MainPage(props) {
  const [section, setSection] = useState(modes.home)
  const user = props.user
  const setUser = props.setUser

  let Section = null
  switch(section) { 
    case modes.home: 
      Section = <Home/>
      break
    case modes.events.pastEvents:  
      Section = <PastEvents/>
      break
    case modes.events.upcomingEvents: 
      Section = <UpcomingEvents/>
      break
    case modes.events.createEvent: 
      Section = <CreateEvent/>
      break
    case modes.account.changeInfo: 
      Section = <ChangeInfo/>
      break
    case modes.account.changePassword: 
      Section = <ChangePassword/>
      break
    case modes.account.setting: 
      Section = <Setting/>
      break
  }
  return (
    <div class = "container-fluid">
      <Menu setSection={setSection} setUser = {setUser}/>
      <div class= "container-fluid w-100 h-100 d-flex justify-content-center align-items-center">
        {Section}
      </div>
    </div>
  )
}

