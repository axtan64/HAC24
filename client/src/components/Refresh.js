import { useEffect, useRef, useState } from 'react';
import refresh from '../assets/refresh-ccw.png';
import RequestWrapper from './RequestWrapper';

function Refresh({ flowchartRef, setFileName }) {
    const [b64img, setb64img] = useState(`data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNgYAAAAAMAASsJTYQAAAAASUVORK5CYII=`);
    const [clickable, setClickable] = useState(true);
    const refreshRef = useRef(null);

    useEffect(() => {
        flowchartRef.current.setAttribute("src", `data:image/png;base64, ${b64img}`);
    }, [b64img])

    async function click() {
        if(!clickable) return false;
        setClickable(false);

        let res = await new RequestWrapper('http://localhost:5000/get_base64_image')
        .then((res) => {
            if(res.status == 200) return res.data;
            return Promise.reject(res)
        })
        .then((res) => {
            setFileName(res.fileName);
            setClickable(true);
            return res.image;
        })
        .catch(() => {
            setClickable(true);
            console.log("Refresh get_base64_image error");
        })

        setb64img(res);
    }

    return (
        <button id="refresh" ref={refreshRef} onClick={click}>
            <img src={refresh} alt="Refresh button" width="24px" style={{imageRendering: 'pixelated'}}></img>
        </button>
    )
}

export default Refresh;