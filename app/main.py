from flask import Flask,Response,request

app=Flask(__name__)


@app.route("/test")
def test():
    print(request.args)
    return {"message":"works"} 

if __name__ == "__main__":
    app.run(debug=True)