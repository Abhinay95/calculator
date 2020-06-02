from flask import Flask, render_template, request, jsonify

main=Flask(__name__)

@main.route('/', methods = ['GET'])
def home_page():
    return render_template('index.html')

@main.route('/math', methods = ['POST'])
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if (operation == 'add'):
            r = num1 + num2
            result = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'The difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'division'):
            r = num1 / num2
            result = 'The quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html', result=result)


@main.route('/via_postman', methods = ['POST'])
def math_operation_via_postman():
    if(request.method == 'POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r = num1+num2
            result = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if(operation=='subtract'):
            r = num1-num2
            result = 'The difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if(operation=='multiply'):
            r = num1*num2
            result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if(operation=='division'):
            r = num1/num2
            result = 'The quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' +str(r)
        return jsonify(result)


if __name__=='__main__':
    main.run(debug=True)
