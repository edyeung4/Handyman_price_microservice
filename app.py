import requests
from flask import Flask, request, jsonify
from datetime import date
app = Flask(__name__)

# @app.route('/getmsg/', methods=['GET'])
# def respond():
#     # Retrieve the name from url parameter
#     name = request.args.get("name", None)

#     # For debugging
#     print(f"got name {name}")

#     response = {}

#     # Check if user sent a name at all
#     if not name:
#         response["ERROR"] = "no name found, please send a name."
#     # Check if the user entered a number not a name
#     elif str(name).isdigit():
#         response["ERROR"] = "name can't be numeric."
#     # Now the user entered a valid name
#     else:
#         response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

#     # Return the response in json format
#     return jsonify(response)
# global curr_json = None

global api_call_date
global curr_store
api_call_date = date.today()
curr_store = None

def curr_conv():
    global curr_store, api_call_date
    """ Currency converter api converts USD to CAD and Eur 
        https://free.currencyconverterapi.com/ """

    access_key = 'd7853e4ed0d5d37e8676'

    # response = requests.get(f"https://free.currconv.com/api/v7/convert?q=USD_CAD&compact=ultra&apiKey={access_key}")

    if date.today() == api_call_date and curr_store is not None:
        return curr_store.json()['USD_CAD']
    else:
        curr_store = requests.get(f"https://free.currconv.com/api/v7/convert?q=USD_CAD&compact=ultra&apiKey={access_key}")

        return curr_store.json()['USD_CAD']

@app.route('/post/', methods=['POST'])
def post_something():
    api_call_date = date.today()

    item_dict = {
        'items' : [None]
    }

    item_list = request.get_json()['inline_shopping_results']
    for item in item_list:

        # replaces first item value in dict which was intialized to None
        if item_dict['items'][0] == None:
            item_dict['items'][0] = {
                'item_pos' : item['position'],
                'price' : [{'USD' : item['price']}, {'CAD' : item['extracted_price']*curr_conv()}]
            }
        else:
            item_dict['items'].append({
                'item_pos' : item['position'],
                'price' : [{'USD' : item['price']}, {'CAD' : f"${item['extracted_price'] *curr_conv():.2f}" }]
            })
    return item_dict


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Cant see gay nibbas like anjan !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
