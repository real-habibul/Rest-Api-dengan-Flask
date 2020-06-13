from flask import Flask, jsonify

class Pengguna:
    def signup(self):
        pengguna = {
            "_id": "",
            "name": "",
            "email": "",
            "password": ""
        }
        return jsonify(pengguna), 200