CREATE DATABASE lucasf1_bdd2;

USE lucasf1_bdd2;

CREATE TABLE pessoas(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    nascimento VARCHAR(255) NOT NULL
);