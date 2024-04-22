import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './FormComponent.css';

const FormComponent = () => {
    const [descr, setDescr] = useState('');
    const [prevAddr, setPrevAddr] = useState('');
    const [productId, setProductId] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        // Send input data to backend
        const response = await fetch('http://localhost:5000/api/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ descr, prevAddr, productId })
        });
        if (response.ok) {
            const data = await response.json();  // Parse the JSON response
            console.log(data);  // Log the data for debugging
        } else {
            console.error('Error:', response.status, response.statusText);
        }
        navigate('/');
    };

    return (
        <div className='form-body'>
            <form onSubmit={handleSubmit}>
                <label>Description</label>
                <input className='input-box'
                    type="text"
                    value={descr}
                    onChange={(e) => setDescr(e.target.value)}
                    placeholder="Enter description"
                />
                <br/>
                <label>Previous Blocks</label>
                <input className='input-box'
                    type="text"
                    value={prevAddr}
                    onChange={(e) => setPrevAddr(e.target.value)}
                    placeholder="Enter previous address"
                />
                <br/>
                <label>Product ID</label>
                <input className='input-box'
                    type="text"
                    value={productId}
                    onChange={(e) => setProductId(e.target.value)}
                    placeholder="Enter product id"
                />

                <br/>
                <button className='submit-button' type="submit">
                    Update blockchain
                </button>
            </form>
        </div>
    );
};

export default FormComponent;
