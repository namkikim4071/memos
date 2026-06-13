# toby

# jenn

# zet
p4 주석설명이 어려움
p35 ERD 넣기
p45 수렴속도의 개선에 대한 개념 궁금
p53
p59 아쉽
p68 Lift 차트 설명?? 추가??
p72
p155 내용이 어려움
p157

인코딩 학습 ==> 인코더 학습
데이터 셋 ==> 데이터셋




# 추가 오류 확인
airflow db upgrade
==>
table _alembic_tmp_ab_user already exists
==>
rm ~/airflow/airflow.db

==>
airflow webserver --port 8080 : 이상없음.

==>
airflow webserver --port 8080 -D
==> airflow 가상환경이 겹치면, 문제가 발생한다. => 다른 가상환경을 모두 삭제하고 실행한다.



mkdir -p ~/airflow/dags
ln -snf ~/Dev/mlops-study-ml-pipeline/features ~/airflow/dags/features
ln -snf ~/Dev/mlops-study-ml-pipeline/models ~/airflow/dags/models
ln -snf ~/Dev/mlops-study-ml-pipeline/support ~/airflow/dags/support
ls -al ~/airflow/dags



##
no such column: dag.dag_display_name ==> 잘못된 버전 설치..

pip install mysqlclient mysql-connector-python ==> 버전 고정안하기!!
==> pip install mysqlclient==2.2.0 mysql-connector-python==8.1.0 ==> 오류발생

mysql-connector-python==8.1.0
mysqlclient==2.2.0

pip install apache-airflow-providers-mysql
==> pip install apache-airflow-providers-mysql==5.4.0




airflow db upgrade

