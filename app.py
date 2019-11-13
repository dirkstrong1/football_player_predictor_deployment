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

    predicted_dict = {0 : 'Strong Defensive Minded Player',
                   1 : 'Technically Gifted Finisher',
                   2 : 'All Around Playmaker',
                   3 : 'Defensive Ball Winner',
                   4 : 'Skilled Aerial Player'}

    results_html_dict = {0 : "strong_def_minded.html",
                   1 : "tech_gifted.html",
                   2 : "all_arounder.html",
                   3 : "def_ball_winner.html",
                   4 : "skilled_air.html"}



    if data and all(feature in data for feature in expected_features):
        # Convert the dict of fields into a list
        test_value = [float(data[feature]) for feature in expected_features]
        predicted_class = predict_player(test_value)
        return render_template(results_html_dict[predicted_class],
               predicted_class=predicted_dict[predicted_class])
    else:
        return abort(400)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
