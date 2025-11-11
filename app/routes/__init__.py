#import blueprints
from .emprestimo_routes import emprestimo_bp
from .usuario_routes import usuario_bp
from .material_routes import material_bp
from .reserva_routes import reserva_bp

#all blueprints and their url prefixes
ALL_BLUEPRINTS = [
    (emprestimo_bp, '/api/emprestimo'),
    (usuario_bp, '/api/usuario'),
    (material_bp, '/api/materiai'),
    (reserva_bp, '/api/reserva'),

]