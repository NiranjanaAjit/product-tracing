import React from 'react';
// import { Link } from 'react-router-dom';
import FormComponent from './FormComponent';
import DataComponent from './DataComponent';
import { BrowserRouter as Router, Link, Route, Routes } from 'react-router-dom';
import Login from './Login';

const App = () => {
    return (
        <div>
            
            <h1>Input Form</h1>
            <FormComponent />
            <h1>Displaying blockchain</h1>
            <DataComponent />
            <Router basename='/'>
                <Link to="/login">
                    <button>Login</button>
                </Link>
                <Routes>
                    <Route path="/login" element = {<Login />} />
                        {/* <Login/> Render LoginComponent when the path is "/login" */}
                </Routes>
            </Router>

            {/* <Link to="/login">
                <button>Login</button>
            </Link> */}
        </div>
    );
};

export default App;
