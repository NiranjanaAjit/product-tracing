import React from "react";
import './Home.css';

export default function Home(){
    return(

        <div className="home">
            <h1>Product Tracing System</h1>
            {/* {console.log('hello')} */}
            {/* <p>Click on the links below to navigate</p> */}
            {/* <ul>
                <li><a href="/display">Display blockchain</a></li>
                <li><a href="/add">Add a new block</a></li>

                <li><a href="/login">Login</a></li>
            </ul> */}
            <a href="/display">
                <button className="submit-button">
                    Display blockchain
                </button>
            </a>
            
            <a href="/add">
                <button className="submit-button">
                    Add a new block
                </button>
            </a>
        </div>
    )
}

