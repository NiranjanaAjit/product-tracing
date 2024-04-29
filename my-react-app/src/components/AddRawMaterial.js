import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const AddRawMaterial = () => {
    const [rawmaterial, setrawmaterial] = useState('');
    const [productid, setproductid] = useState('');
    const navigate = useNavigate();
    const handleSubmit = async (event) => {
        event.preventDefault();
        // Send input data to backend
        const response = await fetch('http://localhost:5000/api/addrawmaterial', {
            method: 'POST',
            cors: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ rawmaterial, productid})
        });
        if (response.ok) {

            const data = await response.json();  // Parse the JSON response
            console.log(data);  // Log the data for debugging
        } else {
            console.error('Error:', response.status, response.statusText);
        
        }
        navigate('/receipt');
    };

    return (
        <div className='form-body'>
                      <div className='sticky-div'>
                  <button className="home-button" onClick={() => navigate('/')}>
                      HOME
                  </button>
          </div>
            
                <div className='label-inputs'>
                    <label className='inputs'>RawMaterial</label>
                    <br/>
                    <br/>
                    <label className='inputs'>Product ID</label>
                </div>

                <div>
                <form onSubmit={handleSubmit}>
                <input className='input-box'
                    type="text"
                    value={rawmaterial}
                    onChange={(e) => setrawmaterial(e.target.value)}
                    placeholder="Raw Material"
                />
                <br/><br/>
                <input className='input-box'
                    type="text"
                    value={productid}
                    onChange={(e) => setproductid(e.target.value)}
                    placeholder="Enter product id"
                />
                <br/>
                <br/>
                
                <button className='update-button' type="submit">
                    Add Raw Material
                </button>
                </form>
                </div>

                
            
        </div>
    );
};

export default AddRawMaterial;
