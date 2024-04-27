import React, { useEffect , useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Receipt.css'

const Receipt = () => {
    const navigate = useNavigate();
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/receipt',{
        method: 'GET',
        headers:{
          'Content-Type': 'application/json'
        }})
            .then(response => response.json())

            .then(data => setData(data))
            .catch(error => console.error('Error:', error));
    }, []);
    console.log(data)
    return(
        <div>
            <div className='sticky-div'>
                  <button className="home-button" onClick={() => navigate('/')}>
                      HOME
                  </button>
            </div>
            
            <h1 className='receipt-heading'>Receipt</h1>
            <h2> Successfully added to blockchain !!! </h2>

            {
                data ? (
                    // <p>Data from Flask API: {data.message}</p>
                    <div className='receipt-div'>
                        {Object.keys(data).map((key, index) => (
                            <p key={index}>{key}: {data[key]}</p>
                        ))}
                    </div>
                ) : (
                    <p>Loading...</p>
                )
            }

        </div>
    )

}

export default Receipt;
