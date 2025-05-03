from flask import Flask  
 
app = Flask(__name__) 
 
@app.route('/') 
def home(): 
    return "Hello from Azure Flask App!"  
 
if __name__== '_main_': 
    app.run(debug=True)
