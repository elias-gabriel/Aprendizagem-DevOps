create schema joins;
use joins;
create table autor
(
ID_autor int(3) AUTO_INCREMENT PRIMARY KEY, 
Nome_autor varchar(30)
);

create table livro 
(
ID_livro int(3) PRIMARY KEY, 
Nome_livro varchar(30), 
FK_A int NULL, FOREIGN KEY (FK_A) REFERENCES autor(ID_autor)
);

alter table livro AUTO_INCREMENT = 50;

insert into autor(ID_autor, Nome_autor) VALUES
(1, 'Paola Joséfina'),
(2, 'Reinaldo'), 
(3, 'Felipe Agnaldo'),
(4, 'Antonia '), 
(5, 'João');

insert into livro(ID_livro, Nome_livro, FK_A) VALUES(50, 'Algoritimos', 5);
insert into livro(ID_livro, Nome_livro, FK_A) VALUES(51, 'BDs', 1);
insert into livro(ID_livro, Nome_livro, FK_A) VALUES(52, 'Python', 3);
insert into livro(ID_livro, Nome_livro, FK_A) VALUES(53, 'C#', null);
insert into livro(ID_livro, Nome_livro, FK_A) VALUES(54, 'Java', 2);



/*INNER JOIN*/
use joins;
select Nome_autor, Nome_livro from autor inner join livro on autor.ID_Autor = livro.FK_A;



/*Left Join*/
use joins;
select Nome_autor, Nome_livro from autor left join livro on autor.ID_Autor = livro.FK_A;
												
                                                /* OU*/
use joins;
select Nome_autor, Nome_livro from livro left join autor on autor.ID_Autor = livro.FK_A;


/* Right Join*/
use joins;
select Nome_autor, Nome_livro from autor right join livro on autor.ID_Autor = livro.FK_A;
													
                                                    /* OU*/
use joins;
select Nome_autor, Nome_livro from livro right join autor on autor.ID_Autor = livro.FK_A;



/* Full Join*/
use joins;
select Nome_autor, Nome_livro from autor left join livro on autor.ID_Autor = livro.FK_A
union
select Nome_autor, Nome_livro from autor right join livro on autor.ID_Autor = livro.FK_A;

                                                    /* OU */
use joins;
select Nome_autor, Nome_livro from autor full join livro on autor.ID_Autor = livro.FK_A;
