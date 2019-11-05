from flask import Flask, send_from_directory, render_template, request, abort
from waitress import serve
from models.player_predictor import predict_player

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""
    return send_from_directory("static", "index.html")

@app.route("/get_results", methods=["POST"])
def get_results():
    """ Predict the player class based on the inputs. """
    data = request.form
    print(data)

    expected_features = ('acceleration', 'sprint_speed', 'agility', 'balance',
        'reactions', 'ball_control', 'composure', 'positioning',
        'finishing','shot_power', 'long_shots', 'volleys', 'penalties',
        'vision', 'crossing', 'free_kick', 'short_pass', 'long_pass',
        'pass_curve', 'interceptions', 'heading', 'marking', 
        'standing_tackle', 'sliding_tackle',
        'jumping', 'stamina', 'strength', 'aggression')

    for feature in expected_features:
        print(data[feature])

    if data and all(feature in data for feature in expected_features):
        # Convert the dict of fields into a list
        test_value = [float(data[feature]) for feature in expected_features]
        predicted_class = predict_player(test_value)
        return render_template("results.html", predicted_class=predicted_class)
    else:
        return abort(400)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
