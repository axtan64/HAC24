export const lineInit = function(editorRef) {
    let editor = editorRef.current;
    if(editor.getAttribute("initiated")) return;
    editor.setAttribute("initiated", true);
    
    function input(txt) {
        let tokens = /\w/g.exec(txt);
        console.log(tokens);
    }

    editorRef.current.addEventListener('keyup', (e) => {
        input(e.target.value);
    })
}