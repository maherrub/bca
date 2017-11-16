$("#slide").hover(function () {
  $("#navrow").fadeIn(200);
  $("#slide").toggleClass("slidebarOpen");
});

$("#slide").mouseleave(function () {
  $("#navrow").fadeOut(0);
});


$("#slidel").hover(function () {
  $("#navrowl").fadeIn(200);
  $("#slidel").toggleClass("slidebarOpenl");
});

$("#slidel").mouseleave(function () {
  $("#navrowl").fadeOut(0);
});

$("#slider").hover(function () {
  $("#navrowr").fadeIn(200);
  $("#slider").toggleClass("slidebarOpenr");
});

$("#slider").mouseleave(function () {
  $("#navrowr").fadeOut(0);
});