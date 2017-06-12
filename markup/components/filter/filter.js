;

var filterAJAXUrl = 'pima';

var changePrice = $('input[name=changePrice]');
var changeSeries = $('select[name=changeSeries]');
var changeParams = $('input[name=changeParams]');

changePrice.on('change', filterAJAXRequest);
changeSeries.on('change', filterAJAXRequest);
changeParams.on('change', filterAJAXRequest);

function filterAJAXRequest() {
  $.post( filterAJAXUrl, $('#filterCategory').serialize(), function(response) {
    console.log(response);
    $('.catalog-wrapper').empty().html(response);
  });
}