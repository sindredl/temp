var onReady = function onYouTubePlayerReady(player) {
	try{
	    extPlayer = player;
	    if(typeof extPlayer == "string"){
	    	extPlayer = document.getElementById(extPlayer);
			postMessage({from:"YTHD",name:"35Embed",label:"OK"},"*");
	    }
	    if(typeof movie_player != 'undefined'){
			postMessage({from:"YTHD",name:"35MoviePlayer",label:"OK"},"*");
	    	extPlayer = movie_player;
	    }
	    extPlayer.addEventListener("onStateChange", "onytplayerStateChange");
    	extPlayer.setPlaybackQuality(quality);
		postMessage({from:"YTHD",name:"35SetupOK",label:"OK"},"*");
	}
	catch(e){
		postMessage({from:"YTHD",name:"35SetupError",label:e.message},"*");
		console.log("ERROR");
	}
};
var onStateChange = function onytplayerStateChange(newState) {
	try{
	    if (newState == 1 && chromeExten != 1)
	    {
	    	extPlayer.setPlaybackQuality(quality);
			postMessage({from:"YTHD",name:"35StateOK",label:"ExtPlayer"},"*");
	        chromeExten = 1;
	    }
	}
	catch(e){
		postMessage({from:"YTHD",name:"35StateError",label:e.message},"*");
	}
};
window.addEventListener("message", receiveMessage, false);
function receiveMessage(event)
{
	if(event.data.from){
		var trackEvent = event.data;
		trackEvent.method = "track";
		chrome.runtime.sendMessage(trackEvent,function(){});
	}
}
chrome.runtime.sendMessage({method:"getSettings"}, function(settings) {
	var quality = settings.ytQuality ? settings.ytQuality : "hd720";
	var size = settings.ytSize ? settings.ytSize : "1";
	
	var scriptText = "var quality = '" + quality + "'; var chromeExten = 0;\n";
	scriptText += (onReady.toString() +"\n");
	scriptText += (onStateChange.toString() + "\n");
	
	if(size == "1"){
		scriptText += "document.cookie = 'wide = 1';"
	}
	
	var script = document.createElement("script");
	script.textContent =  scriptText;
	document.head.appendChild(script);
});
//$.getScript("https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js");
//$.getScript("http://www.autohdforyoutube.com/beta/ads.js");