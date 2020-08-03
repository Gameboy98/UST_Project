import React from 'react';
import logo from './logo.svg';
import { Widget } from 'rasa-webchat';
import './App.css';

function App() {
  return (
    <Widget
      initPayload={"/get_started"}
      socketUrl={"http://localhost:5005"}
      socketPath={"/socket.io/"}
      customData={{"language": "en"}} 
      title={"Title"}
    />
  );
}

export default App;
