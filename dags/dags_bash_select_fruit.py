
import pendulum
import datetime

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_select_fruit",
    schedule = "10 0 * * 6#1",
    start_date = pendulum.datetime(2024, 7, 1, tz="Asia/Seoul"),
    catchup = False,   # False : 시작일자(2021.01.01)의 누락된 구간을 돌리지 않는다. True인 경우 전체를 돌린다.
#    dagrun_timeout = datetime.timedelta(minutes=60),
#    tags = ["example", "example2"],
#    params = {"example_key": "example_value"},
) as dag:

    t1_orange = BashOperator(
        task_id = "t1_orange",
        bash_command = "/opt/airflow/plugins/shell/select_fruit.sh ORANGE",
    )

    t2_avocado = BashOperator(
        task_id = "t2_avocado",
        bash_command = "/opt/airflow/plugins/shell/select_fruit.sh AVOCADO",
  )

t1_orange >> t2_avocado
