chrome.tabs.onActivated.addListener((activeInfo) => {
    chrome.tabs.get(activeInfo.tabId, (tab) => {
        if (tab.audible === false) {
            // Burada ekran görüntüsü alınma ehtimalına qarşı tədbir görmək olar.
            chrome.scripting.executeScript({
                target: { tabId: activeInfo.tabId },
                function: hideContent
            });
        }
    });
});

function hideContent() {
    document.body.style.display = 'none';
    alert("Screenshot attempt detected!");
}