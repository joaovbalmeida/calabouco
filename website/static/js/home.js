// Shadow for Nav Bar
$(window).scroll(function() {
  if ($(window).scrollTop() > 10) {
      $('#top').addClass('top-nav-collapse');
  } else {
      $('#top').removeClass('top-nav-collapse');
  }
});

// Tab Bar Navigation
$('body').scrollspy({
  target: '#navbarCollapse',
  offset: 50
});

// Auto Close Responsive Navbar on Click
function close_toggle() {
  if ($(window).width() <= 768) {
    $('.navbar-collapse a').on('click', function () {
      $('.navbar-collapse').collapse('hide');
    });
  }
  else {
    $('.navbar .navbar-inverse a').off('click');
  }
}
close_toggle();
$(window).resize(close_toggle);

// Back to top
$(window).scroll(function() {
  if ($(this).scrollTop() > 200) {
    $('.back-to-top').fadeIn(200);
  } else {
    $('.back-to-top').fadeOut(200);
  }
});

$('.back-to-top').on('click',function(event) {
  event.preventDefault();
  $('html, body').animate({
    scrollTop: 0
  }, 400);
  return false;
});

// Preloader
$(window).on('load', function() {
  $('#preloader').fadeOut();
});

//WOW Scroll spy
var wow = new WOW({
  mobile: false
});
wow.init();