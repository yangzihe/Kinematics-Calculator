from flask import Flask, render_template, request, jsonify
import kinematics_calc as kCalc


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
if __name__ == "__main__":
    app.run()
