import datetime


class DataBase:
    def __init__(self, filename):
        self._filename = filename
        self._users = None
        self._file = None
        self._load()

    def _load(self):
        self._file = open(self._filename, 'r') # Abre o arquivo especificado pelo nome em modo de leitura
        self._users = {} # Inicializa o atributo como um dicionário vazio

        for line in self._file:
            email, password, name, created = line.strip().split(';') # Divide cada linha do arquivo em quatro partes separadas por ponto e vírgula e atribui essas partes às variáveis email, password, name e created
            self._users[email] = (password, name, created) # Armazena os dados do usuário no dicionário _users usando o email como chave

        self._file.close() # Fecha o arquivo

    def get_user(self, email):
        if email in self._users:
            return self._users[email]
        else:
            print('Usuário não encontrado')
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self._users:
            self._users[email.strip()] = (
                password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print('Email já existente')
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self._users[email][0] == password
        else:
            print('Email não existente')
            return False

    def save(self):
        with open(self._filename, 'w') as f:
            for user in self._users:
                f.write(user + ';' + self._users[user][0] + ';' +
                        self._users[user][1] + ';' + self._users[user][2] + '\n')

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(' ')[0]
