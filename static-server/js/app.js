// read the cookie
var csrftoken=Cookies.get('csrftoken');

function csrfSafeMethod(method){
  // no csrf on the following http reqs
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*
ajaxSetup(options) sets global settings for future ajax requests.
options is a key-value pair that configure this request.
beforeSend is a function to run before the request is sent.
<Code copied from docs of django>
*/
$.ajaxSetup({
  beforeSend: function(xhr,settings){
    if(!csrfSafeMethod(settings.type) && !this.crossDomain){
      xhr.setRequestHeader("X-CSRFToken",csrftoken);
    }
  }
});

// $ is the jquery objs
$(document).ready(function(){
  console.log( "ready!" );

  myFunction();

  $('.add-to-cart').on('click',function(e){
    console.log( "ready!" );
    // e.target is a reference to the obj that dispatched the event.
    var $add_to_cart=$(e.target);

    var $product=$add_to_cart.parent().parent('.product');
    // get the product id which was passed to the template
    var product_id=$product.attr('data-product-id');

    var response=$.post('/products/add_to_cart/'+product_id+'/');
    response.then(function(response){
      if(response.success){
        $add_to_cart.hide();
        $add_to_cart.next().show();
      }
      else {
        alert('Problem while adding to cart');
      }
    })
  });


  $('.remove-from-cart').on('click', function(e) {
        var $remove_from_cart = $(e.target);
        var $product = $remove_from_cart.parent().parent('.product');
        var product_id = $product.attr('data-product-id');

        $.ajax({
            url: '/products/add_to_cart/' + product_id + '/',
            method: 'DELETE',
            success: function(response) {
                $remove_from_cart.hide();
                $remove_from_cart.prev().show();
            },
            failure: function(){
                alert('Error while removing item from cart.');
            }
        });
    });


    $('#showCart').on('click', function(e) {
          $.ajax({
              url: '/cart',
              method: 'GET',
              data: 'json',
              success: function(response){
                  var products = response.data;
                  $("#cartProducts").html('');
                  var total = 0;
                  if (products.length > 0){
                      for(var i=0; i<products.length; i++) {
                          total += parseInt(products[i].price);
                          var html = '<tr>' +
                              '<td class="product-image">' +
                                '<img style="height: 200px; width: 250px;" src=/static/images/' + products[i].image + '/>' +
                              '</td>' +
                              '<td class="product-name">' +
                                '<span>' + products[i].name + '</span>' +
                              '</td>' +
                              '<td class="product-price">' +
                                '<span>Rs.' + products[i].price + '</span>' +
                              '</td>' +
                            '</tr>';

                          $("#cartProducts").append(html);
                      }
                  }
                  else {
                      $('#cartProducts').append("<h5>No products in cart.</h5>");
                  }
                  $('#cartProductsTotal').text("Rs. " + total);
                  $('#cart').modal('show');
              }
          });
      });
});


function myFunction(){
  $.ajax({
    url:'/cart',
    method:'GET',
    data:'json',
    success:function(response){
      var products=response.data;
      if(products.length>0){
        for(var i=0;i<products.length;i++){
          var $selectedClass=$('.product[data-product-id='+products[i].id+']');
          var add=$selectedClass.find('.product-action');
           add.find('.add-to-cart').hide();
           add.find('.remove-from-cart').show();
        }
      }
    }
  });
}
