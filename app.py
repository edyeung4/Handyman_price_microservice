import requests
from flask import Flask, request
app = Flask(__name__)


@app.route('/post/', methods=['POST'])
def post_something():
    """ POST request route handler makes api call to convert USD to CAD and returns 
        JSON object of item and prices"""

    # api call to http://api.currencylayer.com/live
    access_key2 = "879fc9b0c0d703f8e37941ecb126960e"
    response = requests.get(f"http://api.currencylayer.com/live?access_key={access_key2}")
    usd_cad_conv = response.json()["quotes"]["USDCAD"]

    item_dict = {
        'items' : []
    }

    # obtains JSON request body and filters for shopping results
    item_list = request.get_json()['inline_shopping_results']

    # creates JSON response object with item and price conversion
    for item in item_list:
        item_dict['items'].append({
            'item_pos' : item['position'],
            'price' : [{'USD' : item['price']}, {'CAD' : f"${float(item['extracted_price'])*usd_cad_conv:.2f}" }]
        })
    return item_dict

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to price USD-CAD converter !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
