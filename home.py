from flask import Flask
from flask_assistant import Assistant, tell,ask
import logging
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)

app = Flask(__name__)
assist = Assistant(app, project_id='-------your google application id-----')

@assist.action('greeting')
def greet_and_start():
    speech = "Hey! welcome how i can help you?"
    return ask(speech)

@assist.action('Demo')
def hello_world():
    speech = 'Microphone check 1, 2 what is this?'
    return tell(speech)

if __name__ == '__main__':
    app.run(debug=True,port=5001
            )
