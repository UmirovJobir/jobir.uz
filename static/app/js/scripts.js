/* Description: Custom JS file */

(function($) {
    "use strict"; 
	
    /* Navbar Scripts */
    // jQuery to collapse the navbar on scroll
    $(window).on('scroll load', function() {
		if ($(".navbar").offset().top > 60) {
			$(".fixed-top").addClass("top-nav-collapse");
		} else {
			$(".fixed-top").removeClass("top-nav-collapse");
		}
    });
    
	// jQuery for page scrolling feature - requires jQuery Easing plugin
	$(function() {
		$(document).on('click', 'a.page-scroll', function(event) {
			var $anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $($anchor.attr('href')).offset().top
			}, 600, 'easeInOutExpo');
			event.preventDefault();
		});
    });

    // offcanvas script from Bootstrap + added element to close menu on click in small viewport
    $('[data-toggle="offcanvas"], .navbar-nav li a:not(.dropdown-toggle').on('click', function () {
        $('.offcanvas-collapse').toggleClass('open')
    })

    // hover in desktop mode
    function toggleDropdown (e) {
        const _d = $(e.target).closest('.dropdown'),
            _m = $('.dropdown-menu', _d);
        setTimeout(function(){
            const shouldOpen = e.type !== 'click' && _d.is(':hover');
            _m.toggleClass('show', shouldOpen);
            _d.toggleClass('show', shouldOpen);
            $('[data-toggle="dropdown"]', _d).attr('aria-expanded', shouldOpen);
        }, e.type === 'mouseleave' ? 300 : 0);
    }
    $('body')
    .on('mouseenter mouseleave','.dropdown',toggleDropdown)
    .on('click', '.dropdown-menu a', toggleDropdown);


    /* Move Form Fields Label When User Types */
    // for input and textarea fields
    $("input, textarea").keyup(function(){
		if ($(this).val() != '') {
			$(this).addClass('notEmpty');
		} else {
			$(this).removeClass('notEmpty');
		}
	});
	

    /* Back To Top Button */
    // create the back to top button
    $('body').prepend('<a href="body" class="back-to-top page-scroll">Back to Top</a>');
    var amountScrolled = 700;
    $(window).scroll(function() {
        if ($(window).scrollTop() > amountScrolled) {
            $('a.back-to-top').fadeIn('500');
        } else {
            $('a.back-to-top').fadeOut('500');
        }
    });


	/* Removes Long Focus On Buttons */
	$(".button, a, button").mouseup(function() {
		$(this).blur();
	});

    /* Popup Handling */
    // Close popup on click
    $(document).on('click', '.close-popup', function() {
        $(this).closest('.popup').fadeOut();
    });

    // Auto-close popup after 10 seconds
    setTimeout(function() {
        $('.popup').fadeOut();
    }, 10000);

    /* Telegram Web App Logic */
    $(document).ready(function() {
        // Ensure the Telegram Web App is fully ready
        Telegram.WebApp.ready();
    
        const user = Telegram.WebApp.initDataUnsafe.user;
    
        if (user) {
            // Check if the element with ID 'username' is present before modifying it
            const usernameElement = document.getElementById('username');
            if (usernameElement) {
                usernameElement.textContent = "<br>" + user.first_name + " " + user.last_name;
            }
        }
        // else {
        //     document.getElementById('username').textContent = 'Гость';
        // }
    });

    /* Confirmation for Closing Telegram WebApp */
    Telegram.WebApp.onEvent('backButtonClicked', function() {
        // Show confirmation before closing the app
        let confirmation = confirm('Changes that you made may not be saved. Do you really want to close?');
        if (confirmation) {
            Telegram.WebApp.close();  // Close the app if the user confirms
        }
    });
    
    
})(jQuery);