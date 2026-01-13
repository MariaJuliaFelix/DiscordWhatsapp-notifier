# 🚨 Discord Smart Notifier

Sistema de notificações em tempo real que monitora mensagens no Discord e envia alertas automáticos para o WhatsApp quando conteúdos relevantes são detectados.

O objetivo do projeto é garantir que mensagens importantes não passem despercebidas, mesmo quando o usuário não está ativo na plataforma original.

---

## ✨ Funcionalidades

- 🤖 Bot do Discord escutando mensagens em tempo real
- 🔍 Filtro de mensagens por palavras-chave
- 📲 Envio automático de alertas para o WhatsApp
- 🔐 Uso de variáveis de ambiente para dados sensíveis
- 🧱 Arquitetura desacoplada (evento → regra → notificação)

---

## 🧠 Como funciona

O sistema segue o fluxo abaixo:

Discord → Detecção de mensagem → Regra de decisão → WhatsApp


1. O bot monitora mensagens em canais do Discord
2. Cada mensagem é avaliada com base em regras simples de relevância
3. Quando uma condição é atendida, um alerta é enviado para o WhatsApp via Twilio

---

## 🛠 Tecnologias utilizadas

- **Python**
- **discord.py** — integração com a API do Discord
- **Twilio API (WhatsApp Sandbox)** — envio de mensagens
- **python-dotenv** — gerenciamento de variáveis de ambiente

---

## 📁 Estrutura do projeto

discord-smart-notifier/
│
├─ bot/
│ ├─ bot.py # Listener do Discord
│ ├─ rules.py # Regras de decisão
│ └─ notifier.py # Envio de notificações (WhatsApp)
│
├─ teste_whatsapp.py # Teste isolado do Twilio
├─ .env # Variáveis de ambiente (não versionado)
├─ .gitignore
└─ README.md


---

## ⚙️ Configuração

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/discord-smart-notifier.git
cd discord-smart-notifier 
```

### 2️⃣ Crie e ative a virtualenv
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Instale as dependências
```bash
pip install discord.py python-dotenv twilio
```
### 4️⃣ Configure o .env

Crie um arquivo .env na raiz do projeto:
```bash
DISCORD_TOKEN=SEU_TOKEN_DO_DISCORD

TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+55SEUNUMERO
```

## ▶️ Executando o projeto
```bash
//Teste do WhatsApp (isolado)
python teste_whatsapp.py

//Executar o bot
python bot/bot.py
```

## Depois disso:

envie uma mensagem no Discord contendo uma palavra-chave
o alerta será enviado para o WhatsApp

### 🚧 Limitações atuais

Uso do WhatsApp Sandbox do Twilio (ambiente de testes)
Regras de decisão baseadas em palavras-chave
Sem interface gráfica (controle via código)
Essas limitações são intencionais para manter o projeto simples e focado na integração.


### 👩‍💻 Autora

Maria Julia Siqueira Felix
Estudante de Desenvolvimento de Sistemas | Informática
Interesse em Backend, Front-end e Inteligência Artificial
