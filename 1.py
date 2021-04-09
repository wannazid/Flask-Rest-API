#install module
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
#object flask
app = Flask(__name__)
#object restful
api = Api(app)
#object cors
CORS(app)
#dictrio
indentitas = {}
#Class Resource
class ContohResource(Resource):
	#metode get dan post
	def get(self):
		#response = {"msg":"Bingung"}
		return indentitas
	def post(self):
		nama = request.form["nama"]
		umur = request.form["name"]
		identitas["nama"] = nama
		identitas["umur"] = umur
		response = {"msg":"Data Berhasil Di Simpan"}
		return response
#setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])
if __name__ == "__main__":
	app.run(debug=True, port=5005)