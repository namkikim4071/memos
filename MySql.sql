mysql -u root -p

show databases;

create database bai;

create database bai_development;

CREATE USER 'bai_development'@'%' IDENTIFIED BY 'bai_development';


SELECT user, host, plugin FROM user;

msyql > create schema DB명 default character set utf8; -- 둘중에 하나를 입력하면 DB 생성됨

mysql > create database bai_development default character set utf8;

msyql > drop database bai;       // 데이터베이스 삭제

msyql > drop database bai_development;       // 데이터베이스 삭제

mysql > GRANT ALL PRIVILEGES ON DB명.테이블 TO 계정아이디@host IDENTIFIED BY '비밀번호';

--// 계정이 이미 존재 하는데 'identified by '비밀번호' 부분을 추가하면 비밀번호가 변경된다
mysql> GRANT ALL privileges ON DB명.* TO 계정아이디@locahost IDENTIFIED BY '비밀번호';
mysql> GRANT ALL privileges ON DB명.* TO 계정아이디@'%' IDENTIFIED BY '비밀번호';

GRANT ALL privileges ON bai_development.* TO bai_development@'%'

FLUSH PRIVILEGES;


create table bai_development.tmp_table as
select '1' as id
      ,'한글테스트' as content
from dual;



mysql -h localhost -P 3306 -uroot -p


Database



create user ‘user명’@’%’ identified by ‘패스워드’
create user ‘bai_development’@’%’ identified by ‘bai_development’;
create user bai@’%’ identified by ‘skarl@5194’






select user, host from user;


