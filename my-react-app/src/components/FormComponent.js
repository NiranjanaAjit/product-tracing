import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './FormComponent.css';

const FormComponent = () => {
    const [descr, setDescr] = useState('');
    const [prevAddr, setPrevAddr] = useState('');
    const [productId, setProductId] = useState('');
    const [port, setPort] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        // Send input data to backend
        const response = await fetch('http://localhost:5000/api/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ descr, prevAddr, productId, port})
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
            
                <div className='label-inputs'>
                    <label className='inputs'>Description</label>
                    <br/>
                    <br/>
                

                    <label className='inputs'>Used</label>
                    <br/>
                    <br/>

                    <label className='inputs'>Product ID</label>
                    <br/>
                    <br/>
                <label className='inputs'>Port</label>
                    <br/>
                <br/>
                </div>
                <div>
                <form onSubmit={handleSubmit}>
                <input className='input-box'
                    type="text"
                    value={descr}
                    onChange={(e) => setDescr(e.target.value)}
                    placeholder="Enter description"
                />
                <br/>
                <br/>

                <input className='input-box'
                    type="text"
                    value={prevAddr}
                    onChange={(e) => setPrevAddr(e.target.value)}
                    placeholder="Enter product IDs used (space seperated)"
                />
                <br/>
                <br/>
                
                <input className='input-box'
                    type="text"
                    value={productId}
                    onChange={(e) => setProductId(e.target.value)}
                    placeholder="Enter product id"
                />
                <br/>
                <br/>
                <input className='input-box'
                    type="text"
                    value={port}
                    onChange={(e) => setPort(e.target.value)}
                    placeholder="Enter port"
                />
                <br/>
                <br/>
                <button className='update-button' type="submit">
                    Update blockchain
                </button>
                </form>
                </div>

                
            
        </div>
    );
};

export default FormComponent;
