import os 
from flask import Flask, render_template, request #request acessar dados do formulário

# Caminhos absolutos
base_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(base_dir, '../Front-End')

app = Flask(__name__, 
                    template_folder='../Front-End',
                    static_folder='../Front-End',
                    static_host='') # instancia da aplicação

@app.route('/')
def home():
    return render_template('index.html') # renderizar arquivo principal da pagina
@app.route('/calcular_area_trapezio', methods=['POST']) # aceita apenas requisições POST(envio de formulário) 
def calcular_area_trapezio():
    try:
        base_maior_trapezio = float(request.form['base_maior_trapezio']) # acessa os dados do formulário HTML
        base_menor_trapezio = float(request.form['base_menor_trapezio'])
        altura_trapezio = float(request.form['altura_trapezio'])
        area_trapezio = (base_maior_trapezio + base_menor_trapezio) * altura_trapezio / 2 # calcular a area com os valores do fórmulario
        return render_template('index.html', # retornar os valores para o html
                            resultado_trapezio=area_trapezio,
                            base_maior_trapezio=base_maior_trapezio,
                            base_menor_trapezio=base_menor_trapezio,
                            altura_trapezio=altura_trapezio) 
    except ValueError:
        return render_template('index.html',
                               error_message="Por favor, insira apenas números válidos")
@app.route('/somar', methods=['POST'])
def somar():
    try:
        somar_a = float(request.form['somar_a'])
        somar_b = float(request.form['somar_b'])
        resultado_soma = somar_a + somar_b
        return render_template('index.html',
                            resultado_soma=resultado_soma,
                            somar_a=somar_a,
                            somar_b=somar_b) 
    except ValueError:
        return render_template('index.html',
                               error_message="Por favor, insira apenas números válidos")
@app.route('/subtracao', methods=['POST'])
def subtracao():
    try:
        subtracao_a = float(request.form['subtracao_a'])
        subtracao_b = float(request.form['subtracao_b'])
        resultado_subtracao = subtracao_a - subtracao_b
        return render_template('index.html',
                            resultado_subtracao=resultado_subtracao,
                            subtracao_a=subtracao_a,
                            subtracao_b=subtracao_b) 
    except ValueError:
        return render_template('index.html',
                               error_message="Por favor, insira apenas números válidos ")
if __name__ == '__main__': # Garante que o servidor só rode quando o script é executado
    app.run(debug=True)