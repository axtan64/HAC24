import { useEffect, useState } from 'react';
import CodeLine from './CodeLine.js';

const lineSize = 18;

function CodeEditor({ editorRef }) {
    return (
        <div className = "editorContainer">
            <p className="highEmphasis" style={{
                width: "100%", 
                fontWeight: "bold",
                fontSize: `${lineSize}px`,
                textAlign: 'center'
            }}>Code Editor</p>
            <div style={{width: '100%', display: 'inline-flex'}}>
                <table cellSpacing="0" cellPadding="0" border="0" style={{
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
                            let lines = [];
                            for(let lineNum = 0; lineNum < 25; lineNum++) {
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
                <CodeLine editorRef={editorRef}></CodeLine>
            </div>
        </div>
    )
}

export default CodeEditor;