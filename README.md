<h1>POC - FLASK</h1>

<h2>Descrição</h2>
<p>CRUD em uma tabela de estudantes de uma faculdade utilizando <strong>SQLite3</strong> e <strong>Flask</strong>.</p>

<h2>Funcionamento</h2>
<div>
  <ul>
    <li>
      <h3>GET /students</h3>
      <span><strong>Payload:</strong> Nenhum</span>
      <br>
      <span><strong>Resposta:</strong> JSON com todos os estudantes</span>
      <br>
      <details>
        <summary>
        Exemplo:
        </summary>
        <pre>
          [
            {
              "curso": "Engenharia Mecânica",
              "email": "joao.silva@example.com",
              "matricula": 1001,
              "nascimento": "1995-07-15",
              "nome": "João",
              "sobrenome": "Silva",
              "telefone": "2165456545"
            },
            {
              "curso": "Administração",
              "email": "maria.santos@example.com",
              "matricula": 1002,
              "nascimento": "1994-09-20",
              "nome": "Maria",
              "sobrenome": "Santos",
              "telefone": "2195765456"
            },
            {
              "curso": "Medicina",
              "email": "pedro.ferreira@example.com",
              "matricula": 1003,
              "nascimento": "1996-02-10",
              "nome": "Pedro",
              "sobrenome": "Ferreira Alberto",
              "telefone": "2233654568"
            },
            {
              "curso": "Medicina",
              "email": "rafael.alves@example.com",
              "matricula": 1004,
              "nascimento": "1996-02-10",
              "nome": "Rafael",
              "sobrenome": "Alves da Cunha",
              "telefone": "21634789745"
            },
            {
              "curso": "Artes Visuais",
              "email": "carlos.silva@example.com",
              "matricula": 1005,
              "nascimento": "1992-06-10",
              "nome": "Carlos",
              "sobrenome": "da Silva Pinto",
              "telefone": "21995487897"
            },
            {
              "curso": "Engenharia Mecânica",
              "email": "andressa.moraes@example.com",
              "matricula": 1006,
              "nascimento": "1991-02-12",
              "nome": "Andressa",
              "sobrenome": "Moraes da Cunha",
              "telefone": "1145678479"
            },
            {
              "curso": "Engenharia Naval",
              "email": "jose.pereira@example.com",
              "matricula": 1007,
              "nascimento": "1995-11-10",
              "nome": "José",
              "sobrenome": "Pereira de Oliveira",
              "telefone": "2145612345"
            },
            {
              "curso": "Música",
              "email": "bernardo.silva@example.com",
              "matricula": 1008,
              "nascimento": "1996-03-10",
              "nome": "Bernardo",
              "sobrenome": "Silva Souto",
              "telefone": "11997845678"
            },
            {
              "curso": "Música",
              "email": "leticia.lopes@example.com",
              "matricula": 1009,
              "nascimento": "1997-05-05",
              "nome": "Letícia",
              "sobrenome": "Drummound Lopes",
              "telefone": "2154564563"
            }
          ]
        </pre>
      </details>
      <br>
    </li>
    <li>
      <h3>GET /students/1001</h3>
      <span><strong>Payload:</strong> Nenhum</span>
      <br>
      <span><strong>Resposta:</strong> JSON com dados do estudante</span>
      <br>
      <details>
        <summary>
        Exemplo:
        </summary>
        <pre>
            {
              "curso": "Engenharia Mecânica",
              "email": "joao.silva@example.com",
              "matricula": 1001,
              "nascimento": "1995-07-15",
              "nome": "João",
              "sobrenome": "Silva",
              "telefone": "2165456545"
            }
        </pre>
      </details>
      <br>
    </li>
    <li>
      <h3>POST /students</h3>
      <span><strong>Payload:</strong> JSON com dados do estudante</span>
      <br>
      <span><strong>Resposta:</strong> JSON com dados do estudante</span>
      <br>
      <details>
        <summary>
        Exemplo:
        </summary>
        <span>Payload e retorno:</span>
        <pre>
            {
              "curso": "Engenharia Mecânica",
              "email": "joao.silva@example.com",
              "matricula": 1001,
              "nascimento": "1995-07-15",
              "nome": "João",
              "sobrenome": "Silva",
              "telefone": "2165456545"
            }
        </pre>
      </details>
      <br>
    </li>
    <li>
      <h3>PUT /students/1001</h3>
      <span><strong>Payload:</strong> JSON com dados do estudante</span>
      <br>
      <span><strong>Resposta:</strong> JSON com dados atualizados do estudante</span>
      <br>
      <details>
        <summary>
        Exemplo:
        </summary>
        <span>Payload e retorno:</span>
        <pre>
            {
              "curso": "Engenharia de Computação",
              "email": "joao.silva@example.com",
              "matricula": 1001,
              "nascimento": "1995-07-15",
              "nome": "João",
              "sobrenome": "Silva",
              "telefone": "2165456545"
            }
        </pre>
      </details>
      <br>
    </li>
    <li>
      <h3>DELETE /students/1001</h3>
      <span><strong>Payload:</strong> Nenhum</span>
      <br>
      <span><strong>Resposta:</strong> JSON com dados do estudante removido</span>
      <br>
      <details>
        <summary>
        Exemplo:
        </summary>
        <span>Retorno:</span>
        <pre>
            {
              "curso": "Engenharia Mecânica",
              "email": "joao.silva@example.com",
              "matricula": 1001,
              "nascimento": "1995-07-15",
              "nome": "João",
              "sobrenome": "Silva",
              "telefone": "2165456545"
            }
        </pre>
      </details>
      <br>
    </li>
  </ul>
  
</div>

<h2>Para rodar o projeto</h2>
<ol>
  <li>Abra o terminal na raíz do projeto</li>
  <li>Crie um ambiente virtual .venv <br> <code>python3 -m venv .venv</code></li>
  <li>Ative o ambiente virtual <br> <code>source .venv/bin/activate</code></li>
  <li>Instale as dependências necessárias <br> <code>pip install -r requirements.txt </code></li>
  <li>Inicie a aplicação <br> <code>flask --app run run</code></li>
</ol>
