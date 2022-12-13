CREATE USER postgres WITH PASSWORD 'postgres';
CREATE DATABASE IF NOT EXISTS postgres_db;
GRANT ALL PRIVILEGES ON DATABASE "postgres_db" to postgres;

CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL,
  email varchar(250) NOT NULL UNIQUE,
  password varchar(250) NOT NULL
);

INSERT INTO users(name, email, password) VALUES
('christian dalena', 'christian@gmail.com', 'super_secret'),
('mario rossi', 'mario@live.it', 'super_secret'),
('franco verdi', 'franco@live.it', 'super_secret'),
('alessandro neri', 'alessandro@libero.com', 'super_secret'),
('mario bianchi', 'mario@outlook.it', 'super_secret');