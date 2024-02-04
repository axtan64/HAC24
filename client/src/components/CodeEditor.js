import { useState } from 'react';
import CodeLine from './CodeLine.js';

function CodeEditor() {
    const [numLines, setNumLines] = useState(1);
    let linePos = 1; // the line the user is editing
    let lines = [];

    return (
        <div className = "editorContainer">
            <p className="highEmphasis" style={{
                width: "100%", 
                fontWeight: "bold",
                fontSize: '18px',
                textAlign: 'center'
            }}>Code Editor</p>
            <div style={{width: '100%'}}>
                <table style={{
                    paddingLeft: '16px',
                    display: 'inline-block'
                }}>
                    <tbody>
                        <tr>
                            <th style={{
                                width: '16px'
                            }}></th>
                        </tr>
                        {(() => {
                            for(let lineNum = 0; lineNum < 32; lineNum++) {
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