from flask import Flask, render_template, request #request acessar dados do formulário

app = Flask(__name__) # instancia da aplicação

@app.route('/')
def home():
    return render_template('index.html') # renderizar arquivo principal da pagina

@app.route('/calcular', methods=['POST'])
def calcula():
    base_maior = float(request.form['base_maior'])
    base_menor = float(request.form['base_menor'])
    altura = float(request.form['altura'])

    area = (base_maior + base_menor) * altura / 2 

    return render_template('index.html',
                           resultado=area,
                           base_maior=base_maior,
                           base_menor=base_menor,
                           altura=altura) 
if __name__ == '__main__':
    app.run(debug=True)