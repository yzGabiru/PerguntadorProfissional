# 🧠 Perguntador Profissional

**Gere automaticamente perguntas de entrevista com base em currículos em PDF usando inteligência artificial!**

Este projeto extrai o texto de um currículo em PDF, envia o conteúdo para a API da Cohere, e gera perguntas de entrevista relevantes para ajudar candidatos a se prepararem melhor.

---

## 🚀 Funcionalidades

- 📄 Leitura de currículos em PDF
- 🤖 Geração de perguntas com uma LLM (Cohere)
- 📝 Exportação das perguntas para um arquivo `.csv`
- ⚡ Ideal para recrutadores ou candidatos que desejam treinar para entrevistas

---

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Cohere API](https://cohere.com/)
- [pdfplumber](https://pypi.org/project/pdfplumber/)
- [csv (built-in)](https://docs.python.org/3/library/csv.html)

---

## 📦 Como usar

1. **Clone este repositório**

    ```bash
    git clone https://github.com/yzGabiru/PerguntadorProfissional.git

2. **Navegue até a pasta do projeto**

    ```bash
    cd PerguntadorProfissional

3. **Instale as dependências**
    ```bash
    pip install cohere pdfplumber

4. **Edite o nome do currículo PDF no código**
    ```bash
    with pdfplumber.open("Seu currículo aqui.pdf") as pdf:
    for page in pdf.pages:
        texto_curriculo += page.extract_text()

5. **Mude a chave da API cohere para a sua gerada no site**

    ```bash
    co = cohere.ClientV2(api_key="Sua API aqui!")

5. **Execute o programa**
