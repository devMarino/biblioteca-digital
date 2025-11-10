from . import db
import enum

#create enum class for user types
class myEnum(enum.Enum):
    aluno = 'aluno'
    docente = 'docente'
    colaborador = 'colaborador'
    admin = 'admin'

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(50), unique=True, nullable=False)
    tipo = db.Column(db.Enum(myEnum), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    senha = db.Column(db.String(200), nullable=False)


    