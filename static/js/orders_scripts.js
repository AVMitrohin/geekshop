window.onload = function () {
    var _quantity, _price, orderitemNum, deltaQuantity, orderitemQuantity, deltaCost;
    quantity_arr = [];
    price_arr = [];

    var totalForms = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());
    var orderTotalQuantity = parseInt($('.order_total_quantity').text()) || 0;
    var orderTotalCost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;
    var $orderForm = $('.order_form');


    for (i = 0; i < totalForms; i++) {
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
        quantity_arr[i] = _quantity;
        price_arr[i] = (_price) ? _price : 0;
    }

    function orderSummaryUpdate(orderitemPrice, deltaQuantity) {
        deltaCost = orderitemPrice * deltaQuantity;
        orderTotalCost = Number((orderTotalCost + deltaCost).toFixed(2));
        orderTotalQuantity = orderTotalQuantity + deltaQuantity;

        $('.order_total_cost').html(orderTotalCost.toString());
        $('.order_total_quantity').html(orderTotalQuantity.toString());
    }

    function deleteOrderItem(row) {
        var targetName = row[0].querySelector('input[type="number"]').name;
        orderitemNum = parseInt(targetName.replace('orderitems-', '').replace('-quantity', ''));
        deltaQuantity = -quantity_arr[orderitemNum];
        orderSummaryUpdate(price_arr[orderitemNum], deltaQuantity);
    }
    if (!orderTotalQuantity) {
        for (i = 0; i < totalForms; i++) {
            orderTotalQuantity += quantity_arr[i];
            orderTotalCost += quantity_arr[i] * price_arr[i];
        }
        $('.order_total_quantity').html(orderTotalQuantity.toString());
        $('.order_total_cost').html(Number(orderTotalCost.toFixed(2)).toString());
    }

    $orderForm.on('change', 'input[type="number"]', function (event) {
        orderitemNum = parseInt(event.target.name.replace('orderitems-', '').replace('-quantity', ''));
        if (price_arr[orderitemNum]) {
            orderitemQuantity = parseInt(event.target.value);
            deltaQuantity = orderitemQuantity - quantity_arr[orderitemNum];
            quantity_arr[orderitemNum] = orderitemQuantity;
            orderSummaryUpdate(price_arr[orderitemNum], deltaQuantity);
        }
    });

    $orderForm.on('change', 'input[type="checkbox"]', function (event) {
        orderitemNum = parseInt(event.target.name.replace('orderitems-', '').replace('-DELETE', ''));
        if (event.target.checked) {
            deltaQuantity = -quantity_arr[orderitemNum];
        } else {
            deltaQuantity = quantity_arr[orderitemNum];
        }
        orderSummaryUpdate(price_arr[orderitemNum], deltaQuantity);
    });
};