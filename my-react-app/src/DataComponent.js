import React, { useEffect, useState } from 'react';

const DataComponent = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/data')
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div>
            {data ? (
                <p>Data from Flask API: {data.message}</p>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default DataComponent;
