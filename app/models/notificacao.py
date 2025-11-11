from sqlalchemy import Column,Integer, Enum, Text, ForeignKey, DateTime #import columns necessary
from sqlalchemy.orm import relationship #import relationship table
from .enum import TipoNotificacao, StatusNotificacao #import file enum TipoNotificacao and StatusNotificacao
from app import db #import instance db


# Tabela Notificações
class Notificacao(db.Model):
    __tablename__ = 'notificacao'
    
    id_notificacao = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    tipo_notificacao = Column(Enum(TipoNotificacao), nullable=False)
    mensagem = Column(Text, nullable=False)
    data_envio = Column(DateTime, nullable=False)
    status = Column(Enum(StatusNotificacao), default=StatusNotificacao.pendente)
    
    # Relacionamento
    usuario = relationship('usuario', back_populates='notificacao')