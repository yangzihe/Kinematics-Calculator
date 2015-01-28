from flask import Flask, render_template, request, jsonify
import kinematics_calc as kCalc
import os


# Create flask application
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        a = request.form.get('a')
        x = request.form.get('x')
        v0 = request.form.get('v0')
        v = request.form.get('v')
        t = request.form.get('t')
        ans = kCalc.findSol(a, x, v0, v, t)
        return ans
    return render_template('index.html')


# Start flask loop
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
