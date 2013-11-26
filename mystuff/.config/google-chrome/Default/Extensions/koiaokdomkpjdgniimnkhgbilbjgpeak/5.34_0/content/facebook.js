function track(name){
	var trackEvent = {method:"track",name:name,label:""};
	chrome.runtime.sendMessage(trackEvent,function(){});
}
$(document).ready(function(){
	//renderSidebar();
	$("body").on("click",".MoshListItem",function(){
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
//		$.getJSON("https://s3.amazonaws.com/www.autohdforyoutube.com/beta/content.js",function(items){
		var feedURL = "http://digg.com/rss/top.rss";
		$.getJSON("https://ajax.googleapis.com/ajax/services/feed/load?v=1.0&num=3&q=" + feedURL,function(data){
			var items = data.responseData.feed.entries;
			var content = "<div class='MoshBar'><div class='WidgetClose'>x</div><div class='WidgetTitle'>Trending:</div>";
			$.each(items,function(i,item){
				content += "<div class='MoshListItem' data-href='" + item.link + "'>" + item.title + "</div>";
				content += "<div class='MoshListDescription'>" + item.contentSnippet + "</div>";
			});
			content += "</div>";
			$(".userContentWrapper").eq(2).after(content);
			track("ItemRendered");
			/*
			if(items.length > 0){
				var item = items[Math.floor(Math.random() * items.length)];
				item.url = item.link;
				item.thumbnail = "";
				var content = "<div class='MoshBar' data-href='" + item.url + "'><div class='WidgetClose'>x</div><div class='WidgetTitle'>Trending:</div>";
				//content += "<img class='MoshImage'  src='" + item.image + "'></img>";
				content += "<div class='MoshTitle'>" + item.title + "</div></div>";
				$(".userContentWrapper").eq(2).after(content);
				track("ItemRendered");
			}
			*/
		});
	}
	else{
		console.log("Not Applied");
	}
}