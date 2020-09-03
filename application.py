from flask import Flask,render_template,url_for,request
import re
from textblob import TextBlob as tb


email_regex = re.compile(r"[\w\.-]+@[\w\.-]+")
# phone_num = re.compile(r"^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$")
# phone_num = re.compile(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")
# phone_num = re.compile(r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$")
phone_num = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d|\d\d\d-\d\d\d-\d\d\d\d')
url_https_regex = re.compile(r'https?://\S+')
url_regex = re.compile(r'http?://\S+')

application = Flask(__name__)

@application.route('/')
def index():
	return render_template("index2.html")

@application.route('/about')
def about():
	return render_template('about.html')
	
@application.route('/process',methods=["POST"])
def process():
	if request.method == 'POST':
		choice = request.form['taskoption']
		if choice == 'email':
			rawtext = request.form['rawtext']
			results = email_regex.findall(rawtext)
			num_of_results = len(results)
		elif choice == 'phone':
			rawtext = request.form['rawtext']
			results = phone_num.findall(rawtext)
			num_of_results = len(results)
		elif choice == 'url_https':
			rawtext = request.form['rawtext']
			results = url_https_regex.findall(rawtext)
			num_of_results = len(results)
		elif choice == 'url':
			rawtext = request.form['rawtext']
			print(rawtext)
			results = url_regex.findall(rawtext)
			print(results)
			num_of_results = len(results)
		elif choice =='selected':
			results=[ 'Please Select any Option To Continue']
			return render_template("index2.html",results=results)
		elif choice=='translate':
			rawtext = request.form['rawtext']
			w=tb(rawtext)
			ans=w.translate(to='pa')
			results=['<---Conversion To Punjabi--->\n','The detected language Code ---> '+str(w.detect_language()),'The Original Text You entered --> '+str(rawtext),'The Punjabi Translation  --> '+ans.string]
			#num_of_results='Conversion To Punjabi '
			return render_template("index2.html",results=results)


	return render_template("index2.html",results=results,num_of_results = num_of_results)


if __name__ == '__main__':
	application.run(debug=True)
