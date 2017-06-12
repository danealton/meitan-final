'use strict';

/*
    This file can be used as entry point for webpack!
 */
$(document).ready(function() {

  	$(document).foundation();
    // require('components/preloader/preloader.js');
    require('components/filter/filter.js');
  	require('components/cart/cart.js');

  	// Init simple slider
  	$('.js-slider-simple').slick();

    // Init responsive slider
    $("#catalog_news_slider").slick({

      // normal options...
      infinite: true,
      slidesToShow: 3,
      autoplay: true,
      arrows: true,
      prevArrow: '#catalog_news .arrow-left',
      nextArrow: '#catalog_news .arrow-right',

      // the magic
      // responsive: [{

      //     breakpoint: 1024,
      //     settings: {
      //       slidesToShow: 3,
      //       infinite: true
      //     }

      //   }, {

      //     breakpoint: 600,
      //     settings: {
      //       slidesToShow: 2,
      //       dots: true
      //     }

      //   }, {

      //     breakpoint: 300,
      //     settings: "unslick" // destroys slick

      //   }]
    });

    $("#catalog_recommend_slider").slick({
      // normal options...
      infinite: true,
      slidesToShow: 3,
      auoplay: true,
      arrows: true,
      prevArrow: '#catalog_recommend .arrow-left',
      nextArrow: '#catalog_recommend .arrow-right',
    });

    $("#last_news_slider").slick({
      // normal options...
      infinite: true,
      slidesToShow: 3,
      auoplay: true,
      arrows: true,
      prevArrow: '#last_news .arrow-left',
      nextArrow: '#last_news .arrow-right',
    });
	

  	//console.log(Cart);

  	//$('.js-add-cart').on('click', Cart.addItem([1,2,3,4]));


});
