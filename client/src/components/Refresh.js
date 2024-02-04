import refresh from '../assets/refresh-ccw.png';

function Refresh() {
    return (
        <button id="refresh">
            <img src={refresh} alt="Refresh button" width="24px" style={{imageRendering: 'pixelated'}}></img>
        </button>
    )
}

export default Refresh;