addEventListener('mousemove', (event) => {
    //console.log("content ", event.clientX, event.clientY);
    chrome.runtime.sendMessage({
        x: event.clientX,
        y: event.clientY
    }).catch(e => {
    	//console.log(e.message);
    });

});