#flask precisa da pasta templates para rodar o html, em qqr lugar que eu programar
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
@app.route('/entrar/')
def admin_index():
  return render_template('login.html') #carregar no local a pasta entrar

@app.route('/login/', methods=['POST', 'GET'])
def login():
  if request.method == 'POST': 
    usuario=request.form['c_usuario']
    senha=request.form['c_senha']
    if usuario == "lorena" and senha == 123:
      return redirect(url_for('admin', nome=usuario, senha=senha)) # indo para a rota admin
    else:
      return redirect(url_for('login'))
  else:
    usuario=request.args.get('c_usuario')
    senha=request.args.get('c_senha')
    if usuario == "lorena" and senha == 123:
      return redirect(url_for('admin', nome=usuario, senha=senha))
    else:
      return redirect(url_for('login'))
      
@app.route('/admin/<nome>/<senha>')
def admin(nome, senha):
  frase="<b> bem vindo </b>" + nome + "a senha e: <i>" + senha + "</i>" 
  # b negrito i italico
  return frase
  
if __name__ == '__main__':
  app.run('0.0.0.0') 
#ou '127.0.0.1': local host