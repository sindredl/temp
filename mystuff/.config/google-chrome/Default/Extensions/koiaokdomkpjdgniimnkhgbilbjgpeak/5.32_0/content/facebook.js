$(document).ready(function(){
	$("body").on("click","a",function(){
		var href = $(this).attr("href");
		if(href.indexOf("youtube.com/watch") > 0){
			var trackEvent = {method:"track",name:"FBYT",label:""};
			chrome.runtime.sendMessage(trackEvent,function(){});
		}
	})
});