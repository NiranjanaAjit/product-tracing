import { Link } from 'react-router-dom';

export default function Home(){
    return(

        <div>
            <h1>Product Tracing System</h1>
            {console.log('hello')}
            <p>Click on the links below to navigate</p>
            <ul>
                
                <li><a href="/display">Display blockchain</a></li>
                <li><a href="/add">Add a new block</a></li>
                <li><a href="/login">Login</a></li>
            </ul>
        </div>
    )
}

