# Price microservice
Price microservice that converts item prices from USD to CAD and returns conversion in JSON format. 
Input request to microservice must be in the form of JSON request from google search api - serpapi
Example of input POST req:
```
"shopping_results":
[
{
"position":
1,
"block_position":
"right",
"title":
"Red Custom Printed Delta Apparel T-Shirts - Athletic Fit (Red - Sample)",
"price":
"$4.78",
"extracted_price":
4.78,
"link":
"https://www.google.com/aclk?sa=l&ai=DChcSEwiLsa_dycT0AhVYFdQBHQrpCdMYABAIGgJvYQ&ae=2&sig=AOD64_0g0PgSdrM40TlArTAwGYpU45WDIQ&ctype=5&q=&ved=2ahUKEwjdoqPdycT0AhX8l2oFHfkIC8YQ5bgDegQIAhBW&adurl=",
"source":
"DiscountMugs.c...",
"thumbnail":
"https://serpapi.com/searches/61a87373cca014d3ce581826/images/106094d9e87e0d84957861c2613c9bd1ecaeba93732e225ee9ec6d82c61ae597.png",
"extensions":
[
"$75 off $500+"
]
},
{
"position":
2,
"block_position":
"right",
"title":
"Women's Short Sleeve T-Shirt - A New Day Red L",
"price":
"$5.00",
"extracted_price":
5,
"link":
"https://www.google.com/aclk?sa=l&ai=DChcSEwiLsa_dycT0AhVYFdQBHQrpCdMYABAJGgJvYQ&sig=AOD64_3tPS6wVxxJz_aCxctecfRNsRdDYQ&ctype=46&q=&ved=2ahUKEwjdoqPdycT0AhX8l2oFHfkIC8YQ5bgDegQIAhBv&adurl=",
"source":
"Target",
"thumbnail":
"https://serpapi.com/searches/61a87373cca014d3ce581826/images/106094d9e87e0d84957861c2613c9bd196f7afbccbeae9c4ff0f9d70bd68a80f.png"
},
```
USD - CAD Converter can be tesed at https://price-conv-service.herokuapp.com/ using any api testing tool.

Example JSON return
```
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
```
