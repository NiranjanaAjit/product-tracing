import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Search = () => {
    const [input, setInput] = useState('');
    // const [prevAddr, setPrevAddr] = useState('');
    // const [productId, setProductId] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        // Send input data to backend
        const response = await fetch('http://localhost:5000/api/searchblock', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ input })
        });
        if (response.ok) {

            const data = await response.json();  // Parse the JSON response
            console.log(data);  // Log the data for debugging
        } else {
            console.error('Error:', response.status, response.statusText);
        
        }
        navigate('/blockdetails');
    };

    return (
        <div className='form-body'>
                      <div className='sticky-div'>
                  <button className="home-button" onClick={() => navigate('/')}>
                      HOME
                  </button>
          </div>
            
                <div className='label-inputs'>
                    <label className='inputs'>BlockNumber</label>
                    <br/>
                    <br/>
                </div>
                <div>
                <form onSubmit={handleSubmit}>
                <input className='input-box'
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Enter block number"
                />
                <br/>
                <br/>
                <button className='update-button' type="submit">
                    Search for block
                </button>
                </form>
                </div>

                
            
        </div>
    );
};

export default Search;
