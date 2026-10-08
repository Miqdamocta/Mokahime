from flask import Flask, request, render_template_string, redirect
import os

app = Flask(__name__)

# --- CONFIGURATION ---
# You will get these from the Discord Developer Portal
CLIENT_ID = os.environ.get('CLIENT_ID', 'YOUR_CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET', 'YOUR_CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI', 'https://your-app.onrender.com/callback')

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Mokahime Verification</title>
    <style>
        body { font-family: 'Comic Sans MS', cursive, sans-serif; background-color: #ffe4e1; text-align: center; color: #ff69b4; padding: 50px; }
        .container { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); display: inline-block; border: 5px solid #ffb6c1; }
        h1 { font-size: 30px; }
        .btn { background-color: #ff69b4; color: white; border: none; padding: 15px 30px; font-size: 20px; border-radius: 50px; cursor: pointer; text-decoration: none; display: inline-block; transition: 0.3s; }
        .btn:hover { background-color: #ff1493; transform: scale(1.1); }
        .cat { font-size: 50px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="cat">ฅ(=^･ω･^=)ฅ</div>
        <h1>Welcome to Mokahime Verification!</h1>
        <p>Click the button below to verify your identity and get your role, nyaaa~!</p>
        <a href="/verify" class="btn">Verify Me! ✨</a>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/verify')
def verify():
    # In a real Linked Role, you would exchange the code for a token here
    # and then call the Discord API to update the user's role status.
    return "<h1>Success! 🐾</h1><p>You have been verified by Mokahime! You can now go back to Discord, nyaaa~!</p>"

@app.route('/callback')
def callback():
    # This is where Discord sends the user back
    return redirect('/')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
