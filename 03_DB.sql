-- database
create database bai_development;

-- mysql database 를 사용
USE mysql;

-- 사용자 확인
SELECT HOST, USER, PASSWORD FROM USER;

-- 사용자 계정 생성 'id'@'localhost' 이면 로컬에서만 접속 가능
CREATE USER '아이디'@'%' IDENTIFIED BY '비밀번호';
CREATE USER 'board'@'%' IDENTIFIED BY 'board';
CREATE USER 'test'@'%' IDENTIFIED BY 'test';
CREATE USER 'bai_development'@'%' IDENTIFIED BY 'duawlsrud#5194';


-- 사용자 권한 주기
GRANT ALL PRIVILEGES ON 데이터베이스.* TO '아이디'@'%';
GRANT ALL PRIVILEGES ON board.* TO 'board'@'%';
GRANT ALL PRIVILEGES ON test.* TO 'test'@'%';
GRANT ALL PRIVILEGES ON bai_development.* TO 'bai_development'@'%';


-- 새로고침
FLUSH PRIVILEGES;



