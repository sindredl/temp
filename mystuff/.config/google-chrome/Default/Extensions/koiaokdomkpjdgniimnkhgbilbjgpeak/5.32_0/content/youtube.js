var onReady = function onYouTubePlayerReady(player) {
	try{
	    extPlayer = player;
	    if(typeof movie_player != 'undefined'){
		    movie_player.addEventListener("onStateChange", "onytplayerStateChange");
	    	movie_player.setPlaybackQuality(quality);
			postMessage({from:"YTHD",name:"30SetupOK",label:"MoviePlayer"},"*");
	    }
	    else{
	    	// if(extPlayer != " ")
		    extPlayer.addEventListener("onStateChange", "onytplayerStateChange");
	    	extPlayer.setPlaybackQuality(quality);
			postMessage({from:"YTHD",name:"30SetupOK",label:"ExtPlayer"},"*");
	    }
	}
	catch(e){
		postMessage({from:"YTHD",name:"30SetupError",label:e.message},"*");
		console.log("ERROR");
		console.log(e);
	}
};
var onStateChange = function onytplayerStateChange(newState) {
	try{
	    if (newState == 1 && chromeExten != 1)
	    {
		    if(typeof movie_player != 'undefined'){
		    	movie_player.setPlaybackQuality(quality);
				postMessage({from:"YTHD",name:"30StateOK",label:"MoviePlayer"},"*");
	    	}
	    	else{
		    	extPlayer.setPlaybackQuality(quality);
				postMessage({from:"YTHD",name:"30StateOK",label:"ExtPlayer"},"*");
	    	}
	        chromeExten = 1;
	    }
	}
	catch(e){
		//console.log("ONS ERROR: " + e.message);
		postMessage({from:"YTHD",name:"30StateError",label:e.message},"*");
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