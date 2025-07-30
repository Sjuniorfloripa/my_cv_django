![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/Licença-MIT-blue)

# 🧑‍💻 Currículo Online com Django

Este projeto é um **currículo digital interativo** desenvolvido com Django, que permite manter as informações profissionais sempre atualizadas através do painel administrativo (Django Admin). A aplicação exibe os dados em uma página única (One Page) com layout responsivo, modo escuro automático e um botão que gera um **PDF dinâmico** da própria página — sempre refletindo as informações mais recentes.

---

## ✨ Funcionalidades

- ✅ Interface limpa e responsiva (Bootstrap 5)
- 🌗 Modo escuro automático baseado na preferência do sistema
- 🔍 Exibição de dados por categorias: experiências, formação, habilidades, projetos e idiomas
- 🧠 Dados centralizados e gerenciáveis via Django Admin
- 📥 Geração de PDF com um clique (via html2pdf.js)
- 🧼 Cabeçalho, rodapé e botões são ignorados na versão PDF para manter o foco no conteúdo

---

## 🛠️ Tecnologias utilizadas

- Django 5.x
- Python 3.12
- HTML5 + CSS3
- Bootstrap 5
- JavaScript (`html2pdf.js`)

---

## 🚀 Como usar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# 2. Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode as migrações
python manage.py migrate

# 5. Crie um superusuário
python manage.py createsuperuser

# 6. Rode o servidor
python manage.py runserver
```

Acesse http://localhost:8000 para visualizar o currículo.

---
## 🧪 Observações
* O PDF é gerado com base no conteúdo atual da página, refletindo sempre os dados mais recentes.
* Ideal para portfólio pessoal, profissionais freelancers ou desenvolvedores que desejam ter um currículo dinâmico e visual.
* Cabeçalhos, rodapés e botões são ocultados automaticamente na versão PDF com regras de @media print.

---
## 💻 Demonstração
<img width="1440" height="2884" alt="screencapture-my_cv_django" src="https://github.com/user-attachments/assets/318696e2-b6e8-41b6-9ced-5cecdc095032" />

---

## 📫 Contato

| Tipo      | Informação |
|-----------|------------|
| 📧 Email  | [contato@silvanodiasjr.com.br](mailto:contato@silvanodiasjr.com.br) |
| 🔗 LinkedIn | [linkedin.com/in/silvano-charão-dias-junior-99766216a](https://www.linkedin.com/in/silvano-char%C3%A3o-dias-junior-99766216a/) |
| 🐙 GitHub | [@Sjuniorfloripa](https://github.com/Sjuniorfloripa) |
