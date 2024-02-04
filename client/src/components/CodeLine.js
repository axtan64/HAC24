import { useEffect, useRef, useState } from 'react';
import { lineInit } from '../helpers/lineInit.js';

function CodeLine() {
    const [tokens, setTokens] = useState(null);
    const lineRef = useRef(null);

    let numTokens = 0;

    useEffect(() => {
        lineInit(lineRef);
    }, [lineRef])

    useEffect(() => {
        
    }, [tokens])

    return (
        <textarea className='codeLine' ref={lineRef} wrap="none"></textarea>
    )
}

export default CodeLine;