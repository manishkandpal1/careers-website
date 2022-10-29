from flask import Flask
# created a flask application
app=Flask(__name__)
# route
@app.route("/")
def helloworld():
  return "hello world"

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
 # print("I'm inisde the if now")