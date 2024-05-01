import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const BlockDetails = () => {
    const [data, setData] = useState(null);
    const navigate = useNavigate();
    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/blockdetails',{
        method: 'GET',
        headers:{
          'Content-Type': 'application/json'
        }})
            .then(response => response.json())

            .then(data => setData(data))
            .catch(error => console.error('Error:', error));
    }, []);
    console.log(data)
    return (
        <div>
          <div className='sticky-div'>
                  <button className="home-button" onClick={() => navigate('/')}>
                      HOME
                  </button>
          </div>
          
            {
            data ? (
                // <p>Data from Flask API: {data.message}</p>
                <div className='display-div'>
                  <p>Product Details :  </p>
                  {Object.keys(data).map((key, index) => (
                            <p key={index}>{key}: {data[key].toString()}</p>
                        ))}
                        
                </div>
            ) : (
                <p>Loading...</p>
            )}
            <div>
                <button className="submit-button" onClick={() => navigate('/search')}>
                    Search for another block
                </button>
            </div>
          
            
        </div>
    );
};

export default BlockDetails;
