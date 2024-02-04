import { useEffect, useRef, useState } from 'react';
import play from '../assets/play2.png';
import RequestWrapper from './RequestWrapper';

function Play({ editorRef }) {
    const [clickable, setClickable] = useState(true);

    async function click() {
        if(!clickable) return false;
        setClickable(false);

        await new RequestWrapper('http://localhost:5000/receive_data', {method: 'post', data: {
            editorText: editorRef.current.value,
            fileName: 'bruh'
        }})
        .then((res) => {
            if(res.status == 200) return res.data;
            return Promise.reject(res)
        })
        .then((res) => {
            setClickable(true);
            return res.image;
        })
        .catch(() => {
            setClickable(true);
            console.log("Play error");
        })
    }

    return (
        <button id="play" onClick={click}>
            <img src={play} alt="Run button" width="24px" style={{imageRendering: 'pixelated'}}></img>
        </button>
    )
}

export default Play;