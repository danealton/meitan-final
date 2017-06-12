;



var Cart = (function() {

 	var products = [];

  	// public methods
	return {
	    
	    getItemsCount: function() {
	      return products.length;
	    },

	    getItems: function(e) {
	  //   	e.preventDefault();

		 //    return products.map(function(product) {
			// 	console.log(product);
			// });
	    },

	    addItem: function(e) {

	    	e.preventDefault();

	    	var product = $(e.currentTarget).parents('.catalog-item');

	    	products.push(product.prop('id'));

	    	console.log(Cart.getItemsCount());
	    },

      removeItem: function(e) {
        console.log(e);
        var cart = e.currentTarget;

      }

  	}
})();

var cartAJAXUrls = {
  'add' : 'cart/add.py',
  'update' : 'cart/update.py',
  'remove' : 'cart/remove.py',
};

var $cart = $('#cart');

// клик по козине товаров
$cart.on('click', function(e) {
  e.preventDefault();
  e.stopPropagation();

  $.post( cartAJAXUrls.update, data, function(response) {
    $('.cart_items').empty().html(response);
  });
});

// клик по товару в каталоге
$('.catalog-item').on('click', function(e) {
  //e.preventDefault();
});

// добавить товар в корзину
$('.catalog-item').on('click', '.js-add-cart', function(e) {
  e.preventDefault();
  e.stopPropagation();

  var $btn = $(this);
  var $item = $btn.closest('.catalog-item');
  var data = {
    'id' :  $item.attr('id'),
  };
  console.log('Товар: '+$item.find('.catalog-item-title').text()+' добавлен в корзину');
  $.post( cartAJAXUrls.add, data, function(response) {
    console.log('Товар: '+$item.find('.catalog-item-title').text()+' добавлен в корзину');
  });
});

// на странице товара
$('.block-item-form').on('click', function(e) {
  $('#formAddCart').submit();
});
// добавить товар в корзину
$('.formAddCart').on('submit', function(e) {
   $.post( cartAJAXUrls.add, $('#formAddCart').serialize(), function(response) {
    console.log(response);
  });
});

// удалить товар из корзины
$('.cart_item').on('click', '.js-cart-remove', function(e) {
  e.preventDefault();
  e.stopPropagation();

  var $btn = $(this);
  var $item = $btn.closest('.cart_item');
  var data = {
    'id' :  $item.attr('id'),
  };
  
  $.post( cartAJAXUrls.remove, data, function(response) {
    if (response) {
      $item.remove();
    }
  });
});


// var $itemCount = $('input[name=itemCount]');
// $('#countItems').on('change', saveItemCount);
// localStorage.setItem('itemCount', $('#countItems').val().replace(/[^0-9]/g, ''));






// $('.js-item-count').on('click', function(e) {
// 	var oldValue = Number(localStorage.getItem('itemCount')),
// 			newValue = 0,
// 			$this = $(this);

// 	if ($this.data('count') == 'add') {
// 		newValue = oldValue+1;
// 	} else {
// 		if (1 === oldValue) {
// 			newValue = oldValue;
// 		} else {
// 			newValue = oldValue-1;
// 		}
// 	}

// 	$itemCount.val(newValue);

// 	localStorage.setItem('itemCount', newValue);
// 	console.log('newCount - '+localStorage.getItem('itemCount'));
// });


// function saveItemCount(e) {
// 	localStorage.setItem('itemCount', $itemCount.val().replace(/[^0-9]/g, ''));
// 	e.preventDefault();
// 	console.log('Count - '+localStorage.getItem('itemCount'));
// }

