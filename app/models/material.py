from sqlalchemy import Column, Integer, String, Enum, Boolean, Date, Text #import columns necessary
from sqlalchemy.orm import relationship #import relationship table
from enum import TipoMaterial #import file enum TipoMaterial
from app import db
# Tabela Materiais
class Material(db.Model):
    __tablename__ = 'materiais'
    
    id_material = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(150))
    isbn = Column(String(20), unique=True)
    editora = Column(String(100))
    ano_publicacao = Column(Integer)
    tipo_material = Column(Enum(TipoMaterial), nullable=False)
    formato_arquivo = Column(String(10))
    numero_paginas = Column(Integer)
    idioma = Column(String(50))
    area_conhecimento = Column(String(100))
    palavras_chave = Column(Text)
    quantidade_total = Column(Integer)
    quantidade_disponivel = Column(Integer)
    url_arquivo = Column(String(255))
    data_cadastro = Column(Date, nullable=False)
    ativo = Column(Boolean, default=True)
    
    # Relacionamentos
    emprestimos = relationship('Emprestimo', back_populates='material')
    reservas = relationship('Reserva', back_populates='material')