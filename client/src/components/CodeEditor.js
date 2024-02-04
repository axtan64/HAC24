import { useEffect, useState } from 'react';
import CodeLine from './CodeLine.js';

const lineSize = 18;

function CodeEditor() {
    const [numLines, setNumLines] = useState(1);
    let maxLines = 1;
    let linePos = 1; // the line the user is editing
    let lines = [];

    useEffect(() => {

    }, [numLines])

    return (
        <div className = "editorContainer">
            <p className="highEmphasis" style={{
                width: "100%", 
                fontWeight: "bold",
                fontSize: `${lineSize}px`,
                textAlign: 'center'
            }}>Code Editor</p>
            <div style={{width: '100%'}}>
                <table cellspacing="0" cellpadding="0" border="0" style={{
                    paddingLeft: '16px',
                    display: 'inline-block',
                    borderCollapse: 'collapse'
                }}>
                    <tbody>
                        <tr>
                            <th style={{
                                width: '16px'
                            }}></th>
                        </tr>
                        {(() => {
                            for(let lineNum = 0; lineNum < 100; lineNum++) {
                                lines.push(
                                    <tr className="editorrow" key={lineNum}>
                                        <td className="code_linenum">{lineNum + 1}</td>
                                    </tr>
                                )
                            }
                            return lines;
                        })()}
                    </tbody>
                </table>
                <textarea className="codeInput"></textarea>
            </div>
        </div>
    )
}

export default CodeEditor;