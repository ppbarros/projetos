logins = {'ppbar':'2112', 'kyoto': '2424'}

projetos = {'ppbar': [['Projeto1', '21/04/2019', 'João Pedro'], ['Projeto2', '23/09/2019', 'Pedro Paulo'], ['Projeto3', '12/05/2019', 'Felipe Maia']],
            'kyoto': [['Projeto1', '21/04/2019', 'João Pedro'], ['Projeto2', '23/09/2019', 'Pedro Paulo'], ['Projeto4', '08/11/2019', 'Luís Paulo']]}

atividades = {'Projeto1': ['Planejar', 'Construir', 'Autorizar'], 'Projeto2': ['Construir', 'Revisar'], 'Projeto3': ['Manutenção'], 'Projeto4': ['Planejar', 'Revisar']}

detalhe = {'Planejar': 'Descrição de Planejar', 'Construir': 'Descrição de Construir', 'Revisar': 'Descrição de Revisar', 'Autorizar': 'Descrição de Autorizar', 'Manutenção': 'Descrição de Manutenção'}

def validar(user, passw):
    return (user in logins) and (logins[user] == passw)

def get_projetos(user):
    return projetos[user]

def get_atividades(projeto):
    return atividades[projeto]

def get_detalhe(atividade):
    return detalhe[atividade]