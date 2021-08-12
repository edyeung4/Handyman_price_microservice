import requests
from flask import Flask, request, jsonify
from datetime import date
app = Flask(__name__)

global api_call_date
global curr_store
api_call_date = date.today()
curr_store = None

def curr_conv():
    """ Currency converter api converts USD to CAD and Eur 
        https://free.currencyconverterapi.com/ """
    global curr_store, api_call_date
    access_key = 'd7853e4ed0d5d37e8676'

    if date.today() == api_call_date and curr_store is not None:
        return curr_store.json()['USD_CAD']
    else:
        curr_store = requests.get(f"https://free.currconv.com/api/v7/convert?q=USD_CAD&compact=ultra&apiKey={access_key}")
        return curr_store.json()['USD_CAD']

@app.route('/post/', methods=['POST'])
def post_something():
    usd_cad_conv = curr_conv()
    item_dict = {
        'items' : []
    }

    item_list = request.get_json()['inline_shopping_results']

    for item in item_list:
        item_dict['items'].append({
            'item_pos' : item['position'],
            'price' : [{'USD' : item['price']}, {'CAD' : f"${item['extracted_price']:.2f}" }]
        })
    return item_dict


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to price USD-CAD converter !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
