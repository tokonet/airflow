
import pendulum
import datetime

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
    dag_id = "dags_python_with_op_kwargs",
    schedule = "30 6 * * *",
    start_date = pendulum.datetime(2024, 7, 1, tz="Asia/Seoul"),
    catchup = False,   # False : 시작일자(2021.01.01)의 누락된 구간을 돌리지 않는다. True인 경우 전체를 돌린다.
#    dagrun_timeout = datetime.timedelta(minutes=60),
#    tags = ["example", "example2"],
#    params = {"example_key": "example_value"},
) as dag:

    regist2_t1 = PythonOperator(
        task_id = "regist2_t1",
        python_callable = regist2,
        op_args = ['tokonet','man','kr','seoul'],
        op_kwargs = {'email':'tokonet@naver.com','phone':'010'}
    )

regist2_t1
