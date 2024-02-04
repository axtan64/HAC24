import Refresh from '../components/Refresh.js';

import play from '../assets/play2.png';

function Toolbar({ flowchartRef }) {
    return (
        <div id="toolbar" style={{display: 'inline-block', alignItems: 'center', paddingTop: '8px'}}>
            <li style={{display: 'inline-block', alignItems: 'center'}}>
                <span className="highEmphasis" style={{
                    paddingRight: '12px',
                    fontWeight: "bold",
                    fontSize: '20px',
                    left: '0%',
                    top: '50%',
                    transform: '(0%, 0%)'
                }}>Flowchart</span>
                <span className="mediumEmphasis" style={{
                    border: '2px solid white',
                    borderRadius: '4px',
                    padding: '3px'
                }}>
                    ICHack24
                </span>
            </li>

            <li style={{display: 'inline-block', position: 'absolute', right: '32px'}}>
                <Refresh flowchartRef={flowchartRef}></Refresh>
                <button id="play" style={{transform: "translate(0, 0)"}}>
                    <img src={play} alt="Run button" width="24px" style={{imageRendering: 'pixelated'}}></img>
                </button>
            </li>
        </div>
    )
}

export default Toolbar;