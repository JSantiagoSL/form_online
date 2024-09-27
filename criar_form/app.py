from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from models import db, Formulario, Pergunta

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    formularios = Formulario.query.all()
    return render_template('index.html', formularios=formularios)

@app.route('/criar', methods=['GET', 'POST'])
def criar_formulario():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        
        novo_formulario = Formulario(titulo=titulo, descricao=descricao)
        db.session.add(novo_formulario)
        db.session.commit()
        
        contador_perguntas = int(request.form.get('contador_perguntas', 0))
        for i in range(contador_perguntas):
            texto_pergunta = request.form.get(f'perguntas[{i}][texto]')
            tipo_pergunta = request.form.get(f'perguntas[{i}][tipo]')
            if texto_pergunta and tipo_pergunta:
                nova_pergunta = Pergunta(texto=texto_pergunta, tipo=tipo_pergunta, formulario_id=novo_formulario.id)
                db.session.add(nova_pergunta)

        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('criar_form.html')

@app.route('/editar/<int:formulario_id>', methods=['GET', 'POST'])
def editar_formulario(formulario_id):
    formulario = Formulario.query.get_or_404(formulario_id)
    
    if request.method == 'POST':
        texto_pergunta = request.form.get('texto_pergunta')
        tipo_pergunta = request.form.get('tipo_pergunta')
        
        if texto_pergunta and tipo_pergunta:
            nova_pergunta = Pergunta(texto=texto_pergunta, tipo=tipo_pergunta, formulario_id=formulario.id)
            db.session.add(nova_pergunta)
            db.session.commit()
        
    return render_template('criar_form.html', formulario=formulario)

@app.route('/deletar/<int:formulario_id>')
def deletar_formulario(formulario_id):
    formulario = Formulario.query.get_or_404(formulario_id)
    
    db.session.delete(formulario)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/visualizar/<int:formulario_id>')
def visualizar_formulario(formulario_id):
    formulario = Formulario.query.get_or_404(formulario_id)
    return render_template('visualizar_form.html', formulario=formulario)

if __name__ == '__main__':
    app.run(debug=True)
