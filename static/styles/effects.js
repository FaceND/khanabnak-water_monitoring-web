// Create a script element
var script = document.createElement("script");
script.src = "https://code.jquery.com/jquery-3.3.1.min.js";
script.type = "text/javascript";

// Define a callback function to be executed once jQuery is loaded
script.onload = function () {
  jQuery(function ($) {
    var doAnimations = function () {
      // Calc current offset and get all animatables
      var offset = $(window).scrollTop() + $(window).height(),
        $animatables = $(".animatable");

      // Unbind scroll handler if we have no animatables
      if ($animatables.length == 0) {
        $(window).off("scroll", doAnimations);
      }

      // Check all animatables and animate them if necessary
      $animatables.each(function (i) {
        var $animatable = $(this);
        if ($animatable.offset().top + $animatable.height() - 20 < offset) {
          $animatable.removeClass("animatable").addClass("animated");
        }
      });
    };

    // Hook doAnimations on scroll, and trigger a scroll
    $(window).on("scroll", doAnimations);
    $(window).trigger("scroll");
  });
};

// Append the script element to the head of the document
document.head.appendChild(script);
