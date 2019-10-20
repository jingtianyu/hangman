#import re

#line = "Arizona 479, 501, 870. Carlifornia 209, 213, 650"

#m = re.findall("\d",line,re.IGNORECASE)
#
#print(m)

#import re

#line = "The ghost that says boo huants the loo."

#m = re.findall(".oo",line)

#print(m)


from flask import Flask
app = Flask("_name_")

@app.route('/')
def index():
    return "Hello World!"

app.run(port=8000)

