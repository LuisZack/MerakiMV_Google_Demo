import MerakiMV
from flask import Flask
from flask_assistant import Assistant, tell
from flask_cors import CORS

app = Flask(__name__)
app.config['ASSIST_ACTIONS_ON_GOOGLE'] = True
app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']
cors = CORS(app)
assist = Assistant(app, route='/google')

@app.route("/", methods=['GET'])
def main():
	testCad1, testUSRL = MerakiMV.mainReturn()
	return ("Eureka-->{}{}".format(testCad1,testUSRL))

@assist.action('bcic-meraki')
def google_bcic_meraki():
	cad,url = MerakiMV.mainReturn()
	return tell("I see " + cad[:415]).card(
		text="See...",
		title="Image:",
		img_url=url
	)

if __name__ == '__main__':
	app.run(threaded=True, port=5000)
