from app import aplikasi
from user.models import Pengguna

@aplikasi.route("/user/signup", methods=['GET'])
def signup():
    return Pengguna().signup()

@aplikasi.route("/daftar/")
def daftar():
    return "Daftar baru"
