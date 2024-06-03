
import pendulum
import datetime

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,   # False : 시작일자(2021.01.01)의 누락된 구간을 돌리지 않는다. True인 경우 전체를 돌린다.
#    dagrun_timeout=datetime.timedelta(minutes=60),
#    tags=["example", "example2"],
#    params={"example_key": "example_value"},
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

bash_t1 >> bash_t2
