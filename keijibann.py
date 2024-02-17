from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.debug = True  # デバッグモードを有効にする

# ユーザー名
username = None
# メッセージのリスト
messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global username
    if request.method == 'POST':
        new_username = request.form['username']
        if new_username != username:
            username = new_username
            return redirect('/board')
        else:
            return render_template('confirm.html')
    return render_template('index.html')

@app.route('/board', methods=['GET', 'POST'])
def board():
    global username, messages
    if request.method == 'POST':
        if 'delete' in request.form:
            delete_index = int(request.form['delete'])
            if 0 <= delete_index < len(messages) and messages[delete_index]['username'] == username:
                del messages[delete_index]
        else:
            message = request.form.get('message')
            if message:
                messages.append({'username': username, 'message': message})
        return redirect('/board')
    return render_template('board.html', username=username, messages=messages)

if __name__ == '__main__':
    app.run(use_reloader=True)
