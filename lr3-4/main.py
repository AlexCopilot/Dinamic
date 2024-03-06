from flask import Flask, render_template, request

app = Flask(__name__)

# monthly_rate - Ежемесячная ставка
# credit_amount - Сумма кредита
# interest_rate - Процентная ставка
# imortgage_term - Срок ипотеки месяцев
# total_rate - Общая ставка
# monthly_payment - Ежемесячный платеж
# total_loan - Общая плата по кредиту
# overpayment - Переплата

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def return_to_index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def form():
    if request.method == 'POST':
        credit_amount = int(request.form.get('price'))
        initial_fee = int(request.form.get('initial_fee'))
        imortgage_term = int(request.form.get('term'))
        interest_rate = int(request.form.get('rate'))

        imortgage_term *= 12
        credit_amount -= initial_fee
        monthly_rate = interest_rate / 12 / 100
        total_rate = (1 + monthly_rate) ** imortgage_term
        monthly_payment = int(credit_amount * monthly_rate * total_rate / (total_rate - 1))
        total_loan = int(monthly_payment * imortgage_term)
        overpayment = int(total_loan - credit_amount)
        results = [credit_amount+initial_fee, initial_fee, imortgage_term/12, interest_rate, monthly_payment, total_loan, overpayment]
        return render_template('result.html', results = results)


if __name__ == '__main__':
    app.run(debug=True)



