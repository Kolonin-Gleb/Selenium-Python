//chrome.windows.create({url: chrome.extension.getURL('background.html'), 'type': 'popup'});
function updateForm(m) {
    document.getElementById("x").innerHTML = m.x;
    document.getElementById("y").innerHTML = m.y;
}

chrome.runtime.onMessage.addListener(function(message, sender, sendRepsonse) {
    //console.log(message)
    updateForm(message);
    sendResonse({
        data: "Msg received"
    });
});