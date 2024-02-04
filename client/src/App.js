import { useRef, useState } from 'react';
import './App.css';

import CodeEditor from './components/CodeEditor';
import Flowchart from './components/Flowchart';
import Toolbar from './components/Toolbar'

function App() {
  const flowchartRef = useRef(null);
  const editorRef = useRef(null);
  const [fileName, setFileName] = useState("");

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
      <CodeEditor editorRef={editorRef}></CodeEditor>
      <Toolbar flowchartRef={flowchartRef} editorRef={editorRef} fileName={fileName} setFileName={setFileName}></Toolbar>
      <div id="popupContainer" style={{
        position: 'absolute',
        bottom: '25%',
        transform: 'translate(-50%, 75%)',
        left: '50%',
        width: '100%',
        height: '32px'
      }}></div>
    </div>
  )
}

export default App;
