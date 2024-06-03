
import pendulum
import datetime

from airflow.models.dag import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_conn_test",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,   # False : 시작일자(2021.01.01)의 누락된 구간을 돌리지 않는다. True인 경우 전체를 돌린다.
#    dagrun_timeout=datetime.timedelta(minutes=60),
#    tags=["example", "example2"],
#    params={"example_key": "example_value"},
) as dag:
    t1 = EmptyOperator(
        task_id="t1",
    )

    t2 = EmptyOperator(
        task_id="t2",
    )

    t3 = EmptyOperator(
        task_id="t3",
    )

    t4 = EmptyOperator(
        task_id="t4",
    )

    t5 = EmptyOperator(
        task_id="t5",
    )

    t6 = EmptyOperator(
        task_id="t6",
    )

    t7 = EmptyOperator(
        task_id="t7",
    )

    t8 = EmptyOperator(
        task_id="t8",
    )

t1 >> [t2,t3] >> t4
t5 >> t4
[t4,t7] >> t6 >> t8
