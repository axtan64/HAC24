import flowchart1 from '../assets/flowcharts/flowchart1.png';

function Flowchart() {
    return (
        <div className="flowchartContainer">
            <p className="highEmphasis" style={{
                width: "100%", 
                fontWeight: "bold",
                fontSize: '18px',
                textAlign: 'center'
            }}>Flowchart</p>
            <img src={flowchart1} alt="Flowchart 1" style={{
                position: 'absolute',
                left: '50%',
                top: '50%',
                transform: 'translate(-50%, -50%)'
            }}>
            </img>
        </div>
    )
}

export default Flowchart;