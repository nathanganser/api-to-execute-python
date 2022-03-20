from flask import Flask, request, jsonify, render_template

application = Flask(__name__)

secret = "OK"  # can you access this data


@application.route('/', methods=['GET', 'POST'])
def tryme():
    if request.method == 'GET':
        return render_template('try.html')

@application.route("/execute", methods= ['GET', 'POST'])
def execute():
    print(request.json)
    code = request.json.get('code')

    response = {}
    try:
        exec(code, {"__builtins__": None}, response)
    except Exception as e:
        print(e)
        return jsonify("Error: " + str(e))
    print("done")
    return jsonify(response)

if __name__ == '__main__':

    application.run()
