from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()
    query = request.args.get('query')
    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {

        "q": query,

        "apikey": "8LOGBZT09G1P",

        "limit": 9,
    }

    # TODO: Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    r = requests.get("https://api.tenor.com/v1/search" , params = params)


    # TODO: Use the '.json()' function to get the JSON of the returned response
    if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
        top_9gifs = json.loads(r.content)
    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
        top_9gifs = top_9gifs["results"]
    else:
        top_9gifs = None



    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html", gifs = top_9gifs)

if __name__ == '__main__':
    app.run(debug = True)
