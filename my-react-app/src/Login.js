// Login.js
import React from 'react';

const Login = () => {
    // Your login page content and functionality
    return (
        <div>
            <h2>Login Page</h2>
            
            <form>
                <label>
                    Username:
                    <input type="text" name="username" />
                </label>
                <br />
                <label>
                    Password:
                    <input type="password" name="password" />
                </label>
                <br />
                <input type="submit" value="Submit" />
            </form>
        </div>
    );
};

export default Login;
