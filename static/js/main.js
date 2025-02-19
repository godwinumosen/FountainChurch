(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();

    // Sticky Navbar with Scroll Effect
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.navbar').addClass('scrolled');  // Add the "scrolled" class when scrolled past 300px
        } else {
            $('.navbar').removeClass('scrolled');  // Remove the "scrolled" class when back at the top
        }
    });

    // Initiate the wowjs
    new WOW().init();

})(jQuery);
