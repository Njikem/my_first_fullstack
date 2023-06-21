from flask import Flask, request, make_response, jsonify
import dbhelpers, apihelpers, dbcreds

app = Flask(__name__)


@app.get("/api/candy")
def get_all_candy():
    results = dbhelpers.run_procedure("call get_candy()", [])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"), 500)
    

@app.post("/api/candy")
def post_candy():
    error =apihelpers.check_endpoint_info(request.json, ["name", "image_url", "description"])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = dbhelpers.run_procedure("call insert_three_candy(?,?,?)", [request.json.get("name"),request.json.get("image_url"),request.json.get("description")])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"), 500)
    
@app.delete("api/candy")
def delete_candy():
    error =apihelpers.check_endpoint_info(request.json, ["id"])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = dbhelpers.run_procedure("call delete _candy(?)", ["id"])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"), 500)
    

app.run(debug=True)
    

    