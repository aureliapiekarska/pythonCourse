from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    bmi_value = ''
    cpm = ''
    cpm_value = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        age = float(request.form.get('age'))
        pal = float(request.form.get('pal'))
        bmi = calc_bmi(weight, height)
        bmi_value = get_bmi_value(weight, height)
        cpm = calc_calo(weight, height, age, pal)
        cpm_value = get_cpm(cpm)
    return render_template("bmi_calc.html", bmi=bmi, bmi_value=bmi_value, cpm=cpm, cpm_value=cpm_value)



def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)


def get_state(bmi):
    if bmi < 18:
        return "Underweight"
    elif bmi < 25:
        return "Standard, you are in shape"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def get_cpm(cpm):
    if cpm <= 1200:
        return '1200'
    elif 1200 < cpm <= 1400:
        return '1400'
    elif 1400 < cpm <= 1600:
        return '1600'
    elif 1600 < cpm <= 1800:
        return '1800'
    else:
        return 'You need special diet'



def calc_calo(weight, height, age, pal):
    cpm = float(655 + (9.6 * weight) + (1.8 * height - (4.7 * age) * float(pal)))
    return cpm


def get_bmi_value(weight, height):
    bmi_result = calc_bmi(weight, height)
    bmi_status = get_state(bmi_result)
    return bmi_status


def additional_info():
    if request.method == 'POST' and 'age' in request.form:
        age = float(request.form.get('age'))
        return age


def choose_pal():
    if request.method == 'POST' and 'pal' in request.form:
        pal = int(request.form.get('pal'))
        return pal




if __name__ == '__main__':
    app.run()