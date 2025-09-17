# 📬 Listar Pastas de E-mail com Microsoft Graph API

Este projeto em Python permite autenticar via Microsoft Graph API usando o fluxo de credenciais de cliente (Client Credentials Flow) e listar as pastas de e-mail de uma conta específica do Microsoft 365.

## 🚀 Funcionalidades

- Autenticação OAuth 2.0 com Azure AD
- Obtenção de token de acesso
- Consulta às pastas de e-mail de um usuário via Microsoft Graph

## 🚀 Variáveis

**Edite o arquivo principal com suas credenciais:**

- tenant_id = "SEU_TENANT_ID"
- client_id = "SEU_CLIENT_ID"
- client_secret = "SEU_CLIENT_SECRET"
- email = "email@dominio.com"

## 📂 Exemplo de pastas Encontradas

Lista de pastas de e-mail retornadas pela API:

- **Nome:** Caixa de Entrada  
  **ID:** AAMk...

- **Nome:** Itens Enviados  
  **ID:** AAMk...

- **Nome:** ...  
  **ID:** AAMk...


## 🧰 Requisitos

- Python 3.7+
- Conta Microsoft 365 com permissões de leitura de e-mail
- Aplicativo registrado no [Azure Portal](https://portal.azure.com)
- Permissões de API: `Mail.Read` (Application)

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Arii19/mapear_pastas_microsoft_graph.git
   cd listar-pastas-email
