import enum

class TipoUsuario(enum.Enum):
    aluno = 'aluno'
    docente = 'docente'
    colaborador = 'colaborador'
    administrador = 'administrador'

class TipoMaterial(enum.Enum):
    livro_fisico = 'livro_fisico'
    ebook = 'ebook'
    periodico = 'periodico'
    outro = 'outro'

class StatusEmprestimo(enum.Enum):
    ativo = 'ativo'
    devolvido = 'devolvido'
    atrasado = 'atrasado'

class StatusReserva(enum.Enum):
    ativa = 'ativa'
    cancelada = 'cancelada'
    concluida = 'concluida'
    expirada = 'expirada'

class TipoNotificacao(enum.Enum):
    aviso_devolucao = 'aviso_devolucao'
    atraso = 'atraso'
    reserva_disponivel = 'reserva_disponivel'
    outro = 'outro'

class StatusNotificacao(enum.Enum):
    pendente = 'pendente'
    enviado = 'enviado'
    lido = 'lido'