# app.py

from flask import render_template
import connexion

# tells Connexion which directory to look in for its
# configuration file. In this case, same directory app.py is in
app = connexion.App(__name__, specification_dir="./")
# tell app instance to reach swagger.yml from
# the specification directory and configure system to provide
# Connexion functionality 
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)