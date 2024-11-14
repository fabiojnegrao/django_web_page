from django.db import models

# Create your models here.
# Criar as entidades e propriedades 

class Paciente(models.Model): # Definindo as escolhas para o tipo de profissional de saúde
    id = models.AutoField(primary_key=True) # Define o campo 'id' como chave primária automática
    nome = models.CharField(max_length=100) # Nome do paciente
    telefone = models.CharField(max_length=15) #  Campo para telefone, com max_length configurado para 15 caracteres
    cpf = models.CharField(max_length=11, unique=True)  # CPF único com exatamente 11 caracteres
    # prontuario = models.ForeignKey (Prontuario)
    # prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)  # Relacionamento com Prontuario

class Profissional_de_saude(models.Model): 
    id = models.AutoField(primary_key=True) # Define o campo 'id' como chave primária automática
    nome = models.CharField(max_length=100) # Nome do profissional
    tipo_profissional_escolha = [ # categoria do profissional
        ('MÉDICO', 'Médico'),
        ('ENFERMEIRO', 'Enfermeiro'),
        ('NUTRICIONISTA', 'Nutricionista'),
        ('PSICÓLOGO', 'Psicólogo'),
        ('FISIOTERAPEUTA', 'Fisioterapeuta'),
        ('FARMACÊUTICO', 'Farmacêutico'),
        ('BIOMÉDICO', 'Biomédico'),
        ('TÉCNICO_ENFERMAGEM', 'Técnico de Enfermagem'),
        ('AGENTE_DE_SAÚDE', 'Agente de Saúde'),
        ('OUTROS', 'Outros')
    ]
    tipo_profissional = models.CharField( 
        max_length = 20,
        choices = tipo_profissional_escolha,
        default ='OUTROS'
    )
    registro_profissional_escolha = [
        ('MÉDICO', 'CRM'),
        ('ENFERMEIRO', 'COREN E'),
        ('NUTRICIONISTA', 'CRN'),
        ('PSICÓLOGO', 'CRP'),
        ('FISIOTERAPEUTA', 'CREFito'),
        ('FARMACÊUTICO', 'CRF'),
        ('BIOMÉDICO', 'CRBm'),
        ('TÉCNICO_ENFERMAGEM', 'COREN TE'),
        ('AGENTE_DE_SAÚDE', 'Estratégia de Saúde-ESF/UBS/Posto'),
        ('OUTROS', 'Outros')
    ]
    registro_profissional_escolha = models.CharField(
        max_length = 8,
        choices=registro_profissional_escolha,
        default='OUTROS'
    ) 
    numero_registro_profissional = models.CharField(max_length=8, unique=True)
    # prontuario = models.ForeignKey (Prontuario)
    # prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)  # Relacionamento com Prontuario
    #id_endereco
    3 
class Estabelecimento_de_saude(models.Model): 
    id = models.AutoField(primary_key=True) # Define o campo 'id' como chave primária automática
    nome = models.CharField(max_length=100) # Nome do profissional
    cnes = models.CharField(max_length=10)
    cnpj = models.CharField(max_length=14, unique=True)
    estabelecimento_de_saude = [ # tipo de estabelecimento
        ('CLINICA', 'Clínica'),
        ('HOSPITAL', 'Hospital'),
        ('ESTRATÉGIA_DE_SAÚDE ', 'Estratégia de saúde'),
        ('OUTROS', 'Outros')
    ]
    estabelecimento_de_saude = models.CharField( 
        max_length = 20,
        choices= estabelecimento_de_saude,
        default='OUTROS'
    )

class Endereco (models.model):
    id = models.AutoField(primary_key=True)
    rua = models.ChartField(max_length = 30)
    numero = models.IntegerField(max_lenght = 8)
    bairro = models.ChartField(max_length = 30)
    complemento = models.ChartField(max_length = 30)
    uf = models.ChartField(max_length = 15)
    cep = models.CharField(max_length=8, unique=True)  # CEP único com exatamente 8 caracteres

class Prontuario(models.Model):
    id = models.AutoField(primary_key=True) # Define o campo 'id' como chave primária automática
    paciente = models.ForeignKey(Paciente) #chave estrangeira exemplo Prontuario_id 
     # Qual é a hierarquia da classe? Um paciente existe sem prontuário, contudo, um prontuário
    profissional_saude = models.ForeignKey(Profissional_de_saude)
    # descricao_sinais = 


