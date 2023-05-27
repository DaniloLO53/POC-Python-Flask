CREATE TABLE
IF NOT EXISTS students
(
  matricula INTEGER,
  nome VARCHAR
(255) NOT NULL,
  sobrenome VARCHAR
(255) NOT NULL,
  email VARCHAR
(255) NOT NULL,
  telefone VARCHAR
(20) NOT NULL,
  curso VARCHAR
(255) NOT NULL,
  nascimento DATE NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT
CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL
);

INSERT INTO students
  (matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)
SELECT 1001, 'João', 'Silva', 'joao.silva@example.com', '2165456545', 'Engenharia Mecânica', '1995-07-15', CURRENT_TIMESTAMP
WHERE NOT EXISTS (SELECT 1
FROM students
WHERE matricula = 1001)
LIMIT 1;

INSERT INTO students
  (matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)
SELECT 1002, 'Maria', 'Santos', 'maria.santos@example.com', '2195765456', 'Administração', '1994-09-20', CURRENT_TIMESTAMP
WHERE NOT EXISTS (SELECT 1
FROM students
WHERE matricula = 1002)
LIMIT 1;

INSERT INTO students
  (matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)
SELECT 1003, 'Pedro', 'Ferreira Alberto', 'pedro.ferreira@example.com', '2233654568', 'Medicina', '1996-02-10', CURRENT_TIMESTAMP
WHERE NOT EXISTS (SELECT 1
FROM students
WHERE matricula = 1003)
LIMIT 1;

INSERT INTO students
  (matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)
SELECT 1004, 'Rafael', 'Alves da Cunha', 'rafael.alves@example.com', '21634789745', 'Medicina', '1996-02-10', CURRENT_TIMESTAMP
WHERE NOT EXISTS (SELECT 1
FROM students
WHERE matricula = 1004)
LIMIT 1;

INSERT INTO students
  (matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)
SELECT 1005, 'Carlos', 'da Silva Pinto', 'carlos.silva@example.com', '21995487897', 'Artes Visuais', '1992-06-10', CURRENT_TIMESTAMP
WHERE NOT EXISTS (SELECT 1
FROM students
WHERE matricula = 1005)
LIMIT 1;

INSERT INTO students
  (matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)
SELECT 1006, 'Andressa', 'Moraes da Cunha', 'andressa.moraes@example.com', '1145678479', 'Engenharia Mecânica', '1991-02-12', CURRENT_TIMESTAMP
WHERE NOT EXISTS (SELECT 1
FROM students
WHERE matricula = 1006)
LIMIT 1;

INSERT INTO students
  (matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)
SELECT 1007, 'José', 'Pereira de Oliveira', 'jose.pereira@example.com', '2145612345', 'Engenharia Naval', '1995-11-10', CURRENT_TIMESTAMP
WHERE NOT EXISTS (SELECT 1
FROM students
WHERE matricula = 1007)
LIMIT 1;

INSERT INTO students
  (matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)
SELECT 1008, 'Bernardo', 'Silva Souto', 'bernardo.silva@example.com', '11997845678', 'Música', '1996-03-10', CURRENT_TIMESTAMP
WHERE NOT EXISTS (SELECT 1
FROM students
WHERE matricula = 1008)
LIMIT 1;

INSERT INTO students
  (matricula, nome, sobrenome, email, telefone, curso, nascimento, updated_at)
SELECT 1009, 'Letícia', 'Drummound Lopes', 'leticia.lopes@example.com', '2154564563', 'Música', '1997-05-05', CURRENT_TIMESTAMP
WHERE NOT EXISTS (SELECT 1
FROM students
WHERE matricula = 1009)
LIMIT 1;