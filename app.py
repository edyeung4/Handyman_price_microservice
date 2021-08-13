import requests
from flask import Flask, request
app = Flask(__name__)


@app.route('/post/', methods=['POST'])
def post_something():
    """ POST request route handler makes api call to convert USD to CAD and returns 
        JSON object of item and prices"""

    # api call to https://free.currencyconverterapi.com/
    access_key = 'd7853e4ed0d5d37e8676'
    # response = requests.get(f"https://free.currconv.com/api/v7/convert?q=USD_CAD&compact=ultra&apiKey={access_key}")
    response = requests.get('https://free.currconv.com/api/v7/convert?q=USD_CAD&compact=ultra&apiKey=d7853e4ed0d5d37e8676')    
    print(response.json())
    for i in response.json():
        print(i)
        key_api_store = i
    print(type(key_api_store))
    # print(type(response.json()[key_api_store]))
    usd_cad_conv = response.json()[key_api_store]

    item_dict = {
        'items' : []
    }

    # obtains JSON request body and filters for shopping results
    item_list = request.get_json()['inline_shopping_results']

    # creates JSON response object with item and price conversion
    for item in item_list:
        item_dict['items'].append({
            'item_pos' : item['position'],
            'price' : [{'USD' : item['price']}, {'CAD' : f"${item['extracted_price']*usd_cad_conv:.2f}" }]
        })
    return item_dict

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to price USD-CAD converter !!</h1>"


# if __name__ == '__main__':
#     # Threaded option to enable multiple instances for multiple user access support
#     app.run(threaded=True, port=5000)
