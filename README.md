# Sprint 1: 25/03/2024 à 14/04/2024

O projeto se baseia no desenvolvimento de um site para Help Desk, que consiste em um sistema com funcionalidades de gerenciamento de usuários, chamados, geração de relatórios, entre outras ações do contexto. Tendo em mente o MVP, a primeira sprint se deu com a criação de um fluxo básico de criação de usuários, login e listagem de chamados, bem como o acompanhamento desses chamados com sua abertura, análise e fechamento. Para isso, foram levantados e validados os requisitos e o protótipo, construindo os serviços e interfaces visando uma entrega de grande valor condizente com a dor do cliente.

## 🎯 Objetivos 

 - Definir o propósito do projeto;
 - Elaborar o protótipo da aplicação;
 - Escolher a identidade visual;
 - Configurar o ambiente de desenvolvimento;
 - Desenvolver a base do website;
 - Elaborar o backlog inicial e o plano de entrega;
 - Integrar os gráficos gerados a partir de um arquivo CSV com a interface do usuário;
 - Empacotar a aplicação com Docker;
 - Criar o vídeo de apresentação;
 - Implementar a funcionalidade de importação de arquivos CSV no site;
 - Realizar a transformação automática dos dados em gráficos.

# 🧾 Requisitos Funcionais

Os requisitos desenvolvidos durante esta sprint foram:

Requisito funcional | Sprint | Prioridade |
|------|--------|------|
| Apresentar os gráficos, incluindo datas e horários de captura. | 1 | Alta |
| Importar e converter dados de um arquivo CSV. | 1 | Alta |
| Apresentar os gráficos, incluindo datas e horários de captura.| 1 | Alta |


## 📅 Métricas do Time

Utilizamos o Burndown chart para acompanhar o progresso da equipe durante o andamento da sprint (o eixo X são os dias trabalhados na sprint e os valores do eixo Y representam as entregas e esforços realizados com o passar do tempo)

 ![image](https://github.com/user-attachments/assets/abe009e9-32bc-4d4b-a915-9fb990da0ece)



<br>

<span id="demostracao">
  
# 💻 Demonstração

Apresentação das funcionalidades desenvolvidas até o momento:

[![Smartfarm - demonstration](https://img.youtube.com/vi/bqNpXkbuNLw/0.jpg)](https://youtu.be/bqNpXkbuNLw)

<span id="tecnologias">

# 🛠️ Tecnologias Utilizadas

As seguintes ferramentas, linguagens, bibliotecas e tecnologias foram usadas na construção do projeto:

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)

<br>

# 📘 Munual do usuário

Para ter informações de:
- Processo de instalação
- Acesso do programa
- Funções da plataforma

[Acesse aqui!](https://github.com/andresalerno/projeto_api/blob/main/Manual.pdf)

<span id="backlog">

# 🧾 Backlog do produto

Requisito funcional | Sprint | Prioridade |
|------|--------|------|
| Exibir os últimos dados coletados das variáveis essenciais: temperatura, umidade do solo, umidade ambiente e volume da água. | 1 | Alta |
| Importar e converter dados de um arquivo CSV. | 2 | Alta |
| Apresentar os gráficos, incluindo datas e horários de captura.| 2 | Alta |
| Exportar dados de um período selecionado pelo usuário em CSV.| 2 | Média |
| Armazenar os dados no banco de dados. | 3 | Alta |
| Permitir a seleção de conjuntos de dados e combinações para períodos específicos, incluindo filtragem de dados | 3 | Alta |

## Sprint 1. Concepção
- [x] Definir o propósito do projeto;
- [x] Elaborar o protótipo da aplicação;
- [x] Escolher a identidade visual;
- [x] Configurar o ambiente de desenvolvimento;
- [x] Desenvolver a base do website;
- [x] Elaborar o backlog inicial e o plano de entrega;
- [x] Integrar os gráficos gerados a partir de um arquivo CSV com a interface do usuário;
- [x] Empacotar a aplicação com Docker;
- [x] Criar o vídeo de apresentação;
- [x] Implementar a funcionalidade de importação de arquivos CSV no site;
- [x] Realizar a transformação automática dos dados em gráficos.

## Sprint 2. Desenvolvimento do Projeto
- [x] Desenvolver a funcionalidade de importação e conversão automática dos dados do CSV para o banco de dados;
- [x] Permitir o download de todos os dados;
- [x] Implementar a exibição dos últimos dados coletados das variáveis essenciais;
- [x] Testar a funcionalidade de apresentação de gráficos e exportação de dados;
- [x] Desenvolver a funcionalidade de armazenamento dos dados no banco de dados;
- [x] Realizar a adaptação da página web para diferentes dispositivos e tamanhos de tela.

## Sprint 3. Implementação
- [x] Permitir o download dos dados selecionados;
- [x] Hospedar o website a partir do Raspberry Pi 3;
- [x] Implementar a seleção de conjuntos de dados e combinações para períodos específicos, incluindo a filtragem de dados;
- [x] Testar a responsividade da página e a funcionalidade de filtragem.

## Sprint 4. Operacionalização
- [ ] Implementar o botão de limpar filtro
- [ ] Implementar função de baixar por período selecionado pelo filtro
- [ ] Tratamento do erro de ao filtrar o período deve permanecer no input
- [ ] Tratamento do erro de filtro de data inexistente no banco
- [ ] Tratamento do erro de importar dados duplicados
- [ ] Realizar testes de integração para garantir o funcionamento correto de todas as funcionalidades;
- [ ] Corrigir eventuais bugs encontrados durante os testes.

<br>

<span id="autores">

# 👥 Autores


|    Função     | Nome                                  |                                                                                                                                                      LinkedIn & GitHub                                                                                                                                                      |
| :-----------: | :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Product Owner |   Mariane Valério Nunes         |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)]() [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/Marianne10)              |
| Scrum Master  | André Salerno |      [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/andresalerno/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/andresalerno)     |
| Team Member   | Eric Lourenço Mendes da Silva      |         [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)]() [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/ericloumendes)        |
|  Team Member  | Gustavo Muraoka Silva                 |         [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/gustavo-muraoka-4256721ba/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/gustavomuraoka)        |
|  Team Member  | Sarah Montuani Batagioti               |   [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/sarahbatagioti/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/SarahBatagioti)   |
|  Team Member  | Karen de Cássia Gonçalves     |           [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/karen-cgonçalves) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/karengoncalves8)   |
|  Team Member  | Brenno Rosa Lyrio de Oliveira               |   [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/brennolyrio/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/BrennoLyrio)   |
|  Team Member  | Guilherme dos Santos Benedito               |   [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-benedito/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/gui-benedito)   |
|  Team Member  | Arthur Johannes Rodrigues Peres y Peres              |   [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/ajperes/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/ajperes)   |

![image 6](https://github.com/andresalerno/projeto_api/assets/105525498/a7ca2b45-b638-4ae3-a1aa-d4b533acc6ab)
