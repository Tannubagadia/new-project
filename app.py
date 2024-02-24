from flask import Flask, render_template

# flask is module and Flask is class
app= Flask(__name__)
# we have created an object app 
@app.route("/")
# this is a decorator
def hello_world():
  return render_template ('home.html')
# this is a function 
if __name__== "__main__":
  app.run(host="0.0.0.0",debug=True)
# this is a method
