# Price microservice
Price microservice that converts item prices from USD to CAD and returns conversion in JSON format

USD - CAD Converter can be tesed at https://price-conv-service.herokuapp.com/ using any api testing tool.

Example JSON return
{
"items": [{
        "item_pos": 1,
        "price": [{
            "USD": "$149.00"
        }, {
            "CAD": "$186.29"
        }]
    }, {
        "item_pos": 2,
        "price": [{
            "USD": "$41.99"
        }, {
            "CAD": "$52.50"
        }]
    }, {
        "item_pos": 3,
        "price": [{
            "USD": "$19.20"
        }, {
            "CAD": "$24.01"
        }]
    }
}
