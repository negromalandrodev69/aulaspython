# Solicite ao usuário um CEP e realize a requisição HTTP utilizando a API ViaCEP.
# Exiba os dados retornados pela API, como logradouro, bairro, cidade e estado.
# Armazene os resultados no arquivo historico_pesquisa.json, utilizando with open() e a biblioteca json.
# Organize os registros em uma , na qual cada pesquisa representa um novo dicionário.
# Preserve as pesquisas anteriores ao adicionar novos registros ao arquivo.Trate erros, como falhas de conexão, CEP inexistente e arquivo ainda não criado.

#1
import requests, json

dicinario_dados_cep = []
nova_pesquisa = []

with open('historico_pesquisa.json', 'r', encoding='utf-8') as file:
    dicinario_dados_cep.append(json.load(file))

while True:                              # Coloca o link alterado em uma vaiavel com o intuito de preencher a API
    cep_digitado = input('Digite o CEP: ')
    link = f'https://viacep.com.br/ws/{cep_digitado}/json/'
    resposta = requests.get(link)
    print(resposta.json())

    nova_pesquisa.append(resposta.json())
    dicinario_dados_cep.extend(nova_pesquisa)

    for dados in dicinario_dados_cep:
        print(f'\nLogradouro: {dados["logradouro"]}\n'
              f'Bairro: {dados["bairro"]}\n'
              f'Cidade: {dados["localidade"]}\n'
              f'Estado: {dados["estado"]}\n')

    with open('historico_pesquisa.json', 'w', encoding='utf8') as arquivo:
        json.dump(dicinario_dados_cep, arquivo, ensure_ascii=False, indent=4)

        opcao = input("Gite 'sair' para finalizar...")
        if opcao == 'sair':
            break

# Ainda falta codigo para definir a unidade
