import React from "react";
import './Home.css';
import { useNavigate } from 'react-router-dom';


export default function Home(){
    const navigate = useNavigate();
    const handleClick = async (event) => {
        event.preventDefault();
        // Send input data to backend
        
        const response = await fetch('http://localhost:5000/api/menu', {
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
            
            <button className="submit-button" name="searchchain" onClick={handleClick}>
                    Display blockchain
            </button>
            
            <button className="submit-button" name="add" onClick={handleClick}>
                    Add a new block
            </button>

            <button className="submit-button" name="search" onClick={handleClick}>
                    Search details of a block
            </button>


            {/* <button className="submit-button" name="addrawmaterial" onClick={handleClick}>
                    Add Raw Material
            </button> */}
            
            
        </div>
    )
}

