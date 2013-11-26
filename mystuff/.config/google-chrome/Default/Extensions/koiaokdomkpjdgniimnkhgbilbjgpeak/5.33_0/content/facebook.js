function track(name){
	var trackEvent = {method:"track",name:name,label:""};
	chrome.runtime.sendMessage(trackEvent,function(){});
}
$(document).ready(function(){
	renderSidebar();
	$("body").on("click",".MoshBar",function(){
		var href = $(this).data("href");
		window.open(href);
		track("ItemClicked");
	});
	$("body").on("click",".WidgetClose",function(){
		$(".MoshBar").hide();
		track("WidgetClosed");
		return false;
	});
});

function renderSidebar(){
	if((window.location.pathname.length < 3) && ($(".userContentWrapper").length > 2)){
		$.getJSON("https://s3.amazonaws.com/www.autohdforyoutube.com/beta/content.js",function(items){
			if(items.length > 0){
				var item = items[Math.floor(Math.random() * items.length)];
				var content = "<div class='MoshBar' data-href='" + item.url + "'><div class='WidgetClose'>x</div><div class='WidgetTitle'>You might like:</div>";
				content += "<img class='MoshImage'  src='" + item.image + "'></img>";
				content += "<div class='MoshTitle'>" + item.title + "</div></div>";
				$(".userContentWrapper").eq(2).after(content);
				track("ItemRendered");
			}
		});
	}
	else{
		console.log("Not Applied");
	}
}