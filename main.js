$('#gradelist').change(function() {
  if (($(this).val() === 'de') || ($(this).val() === 'C')) {
        // Do something for option "b"
               $('.Open').addClass('active');
                $('.MembersOnly, .Members, .Lords, .LordsOnly, .Apeople, .Bpeople, .Memberlords').removeClass('active');
				if ($('#recesslist').val() === 'no') {
					$('.recessall').addClass('active');
				}
				if (($('#timelist').val() >= 12) && ($('#timelist').val() <= 14)) {
					$('.12to15').removeClass('active')
				}
				if (($('#timelist').val() >= 12) && ($('#timelist').val() <= 28)) {
					$('.A12to8').removeClass('active')
				}
				
  }
  else if ($(this).val() === 'B') {
        // Do something for option "b"
               $('.Bpeople').addClass('active');
                $('.Open').addClass('active');
                $('.MembersOnly, .Members, .Lords, .LordsOnly, .Apeople, .Memberlords').removeClass('active');
				if ($('#recesslist').val() === 'no') {
					$('.recessall').addClass('active');
				}
				if (($('#timelist').val() >= 12) && ($('#timelist').val() <= 14)) {
					$('.12to15').removeClass('active')
				}
				if (($('#timelist').val() >= 12) && ($('#timelist').val() <= 28)) {
					$('.A12to8').removeClass('active')
				}
                
  }
  else if ($(this).val() === 'A') {
        // Do something for option "b"
               $('.Open, .Apeople, .Bpeople, .A12to8').addClass('active');
                $('.MembersOnly, .Members, .Lords, .LordsOnly, .Memberlords').removeClass('active');
				if ($('#recesslist').val() === 'no') {
					$('.recessall').addClass('active');
				}
                
  }
  else if ($(this).val() === 'mem') {
        // Do something for option "b"
               $('.MembersOnly, .Members, .Open, .Apeople, .Bpeople, .Members12to8, .Memberlords').addClass('active');
			   $('.LordsOnly').removeClass('active'); 
			   if (($('#timelist').val() >= 12) && ($('#timelist').val() <= 20)) {
					$('.Members12to8, .Lords').removeClass('active');
			   }
  }
  else if ($(this).val() === 'peer') {
        // Do something for option "b"
               $('.Open, .Apeople, .Bpeople, .Lords, .LordsOnly, .Memberlords').addClass('active');
			   $('.MembersOnly').removeClass('active'); 
				if (($('#timelist').val() >= 12) && ($('#timelist').val() <= 20)) {
					$('.A12to8').removeClass('active');
			   }
  }
});

$('#recesslist').change(function() {
if ($(this).val() === 'no') {
                $('.recessall').addClass('active');
  }
else if (($(this).val() === 'yes') && (($('#gradelist').val() === 'peer') || ($('#gradelist').val() === 'mem'))) {
                $('.recessall').addClass('active');
}
else {
		$('.recessall').removeClass('active');
}
});

$('#timelist').change(function() {
if ((($('#timelist').val() >= 12) && ($('#timelist').val() <= 14)) && (($('#gradelist').val() === 'de') || ($('#gradelist').val() === 'C') || ($('#gradelist').val() === 'B'))) {
                $('.12to15').removeClass('active');
  }
if ((($('#timelist').val() < 12) || ($('#timelist').val() > 14)) && (($('#gradelist').val() === 'de') || ($('#gradelist').val() === 'C') || ($('#gradelist').val() === 'B'))) {
                $('.12to15').addClass('active');
  }
if (($('#timelist').val() < 12) && (($('#gradelist').val() === 'de') || ($('#gradelist').val() === 'C') || ($('#gradelist').val() === 'B') || ($('#gradelist').val() === 'peer'))) {
                $('.A12to8').addClass('active');
  } 
if (($('#timelist').val() >= 12) && (($('#gradelist').val() === 'de') || ($('#gradelist').val() === 'C') || ($('#gradelist').val() === 'B') || ($('#gradelist').val() === 'peer'))) {
                $('.A12to8').removeClass('active');
  }  
});

$('#timelist, #recesslist, #gradelist').change(function() {
	var countofrooms = $('.active').length
	$('#roomcount').text("You can enter " + countofrooms + " rooms at this time");
});