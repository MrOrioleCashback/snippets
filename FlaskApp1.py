from flask import Flask
app = Flask(__name__)

@app.route('/') 	#event handler
def index():		#event function
	return '<h1>Hello World</h1>'
	
@app.route('/user/<name>') #dynamic route
def user(name):
	return '<h1>Hello, {}</h1>'.format(name)

if __name__ == '__main__':	#ensures dev server is started only
	app.run(debug=True)	#when script is run directly
