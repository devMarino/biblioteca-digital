from sqlalchemy import Column,Integer, String,Text, ForeignKey, DateTime #import columns necessary
from sqlalchemy.orm import relationship #import relationship table
from app import db #import instance db

# Tabela Logs de Acesso
class LogAcesso(db.Model):
    __tablename__ = 'logs_acesso'
    
    id_log = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    acao = Column(String(100), nullable=False)
    descricao = Column(Text)
    data_hora = Column(DateTime, nullable=False)
    
    # Relacionamento
    usuario = relationship('Usuario', back_populates='logs_acesso')