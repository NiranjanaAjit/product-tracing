import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const SearchBlockchain = () => {
    // const [input, setInput] = useState('');
    const [port, setPort] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        // Send input data to backend
        const response = await fetch('http://localhost:5000/api/searchchain', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ port })
        });
        if (response.ok) {

            const data = await response.json();  // Parse the JSON response
            console.log(data);  // Log the data for debugging
        } else {
            console.error('Error:', response.status, response.statusText);
        
        }
        navigate('/display');
    };

    return (
        <div className='form-body'>
                      <div className='sticky-div'>
                  <button className="home-button" onClick={() => navigate('/')}>
                      HOME
                  </button>
          </div>
            
                <div className='label-inputs'>
                    <label className='inputs'>Port</label>
                    <br/>
                    <br/>
                </div>
                <div>
                <form onSubmit={handleSubmit}>
                <br/>
                <br/>
                <input className='input-box'
                    type="text"
                    value={port}
                    onChange={(e) => setPort(e.target.value)}
                    placeholder="Enter port"
                />
                <br/>

                <button className='update-button' type="submit">
                    Get blockchain
                </button>
                </form>
                </div>

                
            
        </div>
    );
};

export default SearchBlockchain;
