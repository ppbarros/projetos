from flask import Flask, request, render_template
from bd_simulado import *

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def validar_login():
    if request.method == 'POST':
        user = request.form.get('nuser')
        password = request.form.get('npass')

        if validar(user, password):
            return render_template('entra.html', projetos=get_projetos(user))
        else:
            return render_template('index.html', erro='Usuário ou Senha Incorretos')
    else:
        return render_template('index.html', erro='Método errado! Use POST.')

@app.route('/projetos/<projeto>')
def detalhe_projeto(projeto):
    return render_template('detalhe.html', projeto=projeto, atividades=get_atividades(projeto))

@app.route('/atividade/<atividade>')
def detalhar(atividade):
    return render_template('atividade.html', atividade=atividade, detalhe=get_detalhe(atividade))



if __name__ == '__main__':
    app.run(debug=True)