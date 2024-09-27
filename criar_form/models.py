from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Formulario(db.Model):
    __tablename__ = 'formulario'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    perguntas = db.relationship('Pergunta', backref='formulario', cascade="all, delete-orphan", lazy=True)

class Pergunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    formulario_id = db.Column(db.Integer, db.ForeignKey('formulario.id'), nullable=False)
