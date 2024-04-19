import React, { useState } from 'react';
// import { BrowserRouter as Router, Link, Route, Routes } from 'react-router-dom';
// import FormComponent from './FormComponent';
// Login.js

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = (e) => {
        e.preventDefault();
        // Perform login logic here

        console.log('Username:', username);
        console.log('Password:', password);
        // Reset the form
        setUsername('');
        setPassword('');


    };

    return (
        <div>
            <h2>Login Page</h2>
            <form>
                <label>
                    Username:
                    <input type="text" name="username" value={username} onChange={(e) => setUsername(e.target.value)} />
                </label>
                <br />
                <label>
                    Password:
                    <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                </label>
                <br />
                <input type="submit" value="Submit" onClick={handleLogin} />
            </form>
            
        {/* <Router>
            <Routes>
                <Route path="/" element={ */}
                    {/* <div>
                        <Link to="/FormComponent">
                            <button>Submit</button>
                        </Link>
                    </div> */}
                
                {/* <Route path="/FormComponent" element={<FormComponent />} />
            </Routes>
        </Router> */}
        </div>
    );
};

export default Login;
