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
                  <p>blockchain :  </p>
                  {Object.keys(data).map((key, index) => (
            <div key={index}>
                <h2>Block {key}:</h2>
                {Object.entries(data[key]).map(([key, value], index) => (
                    <p key={index}>{key}: {value.toString()}</p>
                ))}
            </div>
        ))}

                  {/* {Object.keys(data).map(key => (
                  <div key={key} className='array-div'>
                    <p>Array {key}:</p>
                      <div className='node-div'> 
                        {data[key].map((item, index) => (
                          <li key={index}>{item}</li>
                        ))}
                      </div>
                    
                  </div>
                    )
                    )} */}
                </div>
            ) : (
                <p>Loading...</p>
            )}
          
            
        </div>
    );
};

export default BlockDetails;
