from flask import Flask, request, jsonify

application = Flask(__name__)

secret = "OK"  # can you access this data


@application.route("/execute", methods= ['GET', 'POST'])
def execute():
    code = request.json.get('code')

    response = {}
    try:
        exec(code, {"__builtins__": None}, response)
    except Exception as e:
        print(e)
        return jsonify("Error: " + str(e))
    print("done")
    return jsonify(response)


application.run()
