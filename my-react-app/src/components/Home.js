import React from "react";
import './Home.css';
import { useNavigate } from 'react-router-dom';


export default function Home(){
    const navigate = useNavigate();
    const handleClick = async (event) => {
        event.preventDefault();
        // Send input data to backend
        
        const response = await fetch('http://localhost:5000/api/button', {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
    
            body: JSON.stringify({ input: event.target.name})
        });
        
        if (response.ok) {
            const data = await response.json();  // Parse the JSON response
            console.log(data);  // Log the data for debugging
        } else {
            console.error('Error:', response.status, response.statusText);
        }
        
        console.log(event.target.name);
       // const data = await response.json();
        // console.log(data);
        navigate(`/${event.target.name}`);
        
    }

    return(

        <div className="home">
            <h1>Product Tracing System</h1>
            {/* {console.log('hello')} */}
            {/* <p>Click on the links below to navigate</p> */}
            {/* <ul>
                <li><a href="/display">Display blockchain</a></li>
                <li><a href="/add">Add a new block</a></li>

                <li><a href="/login">Login</a></li>
            </ul> 
            <a href="/display">
            <a href="/add">
            </a>
            </a>

            */}
            <button className="submit-button" name="display" onClick={handleClick}>
                    Display blockchain
            </button>
            
            <button className="submit-button" name="add" onClick={handleClick}>
                    Add a new block
            </button>
            
            
        </div>
    )
}

