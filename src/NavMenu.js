import React, { useState } from 'react';
import { Collapse, Navbar, NavbarBrand, NavbarToggler, NavItem, NavLink } from 'reactstrap';
import { Link } from 'react-router-dom';
import './NavMenu.css';

function NavMenu(props) {
    const [collapsed, setCollapsed] = useState(true);
    const toggleNavbar = () => { setCollapsed(!collapsed)  }
    return (
        <header>
            <Navbar className={"navbar-expand-sm navbar-toggleable-sm"}>
                <div className="container-fluid">
                    <NavbarBrand>
                        <img src="static/logo192.png" width="32" height="32" alt="Logo" style={{ marginTop: '-4px', marginRight:'7px'}} />Django Web Page
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
