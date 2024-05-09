from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', resultado='')

@app.route('/verificar', methods=['POST'])
def verificar():
    fatorial = int(request.form["fatorial"])
    fato = 2
    fatorando = 0
    fatorial_ = fatorial
    while fatorial_ != fato:
        if fatorial == -1:
            break
        fatorando = fato * fatorial
        fatorial = fatorando
        fato = fato + 1

    return render_template('index.html', resultado=f'O resultado é {fatorando}')

if __name__ == '__main__':
    app.run(debug=True)