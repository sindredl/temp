var ArrayUtils = {
	random:function(array){
		// returns a random element of an array.
		return array[Math.floor(Math.random() * array.length)];
	}
}

var StringUtils = {
	containsArray:function(source,needles){
		for (var i = 0; i < needles.length; i++) {
			if (source.search(needles[i]) > -1) {
				return true;
			}
		}
		return false;
	}
}


var DataUtils = {
	put:function(key, object) {
	    localStorage[key] = JSON.stringify(object);
	},
	get:function(key, defaultValue) {
	    var result;
	    if (localStorage[key]) {
	        result = JSON.parse(localStorage[key]);
	    }
	    else{
	    	result = defaultValue;
	    }
	    return result;
	}
}

function getHost(url){
	var parser = document.createElement('a');
	parser.href = url;
	return parser.hostname;
}