from flask import Flask
from flask import request 
from flask import url_for
from flask import redirect
import stripe

app = Flask(__name__)
@app.route("/")
def index():
  url_for('static', filename='index.html')
  return redirect('/static/index.html')

@app.route('/stripe_charge', methods=['POST'])
def stripe_charge():

  # Set your secret key: remember to change this to your live secret key in
  # production
  # See your keys here https://manage.stripe.com/account
  stripe.api_key = ''

  # Get the credit card details submitted by the form
  token = request.form['stripeToken']

  # Create the charge on Stripe's servers - this will charge the user's card
  try:
    charge = stripe.Charge.create(
        amount=1000, # amount in cents, again
        currency="usd",
        card=token,
        description="payinguser@example.com")
    return 'payment received'
  except Exception,e:
    print str(e)
    return 'payment failed'

if __name__ == "__main__":
  app.run()
