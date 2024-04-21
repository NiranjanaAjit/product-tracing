import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './FormComponent.css';

const FormComponent = () => {
    const [inputValue, setInputValue] = useState('');
    const navigate = useNavigate();
    const handleSubmit = async (event) => {
        event.preventDefault();
        // Send input data to backend
        const response = await fetch('http://localhost:5000/api/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ input: inputValue })
        });
        const data = await response.json();
        // Process response data as needed
        console.log(data);
        navigate('/')
    };

    return (
        <form onSubmit={handleSubmit}>
            <input className='input-box'
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder="Enter data"
            />
            <br/>
            <button className='submit-button' type="submit">
                Update blockchain
                {/* <a href='/display'></a> */}
            </button>
        </form>
    );
};

export default FormComponent;
