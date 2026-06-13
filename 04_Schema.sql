CREATE TABLE Persons (
    Personid int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (Personid)
);

CREATE TABLE bai_development.board (
    id int NOT NULL AUTO_INCREMENT,
    title varchar(45) NOT NULL,
    content text,
    PRIMARY KEY (id)
);


