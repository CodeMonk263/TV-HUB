import Routes from "./Routes";

import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';

ReactDOM.render(
    <Router forceRefresh={true}>
        <div className="App">
            <Routes />
        </div>
    </Router>,
    document.getElementById('app')
);