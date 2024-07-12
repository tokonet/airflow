
import pendulum
import datetime
import random

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id = "dags_python_operator",
    schedule = "30 6 * * *",
    start_date = pendulum.datetime(2024, 7, 1, tz="Asia/Seoul"),
    catchup = False,   # False : 시작일자(2021.01.01)의 누락된 구간을 돌리지 않는다. True인 경우 전체를 돌린다.
#    dagrun_timeout = datetime.timedelta(minutes=60),
#    tags = ["example", "example2"],
#    params = {"example_key": "example_value"},
) as dag:
    def select_fruit():
        fruit = ['APPLE','BANANA','ORANGE','AVOCADO']
        rand_int = random.randint(0,3)
        print(fruit[rand_int])

    py_t1 = PythonOperator(
        task_id = "py_t1",
        python_callable = select_fruit
    )

py_t1
