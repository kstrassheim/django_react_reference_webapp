import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState}  from 'react';
import { Switch,  Route } from 'react-router';
import NavMenu from './NavMenu';
import NotFound from './NotFound'
import Home from './pages/Home'
import About from './pages/About'

function App(props) {
  return (
    <div className="App">
      <NavMenu />
      <Switch>
        <Route exact path='/' component={() => <Home  />} />
        <Route exact path='/about' component={() => <About  />} />
        <Route component={() => <NotFound  />} />
      </Switch>
    </div>
  );
}

export default App;
