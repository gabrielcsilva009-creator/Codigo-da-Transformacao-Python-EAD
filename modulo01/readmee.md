🎲 Pensamento Computacional — Projetos Python
Repositório oficial do Código da Transformação, criado para aprender, praticar e documentar o desenvolvimento de sistemas reais utilizando Python.

📚 Sobre o Repositório
Este repositório reúne projetos desenvolvidos durante o processo de aprendizagem em Pensamento Computacional e Programação Python.

Os projetos demonstram a evolução desde aplicações simples executadas pelo terminal (CLI) até sistemas com Interface Gráfica (GUI) utilizando Tkinter.

🚀 Projetos
🍧 Sistema de Vendas — Açaiteria: aplicação CLI para cadastro de produtos, consulta de estoque e realização de vendas.
💈 Barber Shop System: aplicação GUI para gerenciamento de serviços, profissionais, vagas e agendamentos.
🍧 Sistema de Vendas — Açaiteria
📌 Sobre o Projeto
O Sistema de Vendas para Açaiteria é uma aplicação desenvolvida em Python que funciona através da linha de comando (CLI).

O sistema foi criado para simular as principais operações de uma açaiteria, permitindo cadastrar produtos, consultar o catálogo e realizar vendas com atualização automática do estoque.

🎯 Objetivos
Praticar fundamentos da linguagem Python.
Desenvolver lógica de programação.
Trabalhar com estruturas condicionais e de repetição.
Implementar controle básico de estoque.
Simular um sistema de vendas.
Preparar a aplicação para futuras evoluções com interface gráfica.
👥 Papéis do Projeto
Papel	Objetivo
PO — Dono do Negócio	Controle de produtos, estoque e vendas.
QA — Visão do Cliente	Garantir um processo de compra simples e rápido.
Tech / Dev	Desenvolver código funcional, organizado e de fácil manutenção.
UX / Designer	Planejar uma experiência de usuário melhor para futuras versões.
IA / Analista de Dados	Preparar o sistema para coleta e análise de dados de consumo.

🔄 Ciclo de Desenvolvimento
Planejamento — definição dos requisitos e necessidades do negócio.
Análise — modelagem dos dados e validação dos requisitos.
Desenvolvimento — implementação da aplicação em Python.
Testes — validação dos fluxos de cadastro, consulta e venda.
Implantação — execução do sistema no terminal.
Manutenção — correção de problemas e preparação para novas funcionalidades.
🚀 Funcionalidades
1. Cadastrar Produto
Permite cadastrar até três produtos, armazenando:

Nome
Quantidade em estoque
Preço
Data de validade
Descrição
2. Listar Produtos
Exibe os produtos cadastrados e suas respectivas informações, incluindo a quantidade disponível em estoque.

3. Realizar Venda
Permite:

Selecionar um produto pelo nome.
Informar a quantidade desejada.
Calcular o valor total.
Verificar a disponibilidade em estoque.
Dar baixa automática no estoque.
0. Sair
Encerra o programa de maneira segura.

🛠️ Tecnologias e Conceitos
Python 3
while True
if / elif / else
Variáveis
Strings
Entrada e saída de dados
.lower()
Formatação de valores com :.2f
Controle de estoque
💻 Como Executar
Pré-requisitos
É necessário possuir o Python 3.x instalado.

Execução
Salve o código em um arquivo chamado, por exemplo:

acaiteria.py

Depois, abra o terminal na pasta do projeto e execute:

python acaiteria.py

Utilize o teclado para navegar pelo menu e selecionar as opções disponíveis.

🔮 Evolução do Projeto — CLI → GUI
Uma das propostas do projeto é evoluir o sistema da Açaiteria de uma aplicação baseada em terminal para uma Interface Gráfica (GUI).

A biblioteca Tkinter pode ser utilizada para criar uma experiência mais intuitiva, incluindo:

Catálogo visual de produtos.
Cadastro e edição de produtos.
Controle visual do estoque.
Registro de vendas.
Histórico de vendas.
Relatórios de faturamento.
Imagens dos produtos.
Interface mais amigável para clientes e administradores.
💈 Barber Shop System
📌 Sobre o Projeto
O Barber Shop System representa uma evolução dos conceitos trabalhados no projeto da Açaiteria.

O sistema foi desenvolvido para facilitar o gerenciamento de serviços e o agendamento de horários em uma barbearia, utilizando uma Interface Gráfica (GUI) construída com Python e Tkinter.

A aplicação possui uma interface temática inspirada nas barbearias clássicas, utilizando uma combinação de azul escuro, dourado, vermelho e grafite.

🚀 Funcionalidades
✂️ Agendamento de Serviços
Permite visualizar os serviços disponíveis e realizar um agendamento.

Cada serviço apresenta:

Nome
Preço
Duração
Quantidade de vagas
Profissionais disponíveis
O cliente pode selecionar um barbeiro e confirmar o agendamento.

🛠️ Gerenciamento de Serviços
Permite editar as informações dos serviços cadastrados:

Nome
Barbeiros
Preço
Duração
Descrição
Quantidade de vagas
Os dados são atualizados diretamente na aplicação.

📊 Status do Estoque e Vagas
Apresenta visualmente a quantidade de vagas disponíveis para cada serviço.

Quando o estoque chega a zero, o sistema identifica o serviço como esgotado.

📍 Localização e Contato
Apresenta informações como:

Endereço
Ponto de referência
Telefone
WhatsApp
E-mail
💈 Sobre a Barbearia
Exibe informações sobre:

A empresa
Horário de funcionamento
Proposta do estabelecimento
Créditos da equipe responsável pelo projeto
🛠️ Tecnologias
Python 3
Tkinter
TTK
Listas
Dicionários
Funções
Classes
Programação Orientada a Objetos (POO)
Programação Orientada a Eventos
lambda
bind
messagebox
Combobox
🧱 Estrutura de Dados
Os serviços são armazenados utilizando uma lista de dicionários:

servicos = [
    {
        "nome": "Corte",
        "barbeiros": "Gustavo, Nicolas, Felipe, Victor",
        "preco": 30.00,
        "validade": "7 dias",
        "descricao": "O melhor corte da região.",
        "estoque": 10,
    }
]

Essa estrutura facilita a criação, consulta e alteração dos serviços.

🖥️ Interface Gráfica
A aplicação possui uma estrutura dividida em:

┌──────────────────────────────────────────────┐
│          💈 BARBER SHOP SYSTEM 💈           │
│       Tradição, Estilo e Modernidade        │
├────────────────┬─────────────────────────────┤
│                │                             │
│   NAVEGAÇÃO    │      ÁREA DE CONTEÚDO      │
│                │                             │
│ Agendar        │                             │
│ Serviços       │                             │
│ Estoque        │                             │
│ Contato        │                             │
│ Sobre          │                             │
│                │                             │
│ Sair           │                             │
└────────────────┴─────────────────────────────┘

A aplicação utiliza diferentes componentes do Tkinter, como:

Frame
Label
Button
Entry
LabelFrame
Combobox
Toplevel
messagebox
👨‍💻 Estrutura do Código
A aplicação utiliza a classe principal:

class BarbeariaApp:

Ela é responsável por controlar a interface e as principais ações do sistema.

Entre seus métodos estão:

criar_menu()
limpar_tela_conteudo()
criar_titulo_secao()
mostrar_home()
mostrar_agendamento()
popup_escolher_barbeiro()
mostrar_gerenciamento()
mostrar_estoque()
mostrar_info()
mostrar_sobre()

Essa organização facilita a manutenção e permite adicionar novas funcionalidades futuramente.

🎨 Identidade Visual
O projeto utiliza uma paleta inspirada em barbearias tradicionais:

Cor	Código	Utilização
Grafite	#1A1A1A	Fundo principal
Cinza escuro	#262626	Cards e painéis
Branco	#FFFFFF	Textos
Dourado	#D4AF37	Destaques
Azul	#1E3A8A	Botões
Vermelho	#991B1B	Alertas e saída

👥 Participantes
🌆 Turma da Tarde — Segunda e Terça
Equipe responsável pelo desenvolvimento e aprimoramento do Barber Shop System:

✂️ Gabriel Carvalho
✂️ Nicolas
✂️ Kauan
✂️ Felipe
✂️ Gustavo
✂️ Victor
Para consultar a lista completa de participantes e outros projetos desenvolvidos, consulte as demais seções do repositório.

📈 Evolução dos Projetos
Os projetos representam uma evolução gradual dos conhecimentos adquiridos:

Python Básico
     ↓
Estruturas Condicionais
     ↓
Laços de Repetição
     ↓
Listas e Dicionários
     ↓
Funções
     ↓
Programação Orientada a Objetos
     ↓
Tkinter
     ↓
Interface Gráfica
     ↓
Persistência de Dados
     ↓
Relatórios e Análise de Dados

🔮 Próximos Passos
Para futuras versões dos sistemas, estão planejadas funcionalidades como:

 Banco de dados SQLite.
 Login de administrador.
 Cadastro de clientes.
 Cadastro de funcionários.
 Histórico de vendas e agendamentos.
 Relatórios de faturamento.
 Controle de horários.
 Pesquisa e filtros.
 Exportação de relatórios.
 Dashboard com indicadores.
 Integração com análise de dados.
 Melhorias na experiência do usuário.
 Sistema de notificações.
 Persistência dos dados após fechar o programa.
🎓 Objetivo Educacional
O principal objetivo deste repositório é documentar a evolução prática no desenvolvimento de sistemas utilizando Python.

Através dos projetos, são trabalhados conceitos de:

Pensamento computacional.
Lógica de programação.
Estruturação de dados.
Programação Orientada a Objetos.
Desenvolvimento de interfaces.
Experiência do usuário.
Controle de estoque.
Sistemas de vendas.
Sistemas de agendamento.
Organização e manutenção de código.
📂 Organização Sugerida do Repositório
codigo-da-transformacao/
│
├── README.md
│
├── acaiteria/
│   └── acaiteria.py
│
└── barbearia/
    └── barbearia.py

🏁 Conclusão
O Sistema de Vendas da Açaiteria representa o início do desenvolvimento de aplicações em Python utilizando a linha de comando.

O Barber Shop System demonstra a evolução desses conhecimentos para uma aplicação gráfica mais completa, utilizando Tkinter, listas, dicionários e Programação Orientada a Objetos.

Dessa forma, o repositório documenta não apenas os sistemas desenvolvidos, mas também a evolução do aprendizado em programação e desenvolvimento de software.

🐍 Python • 💻 Tecnologia • 🎓 Aprendizado • 🚀 Evolução