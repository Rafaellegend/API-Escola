# API-Escola
[![Python Version](https://img.shields.io/badge/3.13-Python-brightgreen?logo=python&logoColor=white&color=%233776AB)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/5.2-Django-brightgreen?logo=django&logoColor=white&color=%23092E20)](https://www.djangoproject.com/download/)

Esse projéto faz parte da aula de Django REST Framework da plataforma [Alura](https://www.alura.com.br)

## 💻Pré-Requisitos
Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou:
    - [Python 3.13](https://www.python.org/downloads/)
    - [Django 5.2](https://www.djangoproject.com/download/)
    - [Django REST framework](https://www.django-rest-framework.org/#installation)

> Versões Inferiores ou Superiores não testados

## ☕Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/Rafaellegend/API-Escola
```

Entre no diretório do projeto

```bash
  cd API-Escola
```

Crie o ambiente Virtual
```bash
  python -m venv ./venv
```

Inicie o ambiente virtual
- Windows
    ```bash
      venv/Scripts/activate
    ```
- Linux
    ```bash
      source venv/Scripts/activate.fish
    ```

- Mac
    ```bash
      source venv/Scripts/activate.fish
    ```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Realize as Migrações

```bash
  python manage.py makemigrations
```

```bash
  python manage.py migrate
```

Inicie o servidor

```bash
  python manage.py runserver 
```


## 📫Documentação da API
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

#### Retorna lista de estudantes

```http
  GET estudantes/
```

#### Retorna um estudante em específico

```http
  GET estudantes/${id}
```

#### Retorna lista de cursos

```http
  GET cursos/
```

#### Retorna um curso em específico

```http
  GET cursos/${id}
```

#### Retorna lista de matriculas

```http
  GET matriculas/
```

#### Retorna um matriculas em específico

```http
  GET matriculas/${id}
```

#### Retorna as matriculas de um estudante em específico

```http
  GET estudantes/${id}/matriculas
```

#### Retorna as matriculas de um curso em específico

```http
  GET cursos/${id}/matriculas
```

## 👨‍💻Autores
<table>
    <tr>
        <td align='center'>
            <a href='https://github.com/Rafaellegend'>
                <img src="https://avatars.githubusercontent.com/u/39443512?s=400&u=f816ce76f9d3f3a90aaab97ea80b27f283402ff3&v=4" alt="Rafaellegend Profile Picture"width="100">
                <p>Rafaellegend</p>
            </a>
        </td>
    </tr>
</table>

