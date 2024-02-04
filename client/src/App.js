import { useRef } from 'react';
import './App.css';

import CodeEditor from './components/CodeEditor';
import Flowchart from './components/Flowchart';
import Toolbar from './components/Toolbar'

function App() {
  const flowchartRef = useRef(null);

  return ( 
    <div className="App">
      <div style={{
        position: 'absolute',
        width: '100%',
        height: '64px',
        backgroundColor: '#1f1f1f'
      }}></div>
      <div style={{
        position: 'absolute',
        width: '100%',
        height: '16px',
        backgroundColor: '#000000'
      }}></div>
      <Flowchart flowchartRef={flowchartRef}></Flowchart>
      <Toolbar flowchartRef={flowchartRef}></Toolbar>
      <CodeEditor></CodeEditor>
    </div>
  )
}

export default App;
