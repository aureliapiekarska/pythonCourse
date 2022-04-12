from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
    return render_template("bmi_calc.html",
	                        bmi=bmi)

def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)

def additional_info():
    if request.method == 'POST' and 'age' in request.form:
        age = float(request.form.get('age'))
        return print(age)

if __name__ == '__main__':
    app.run()