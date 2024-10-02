from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def subtract_large_numbers(num1: str, num2: str) -> str:
    """
    Функция для посимвольного вычитания одного длинного числа из другого.
    """
    negative = False
    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        num1, num2 = num2, num1
        negative = True

    num1 = list(num1)
    num2 = list(num2.zfill(len(num1)))

    result = []
    borrow = 0

    for i in range(len(num1) - 1, -1, -1):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) + borrow

        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0

        result.append(str(digit1 - digit2))

    while result and result[-1] == '0':
        result.pop()

    if not result:
        return '0'

    result = ''.join(reversed(result))

    if negative:
        result = '-' + result

    return result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = subtract_large_numbers(num1, num2)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
