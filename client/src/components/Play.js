import { createRoot } from 'react-dom/client';
import React, { useEffect, useRef, useState } from 'react';
import play from '../assets/play2.png';
import RequestWrapper from './RequestWrapper';
import Popup from './Popup.js';
import reactDom from 'react-dom';

function Play({ editorRef, fileName }) {
    const [clickable, setClickable] = useState(true);

    async function click() {
        if(!clickable) return false;
        setClickable(false);

        await new RequestWrapper('http://localhost:5000/receive_data', {method: 'post', data: {
            editorText: editorRef.current.value,
            fileName
        }})
        .then((res) => {
            if(res.status == 200) return res.data;
            return Promise.reject(res)
        })
        .then((res) => {
            setClickable(true);
            /*const root = createRoot(document.getElementById("popupContainer"));
            let newPopup = (<Popup txt=""></Popup>);
            root.render(newPopup);*/
            //editorRef.current.value = "";
            
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