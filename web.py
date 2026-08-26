from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "I REALLY LOVE YOU WHY DONT YOU UNDERTSTAND MAN IM FEELING SAD ."
if __name__=="__main__":
    app.run(debug=True)
    