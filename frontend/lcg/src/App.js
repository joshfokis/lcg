import React, {useState, useEffect} from 'react';
import './App.css';
import axios from 'axios';
import AgendaView from './components/agendaview';
// import ActView from './components/actview';
// import LocationView from './components/locationview';
// import EncounterView from './components/encounterview';

function App() {

  const [agenda, setAgenda] = useState([{}]);
  // const [act, setAct] = useState([{}]);
  // const [location, setLocation] = useState([{}]);
  // const [encounter, setEncounter] = useState([{}]);
  
  useEffect(() => {
    // axios.get('https://arkhamdb.com/api/public/cards/core')
    axios.get('http://localhost:8000/arkham')
      .then(res => {
        setAgenda(res.data.agenda)
        // setAct(res.data)
        // setLocation(res.data)
        // setEncounter(res.data)
      })
  });

 return (
    <div className="App">
      <AgendaView agenda={agenda} />
      {/* <ActView act={act} />
      <LocationView location={location} />
      <EncounterView encounter={encounter} /> */}
    </div>
  );
}

export default App;
