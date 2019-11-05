import joblib

def predict_player(test_value):
    loaded_model = load_model()
    predictions = loaded_model.predict([test_value])
    if len(predictions > 0):
        return predictions[0]
    else:
        return -1

def load_model():
    """ Load the model from the .joblib file """
    model_file = open("models/football_model.joblib", "rb")
    loaded_model = joblib.load(model_file)
    model_file.close()
    return loaded_model