from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def convert_temperature(celsius=0.0):
    fahrenheit = convert_celsius_to_fahrenheit(float(celsius))
    return f"{celsius}°C is {fahrenheit}°F"


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
