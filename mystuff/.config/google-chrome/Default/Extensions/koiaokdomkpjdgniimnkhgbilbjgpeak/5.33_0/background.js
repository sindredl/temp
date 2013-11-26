var manifest = chrome.runtime.getManifest();

/* GOOGLE ANALYTICS */
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-7929453-158']);
_gaq.push(['_trackPageview']);
(function() {
	var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
	ga.src = 'https://ssl.google-analytics.com/ga.js';
	var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
function track(name,label){
	if(label == ""){
		label = manifest.version;
	}
	_gaq.push(["_trackEvent", manifest.name,name,label]);
}

/* HANDLING MESSAGES */
chrome.extension.onMessage.addListener(function(request, sender, sendResponse) {
	if(request.method == "track"){
		track(request.name,request.label);
	}
	if(request.method == "getSettings"){
		sendResponse(localStorage);
	}
});

/* HANDLING STARTUP */
chrome.runtime.onStartup.addListener(function(){
	track("Started",manifest.version);
});

/* HANDLING UPDATES */
chrome.runtime.onInstalled.addListener(function(details) {
	if(details.reason == "install"){
		track("Installed",manifest.version);
        chrome.tabs.create({"url": "http://www.autohdforyoutube.com/pages/installed.htm",active:true});
	}
	else{
		track("Updated",manifest.version);
	}
	if(!localStorage.installTime){
		localStorage.installTime = Math.round(Date.now() / 1000);
	}
});

/* HANDLING PAGE ACTION */
chrome.tabs.onUpdated.addListener(function(tabId,changeInfo,tab){
	if(tab.url.indexOf("youtube.com/watch") > 0 && changeInfo.status == "complete"){
		chrome.pageAction.show(tabId);
	}
});

try{
	chrome.runtime.setUninstallUrl("http://www.autohdforyoutube.com/pages/uninstalled.htm");
}
catch(e){
}
