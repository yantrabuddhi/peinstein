(function(ext) {
	
	var descriptor = {
    	blocks: [
			[' ', 'Say %s', 'sayThis', 'txt', 'txt'],
          		[' ', 'Walk', 'walk'],
          		[' ', 'Go Crazy', 'crazy'],
			[' ', 'connect','connect']
    	],
    	txt: 'Hello'
  	};
  
  	ext._shutdown = function() {};
  	
  	ext._getStatus = function() {
  		return {status: 2, msg: 'Device connected'}
  	};
  	
  	ext.sayThis = function(txt) {
		$.get('http://127.0.0.1:8080/say/'+txt)
  	};
	ext.walk = function() {
		$.get('http://127.0.0.1:8080/walk')
	}; 	
	ext.crazy = function() {
		$.get('http://127.0.0.1:8080/crazy')
	};
	ext.connect = function() {
		$.get('http://127.0.0.1:8080/connect')
	};

    ScratchExtensions.register("Einstein", descriptor, ext);
})({});
