from flask import Flask, render_template
from flask import jsonify
Trip=[
  {
    'id':1,
    'city':'Mumbai',
    # 'image':'https://images.unsplash.com/photo-1589182337358-09c156b66eaf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',
    'country':'India',
    'currency':'Rupees',
    'language':'Hindi',
    'currency_code':'INR',
    'currency_symbol':'₹',
    'currency_decimal_digits':'2',
    'currency_thousands_separator':',',
    'currency_grouping':3,
    'time_zone':'Asia/Kolkata',
    'continent':'Asia',
    'latitude':'19.0760',
    'longitude':'72.8777',
    'flag':'https://cdn.countryflags.com/thumbs/india/flag-400.png'
  },
  {
    'id':2,
    'city':'Mumbai',
    # 'image':'https://images.unsplash.com/photo-1589182337358-09c156b66eaf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',
    'country':'USA',
    'currency':'Dollar',
    'language':'English',
    'currency_code':'INR',
    'currency_symbol':'₹',
    'currency_decimal_digits':'2',
    'currency_thousands_separator':',',
    'currency_grouping':3,
    'time_zone':'Asia/Kolkata',
    'continent':'Asia',
    'latitude':'19.0760',
    'longitude':'72.8777',
    'flag':'https://cdn.countryflags.com/thumbs/india/flag-400.png'
    
  },
  {
    'id':3,
    'city':'Mumbai',
    # 'image':'https://images.unsplash.com/photo-1589182337358-09c156b66eaf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',
    'country':'India',
    'currency':'Rupees',
    'language':'Hindi',
    'currency_code':'INR',
    'currency_symbol':'₹',
    'currency_decimal_digits':'2',
    'currency_thousands_separator':',',
    'currency_grouping':3,
    'time_zone':'Asia/Kolkata',
    'continent':'Asia',
    'latitude':'19.0760',
    'longitude':'72.8777',
    'flag':'https://cdn.countryflags.com/thumbs/india/flag-400.png'
  },
  {
    'id':4,
    'city':'Mumbai',
    # 'image':'https://images.unsplash.com/photo-1589182337358-09c156b66eaf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',
    'country':'USA',
    'currency':'Dollar',
    'language':'English',
    'currency_code':'INR',
    'currency_symbol':'₹',
    'currency_decimal_digits':'2',
    'currency_thousands_separator':',',
    'currency_grouping':3,
    'time_zone':'Asia/Kolkata',
    'continent':'Asia',
    'latitude':'19.0760',
    'longitude':'72.8777',
    'flag':'https://cdn.countryflags.com/thumbs/india/flag-400.png'
  }
  
]
# flask is module and Flask is class
app= Flask(__name__)
# we have created an object app 
@app.route("/")
# this is a decorator
def hello_world():
  return render_template ('home.html',trip=Trip,company_name='TriveTrove')
# this is a function 

@app.route("/api/trip")
def list_trip():
  return jsonify(Trip)
  
if __name__== "__main__":
  app.run(host="0.0.0.0",debug=True)
# this is a method
