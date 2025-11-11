from flask import Blueprint, request, jsonify
from app import db
from app.models.usuario import Usuario 
from app.models.enum import TipoUsuario

usuario_bp = Blueprint('usuario', __name__)

# @usuario_bp.route('', methods=['GET'])
# def get_all_usuario():
#     try:
#         emprestimos = Emprestimo.query.all()
#         output = []

#         for emprestimo in emprestimos:
#             output.append({
#                 'id_emprestimo': emprestimo.id_emprestimo,
#                 'id_usuario': emprestimo.id_usuario,
#                 'id_material': emprestimo.id_material,
#                 'data_emprestimo': emprestimo.data_emprestimo.isoformat()if emprestimo.data_emprestimo else None,
#                 'data_devolucao': emprestimo.data_devolucao.isoformat() if emprestimo.data_devolucao else None
#             })
#         return jsonify(output), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('', methods=['POST'])
def create_usuario():
    from datetime import date
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'Requisição sem corpo JSON.'}), 400

        required_fields = ['nome', 'matricula', 'tipo_usuario', 'turma', 'senha', 'email', 'data_cadastro']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Campos obrigatórios faltando.'}), 400

        if Usuario.query.filter_by(email=data['email']).first():
            return jsonify({'erro': 'Email já cadastrado'}), 409


        valor_enum = data.get('tipo_usuario')
        try:
            tipo_usuario = TipoUsuario(valor_enum)
        except ValueError:
            return jsonify({
                'error': f"Valor inválido para tipo_usuario: {valor_enum}. "
                         f"Use um dos seguintes: {[e.value for e in TipoUsuario]}"
            }), 400

        novo_usuario = Usuario(
            nome=data['nome'],
            matricula=data['matricula'],
            tipo_usuario=tipo_usuario, 
            turma=data['turma'],
            senha=data['senha'],
            email=data['email'],
            telefone=data.get('telefone'),
            data_cadastro=date.fromisoformat(data['data_cadastro']),
            ativo=data.get('ativo', True)
        )

        db.session.add(novo_usuario)
        db.session.commit()

        return jsonify({
            'message': 'Usuário cadastrado com sucesso.',
            'usuario_id': novo_usuario.id_usuario,
            'tipo_usuario': novo_usuario.tipo_usuario.value
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# @emprestimo_bp.route('/<int:emprestimo_id>', methods=['PUT'])
# def put_all_emprestimo(emprestimo_id): 
#     from datetime import date
#     try:
#         emprestimo = Emprestimo.query.get(emprestimo_id)
#         if not emprestimo:
#             return jsonify({'error': f'Emprestimo {emprestimo_id} não encontrado'}), 404
        
#         if emprestimo.data_devolucao:
#             return jsonify({'error': 'Emprestimo já foi devolvido'}), 200
        
#         emprestimo.data_devolucao = date.today()

#         db.session.commit()

#         return jsonify ({'message': 'Emprestimo devolvido com sucesso', 'id_emprestimo': emprestimo.id_emprestimo, 'data_devolução': emprestimo.data_devolucao.isoformat()}), 200
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500
    

    

