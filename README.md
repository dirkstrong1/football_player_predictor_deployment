# Football Player Predictor

This project fully deploys a web application using a machine learning algorithm to
predict a football player class. The landing pages then provide further information on the
players and insights into play styles.

* Python (3.7.4)

### System

This project was created on a Macbook Pro running MacOS Mojave.

#### Python

This project used Python 3.7.4 and Anaconda 4.7.12. All Python packages can be found in the [`environment.yml`] file.


## Acknowledgements

### Data

Thank you to [Aishwarya Sharma](https://www.kaggle.com/aishwarya1992) for publishing his [FIFA 19 Player Database on Kaggle](https://www.kaggle.com/aishwarya1992/fifa-19-player-database/):

> [This] Data set consists of all the player data from EA Sports FIFA 19. It contains all the attributes and ratings for all players in the data set.

## Requirements

This repo uses Python 3.6.0. All python packages can be found in the `requirements.txt` file.  The requirements are in `pip` style, because this is supported by Heroku.

To create a new `conda` environment to use this repo, run:
```bash
conda create --name flask-env
conda activate flask-env
pip install -r requirements.txt
```

You will likely need to install additional packages to support your deployment.  With the `flask-env` activated, you can run `conda install <package-name>`.  Once you are ready to deploy, you can generate your own `requirements.txt` for reproducibility purposes with:
```bash
pip freeze > requirements.txt
```
## Running the Flask Application

To run in a development environment (on your local computer)
```bash
export FLASK_ENV=development
env FLASK_APP=app.py flask run
```

To run in a production environment (used for deployment, but test it out locally first):
```bash
export FLASK_ENV=production
python app.py
```
