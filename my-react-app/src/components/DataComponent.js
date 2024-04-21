import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './DataComponent.css';
const DataComponent = () => {
    const [data, setData] = useState(null);
    const navigate = useNavigate();
    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/data')
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error('Error:', error));
    }, []);
    console.log(data)
    return (
        <div>
          <div className='sticky-div'>
                  <button className="submit-button" onClick={() => navigate('/')}>
                      HOME
                  </button>
          </div>
          
            {
            data ? (
                // <p>Data from Flask API: {data.message}</p>
                <div className='display-div'>
                  <p>blockchain :  </p>
                  {Object.keys(data).map(key => (
                  <div key={key} className='array-div'>
                    <p>Array {key}:</p>
                      <div className='node-div'> 
                        {data[key].map((item, index) => (
                          <li key={index}>{item}</li>
                        ))}
                      </div>
                    
                  </div>
                    )
                    )}
                </div>
            ) : (
                <p>Loading...</p>
            )}
          
            
        </div>
    );
};

export default DataComponent;
