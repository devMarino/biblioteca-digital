from sqlalchemy import Column,Integer, Enum, Date,ForeignKey #import columns necessary
from sqlalchemy.orm import relationship #import relationship table
from enum import StatusReserva #import file enum StatusReserva
from app import db #import instance db

# Tabela Reserva
class Reserva(db.Model):
    __tablename__ = 'reservas'
    
    id_reserva = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    id_material = Column(Integer, ForeignKey('materiais.id_material'), nullable=False)
    data_reserva = Column(Date, nullable=False)
    data_expiracao = Column(Date, nullable=False)
    status = Column(Enum(StatusReserva), default=StatusReserva.ativa)
    
    # Relacionamentos
    usuario = relationship('Usuario', back_populates='reservas')
    material = relationship('Material', back_populates='reservas')
