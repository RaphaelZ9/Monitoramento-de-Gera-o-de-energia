# ⚡ Monitoramento de Geração de Energia

Aplicação web desenvolvida para **consulta e monitoramento de dados de geração de energia de inversores**, permitindo analisar informações em diferentes níveis de resolução e períodos de consulta.

O projeto utiliza **Python com Flask** no backend e uma interface web em **HTML, CSS e JavaScript**, integrando-se ao **Supabase** por meio de sua API REST e funções RPC.

## 🚀 Funcionalidades

* Consulta de geração por data
* Consulta com resolução de **1 hora ou 15 minutos**
* Definição opcional de hora inicial e final
* Consulta do dia completo quando o intervalo de horas não é informado
* Atalhos para consulta de **Hoje** e **Ontem**
* Aplicação opcional de limite/margem de chamada
* Exibição dos resultados em tabela
* Endpoint de verificação de saúde da aplicação
* Comunicação com o Supabase através de API REST
* Tratamento de erros e validação dos parâmetros de consulta

## 🏗️ Arquitetura

```text
┌──────────────────────────────┐
│       Interface Web          │
│       HTML / CSS / JS        │
└──────────────┬───────────────┘
               │
               │ HTTP / JSON
               ▼
┌──────────────────────────────┐
│       Python + Flask         │
│                              │
│  /api/health                 │
│  /api/consulta               │
└──────────────┬───────────────┘
               │
               │ REST API
               ▼
┌──────────────────────────────┐
│           Supabase           │
│                              │
│  RPC energia_inversor_1hr    │
│  RPC energia_inversor_15min  │
└──────────────────────────────┘
```

## 🛠️ Tecnologias

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **JavaScript**
* **REST API**
* **JSON**
* **Supabase**
* **PostgreSQL / RPC**
* **python-dotenv**
* **Requests**

## 🔌 API

O backend disponibiliza endpoints para comunicação entre a interface e o banco de dados.

### Health Check

```http
GET /api/health
```

Verifica se as configurações necessárias para comunicação com o Supabase estão disponíveis.

### Consulta

```http
POST /api/consulta
```

Recebe parâmetros como:

```json
{
  "data": "YYYY-MM-DD",
  "resolucao": "1hr",
  "hora_inicio": 8,
  "hora_fim": 18,
  "limite_ativo": false
}
```

A aplicação valida os parâmetros recebidos e realiza a chamada à RPC correspondente no Supabase.

## 📊 Resoluções disponíveis

### 1 hora

Utiliza:

```text
energia_inversor_1hr
```

### 15 minutos

Utiliza:

```text
energia_inversor_15min
```

As duas operações são realizadas através da API REST do Supabase.

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/RaphaelZ9/Monitoramento-de-Gera-o-de-energia.git
```

### 2. Entre na pasta

```bash
cd Monitoramento-de-Gera-o-de-energia
```

### 3. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

No Windows:

```powershell
.venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Configure as variáveis de ambiente

Copie:

```text
.env.example
```

para:

```text
.env
```

e configure as variáveis necessárias para conexão com o Supabase.

### 7. Execute a aplicação

```bash
python app.py
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8080
```

## 📁 Estrutura do projeto

```text
Monitoramento-de-Gera-o-de-energia/
│
├── app.py
├── index.html
├── favicon.svg
├── requirements.txt
├── .env.example
├── Iniciar Monitor de Geracao.bat
├── Iniciar Monitor de Geracao.vbs
└── README.md
```

## 🎯 Objetivo técnico

O projeto demonstra a integração entre **interface web, backend Python, APIs REST e banco de dados**, utilizando o Supabase como camada de dados e RPCs para execução das consultas.

Também demonstra práticas de:

* validação de entradas;
* comunicação HTTP;
* processamento de JSON;
* tratamento de erros;
* integração com serviços externos;
* organização de uma aplicação web com backend e frontend separados.

## 📌 Projeto

Desenvolvido por **Raphael Wilson** como projeto de desenvolvimento e monitoramento de dados de geração de energia.

---

### Tecnologias principais

`Python` `Flask` `JavaScript` `HTML` `CSS` `REST API` `JSON` `Supabase` `PostgreSQL`
