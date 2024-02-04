import { useEffect, useRef, useState } from 'react';
import { lineInit } from '../helpers/lineInit.js';

function CodeLine({ editorRef }) {
    /*const lineRef = useRef(null);

    useEffect(() => {
        lineInit(lineRef);
    }, [lineRef])

    return (
        <textarea className="codeInput" rows="25" ref={lineRef}></textarea>
    )*/

    return (
        <textarea className="codeInput" rows="25" ref={editorRef}></textarea>
    )
}

export default CodeLine;