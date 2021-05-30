import React, { useState } from 'react';
import { Collapse, Navbar, NavbarBrand, NavbarToggler, NavItem, NavLink } from 'reactstrap';
import {Dropdown, DropdownButton} from 'react-bootstrap';
import { Link } from 'react-router-dom';
import './NavMenu.css';
import $ from 'jquery'

function NavMenu(props) {
    const [collapsed, setCollapsed] = useState(true);
    const toggleNavbar = () => { setCollapsed(!collapsed)  }
    const btnCollapseClick = () => { $("#optionsToolbar").slideToggle("fast"); }
    const dropDownSelect = (obj, event) => { props.setRedditChannelCallback(event.target.value); }
    return (
        <header>
            <Navbar className={"navbar-expand-sm navbar-toggleable-sm" + ((!!props.darkMode) ? " navbar-dark" : "")} light={true}>
                <div className="container-fluid">
                    <NavbarBrand onClick={btnCollapseClick}>
                        <img src="static/favicon192.png" width="32" height="32" alt="Logo" style={{ marginTop: '-4px', marginRight:'7px'}} />Reddit-Mining
                    </NavbarBrand>
                    <NavbarToggler onClick={toggleNavbar} className="mr-2" />
                    <Collapse className="d-sm-inline-flex flex-sm-row-reverse" isOpen={!collapsed} navbar>
                    <ul className="navbar-nav flex-grow">
                        <NavItem><NavLink tag={Link} to="/">Home</NavLink></NavItem>
                        <NavItem><NavLink tag={Link} to="/about">About</NavLink></NavItem>
                    </ul>
                    </Collapse>
                </div>
            </Navbar>
        </header>
    );
}

export default NavMenu;
