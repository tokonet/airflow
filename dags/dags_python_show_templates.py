
import datetime
import pendulum

from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id = "dags_python_show_templates",
    schedule = "30 9 * * 1",
    start_date = pendulum.datetime(2024, 7, 1, tz="Asia/Seoul"),
    catchup = True,   # False : 시작일자(2024.07.01)의 누락된 구간을 돌리지 않는다. True인 경우 전체를 돌린다.
) as dag:

    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)
    
    show_templates()

