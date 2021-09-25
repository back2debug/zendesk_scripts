//grabbing status for Connect script from statuspage-TM
	var sp = new StatusPage.page({ page : '' });
	sp.summary({
  	success: function(data) {
   	// adds the status text description
    $('.color-description').text(data.status.description);
    // update the indicator to use the right color for the dot
    $('.color-dot').addClass(data.status.indicator);
  	}
	});