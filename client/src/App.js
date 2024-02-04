import './App.css';

import CodeEditor from './components/CodeEditor';
import Flowchart from './components/Flowchart';
import Toolbar from './components/Toolbar'

function App() {
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
      <Toolbar></Toolbar>
      <CodeEditor></CodeEditor>
      <Flowchart></Flowchart>
    </div>
  )
}

export default App;
