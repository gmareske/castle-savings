# Save It!
Hack UIowa project - a chatbot for slaying personal savings goals. Winner, Best Fintech/Insuretech Hack.

### US savings rate in decline
According to FRED data, personal savings as percent of DPI (that is, how much people save as a percentage of their after-tax income) was 3.5% in July 2017.
The average savings rate over the past 58 years is 8.3% of DPI, over the last 10 years we saved an average of 5.5%. Today's low savings rate, especially given our relative economic strength, is a cause for concern.
Conventional wisdom, [such as this article from TIAA](https://www.tiaa.org/public/offer/insights/starting-out/how-much-of-my-income-should-i-save-every-month), suggests 20% as a responsible personal savings rate.

### Save It! "Nudges" towards saving more
> “A nudge, as we will use the term, is any aspect of the choice architecture that alters people’s behavior in a predictable way without forbidding any options or significantly changing their economic incentives.”

― Richard H. Thaler, Nudge: Improving Decisions About Health, Wealth, and Happiness

Through both a website and convenient text messaging interface, Save It! makes it easy to set and track savings goals until you have enough socked away to buy anything.

### The Website
The website is hosted on GitHub pages, so you cannot actually interact with the chatbot. View the design [here](GRIFFIN)

### Installing
Setting this up is appropriately convoluted. Here's the step-by-step to how we started building this:

Requirements:
* Python 3 or higher
* Pip
* A Twilio account with a phone number set up (we had a free trial)
* Some way of exposing the server to the internet (we used ```[ngrok](https://ngrok.com)```)
* Virtualenv (recommended)

Install required libraries:

```bash
pip install flask twilio textblob word2number
```

Install text corpora data for nltk/textblob:

```bash
python -m textblob download_corpora
```

Clone the repository:

```bash
git clone https://github.com/gmareske/saveit.github
cd saveit
```

Start up ngrok:

```bash
ngrok http 5000
```
5000 is the default port for Flask apps and we have not changed that.

Ngrok will, in the terminal window, give you a url under the Forwarding section (ex: ```http://********.ngrok.io/```).
Write this down, it will be useful for setting up the Twilio text messaging.

Run the server:
```bash
python main.py
```

Lastly, change the phone number setting in your Twilio account so that when a message comes in, there's a webhook for the ngrok url (obtained above). 
See [this blog post by Twilio](https://www.twilio.com/blog/2016/09/how-to-receive-and-respond-to-a-text-message-with-python-flask-and-twilio.html) for more details.

This should put you all ready to go. Connect to ```localhost:5000``` in a web browser or send a text to the Twilio phone number.

### Images
