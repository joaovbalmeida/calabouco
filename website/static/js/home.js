//Shadow for Nav Bar
$(window).scroll(function() {
  if ($(window).scrollTop() > 10) {
      $('#top').addClass('top-nav-collapse');
  } else {
      $('#top').removeClass('top-nav-collapse');
  }
});

//Tab Bar Navigation
$('body').scrollspy({
  target: '#navbarCollapse',
  offset: 50
});