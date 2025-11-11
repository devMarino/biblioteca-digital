from flask import Blueprint, request, jsonify
from app import db
from app.models.emprestimo import Emprestimo

emprestimo_bp = Blueprint('emprestimo', __name__)

@emprestimo_bp.route('', methods=['GET'])
def get_all_emprestimos():
    try:
        emprestimos = Emprestimo.query.all()
        output = []

        for emprestimo in emprestimos:
            output.append({
                'id_emprestimo': emprestimo.id_emprestimo,
                'id_usuario': emprestimo.id_usuario,
                'id_material': emprestimo.id_material,
                'data_emprestimo': emprestimo.data_emprestimo.isoformat()if emprestimo.data_emprestimo else None,
                'data_devolucao': emprestimo.data_devolucao.isoformat() if emprestimo.data_devolucao else None
            })
        return jsonify(output), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@emprestimo_bp.route('', methods=['POST'])
def create_emprestimo():

    from datetime import date

    try:
        data = request.get_json()
        
        id_usuario = data.get('id_usuario')

        if not id_usuario:
            return jsonify({'error': 'ID do usuário é obrigatório.'}), 400
        id_material = data.get('id_material')

        if not id_material:
            return jsonify({'error': 'ID do material é obrigatório.'}), 400
        
        data_emprestimo = data.get('data_emprestimo')
        if not data_emprestimo:
            return jsonify({'error': 'Data do empréstimo é obrigatória.'}), 400
        
        data_prevista_devolucao = data.get('data_prevista_devolucao')
        if not data_prevista_devolucao:
            return jsonify({'error': 'Data prevista de devolução é obrigatória.'}), 400

        
        novo_emprestimo = Emprestimo(
        id_usuario=data['id_usuario'],
        id_material=data['id_material'],
        data_emprestimo=date.fromisoformat(data['data_emprestimo']),
        data_prevista_devolucao=date.fromisoformat(data['data_prevista_devolucao']),
        observacoes=data.get('observacoes', '')
        )
        
        db.session.add(novo_emprestimo)
        db.session.commit()

        return jsonify({'message': 'Emprestimo realizado', 'emprestimo_id': novo_emprestimo.id_emprestimo}), 201

    except Exception as e:
        db.session.rollback() 
        return jsonify({'error': str(e)}), 500

@emprestimo_bp.route('/<int:emprestimo_id>', methods=['PUT'])
def put_all_emprestimo(emprestimo_id): 
    from datetime import date
    try:
        emprestimo = Emprestimo.query.get(emprestimo_id)
        if not emprestimo:
            return jsonify({'error': f'Emprestimo {emprestimo_id} não encontrado'}), 404
        
        if emprestimo.data_devolucao:
            return jsonify({'error': 'Emprestimo já foi devolvido'}), 200
        
        emprestimo.data_devolucao = date.today()

        db.session.commit()

        return jsonify ({'message': 'Emprestimo devolvido com sucesso', 'id_emprestimo': emprestimo.id_emprestimo, 'data_devolução': emprestimo.data_devolucao.isoformat()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    

    

