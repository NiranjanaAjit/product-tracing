import React from 'react';
import { BrowserRouter as Router, Routes , Route} from "react-router-dom";
import FormComponent from './components/FormComponent';
import DataComponent from './components/DataComponent';
import Login from './components/Login';
import Home from './components/Home';
import Receipt from './components/Receipt';
import Search from './components/Search';
import BlockDetails from './components/BlockDetails';
import AddRawMaterial from './components/AddRawMaterial';
import SearchBlockchain from './components/SearchBlockchain';



const App = () => {
    return (
        <Router>
        <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/login" element={<Login />}></Route>
            <Route path="/display" element={<DataComponent />}></Route>
            <Route path="/add" element={<FormComponent />}></Route>
            <Route path="/receipt" element={<Receipt />}></Route>
            <Route path="/search" element={<Search />}></Route>
            <Route path="/blockdetails" element={<BlockDetails/>}></Route>
            <Route path="/addrawmaterial" element={<AddRawMaterial/>}></Route>
            <Route path="/searchchain" element = {<SearchBlockchain/>}></Route>
        </Routes>
        </Router>




        // <Router>
        //     <Routes>
        //         <Route path="/" element={
        //             <div>
        //                 <h1>Input Form</h1>
        //                 <FormComponent />
        //                 <h1>Displaying blockchain</h1>
        //                 <DataComponent />
        //                 <Link to="/login">
        //                     <button>Go to Login</button>
        //                 </Link>
        //             </div>
        //         } />
        //         <Route path="/login" element={<Login />} />
        //     </Routes>
        // </Router>
    );
};

export default App;
