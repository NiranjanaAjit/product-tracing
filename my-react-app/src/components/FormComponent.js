import React, { useState } from 'react';

const FormComponent = () => {
    const [inputValue, setInputValue] = useState('');

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
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder="Enter data"
            />
            <button type="submit">Submit</button>
        </form>
    );
};

export default FormComponent;
