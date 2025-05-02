from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def bounce():
    # Ambil URL target dari parameter query 'target'
    target = request.args.get('target')
    if not target:
        return 'Missing target parameter', 400

    # Redirect ke target yang diberikan
    return redirect(target, code=302)

@app.route('/test')
def test():
    return 'Redirector is running!', 200

if __name__ == '__main__':
    # Jalankan app Flask pada host 0.0.0.0 (akses dari luar) di port 80 (untuk Azure App Service)
    app.run(host='0.0.0.0', port=8000)
