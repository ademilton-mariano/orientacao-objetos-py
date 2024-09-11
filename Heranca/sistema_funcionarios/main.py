from clt import FuncionarioCLT
from pj import FuncionarioPJ


funcionario_clt = FuncionarioCLT("Ana", 5000)
funcionario_pj = FuncionarioPJ("João", 8000)

funcionario_clt.calcular_pagamento()
funcionario_pj.calcular_pagamento()