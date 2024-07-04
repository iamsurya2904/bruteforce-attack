app.py # type: ignore

from flask import Flask, request, jsonify
from bruteforcecaeser import brute_force

app = Flask(__name__)

@app.route('/bruteforce', methods=['POST'])
def bruteforce():
    data = request.get_json()
    password = data['password']
    found_password = brute_force(password)
    if found_password:
        return jsonify(message=f"Success: The password is {found_password}")
    else:
        return jsonify(message="Failed: Password not found")

if __name__ == "__main__":
    app.run(debug=True)
