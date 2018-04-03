from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """

<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-raduis: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label for="user-number">Rotate by:</label>
            <input type="text" id="user-number" name="rot" value="0" />
            <textarea name="text" rows="12" cols="80">{0}</textarea>
            <input type="submit" value="Submit Query" />
        
        </form>
    </body>
</html>
"""


@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    result = rotate_string(text, int(rot))
    return form.format(result)

@app.route("/")
def index():
    return form.format("")

app.run()