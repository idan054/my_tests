from flask import Flask, render_template, request
import stream_chat
from datetime import datetime

# current date and time
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

app = Flask(__name__)
@app.route('/firebase', methods=["GET", "POST"])
def home():
    # POST is not in use.
    if request.method == "POST":
        name = request.form["first name"]

        # resp = push(file_path, f"Latest update on {now} (by .py)", name, "main")
        # return render_template("resp.html", name=name, resp=resp) # age.html

    # example: http://127.0.0.1:5000/firebase?uid=325245&name=idan
    print('Start:')
    args = request.args
    uid = args.get('uid')
    name = args.get('name')
    print(f'{uid} - {name}')

    server_client = stream_chat\
        .StreamChat(api_key="ah48ckptkjvm",
                    api_secret="gfcfa94ghkctn3du36s2d4nmqg9q24wtxhr56qd84pj7dum94ahhtedccj8q7wk4")

    token = server_client.create_token(f'{uid}')
    print(f'token {token}')

    # return render_template("base.html")
    return {
        'get_api_call_at' : f'{now}',
        'firebase_uid' : f'{uid}',
        'firebase_name' : f'{name}',
        'getStream_token' : f'{token}'
    }


if __name__ == '__main__':
    app.run(debug=True)
