
import pendulum

from airflow import DAG
from operators.seoul_api_to_csv_operator import SeoulApiToCsvOperator

with DAG(
    dag_id = 'dags_seoul_api_corona',
    schedule = '0 7 * * *',
    start_date = pendulum.datetime(2024, 7, 1, tz='Asia/Seoul'),
    catchup = False
) as dag:

    '''서울시 코로나19 확진자 발생동향'''
    # https://data.seoul.go.kr/dataList/OA-20461/S/1/datasetView.do
    # 서울시 코로나19 확진자(전수감시) 발생동향 (2023.08.31.이전)

    tb_corona19_count_status = SeoulApiToCsvOperator(
        task_id = 'tb_corona19_count_status',
        dataset_nm = 'TbCorona19CountStatus',
        path = '/opt/airflow/file/TbCorona19CountStatus/{{data_interval_end.in_timezone("Asia/Seoul") | ds_nodash }}',
        file_name = 'TbCorona19CountStatus.csv'
    )

    '''서울시 코로나19 백신 예방접종 현황'''
    # https://data.seoul.go.kr/dataList/OA-20914/S/1/datasetView.do
    # 서울시 코로나19 백신 예방접종 현황 (2023.08.31.이전)
    tv_corona19_vaccine_stat_new = SeoulApiToCsvOperator(
        task_id = 'tv_corona19_vaccine_stat_new',
        dataset_nm = 'tvCorona19VaccinestatNew',
        path = '/opt/airflow/file/tvCorona19VaccinestatNew/{{data_interval_end.in_timezone("Asia/Seoul") | ds_nodash }}',
        file_name = 'tvCorona19VaccinestatNew.csv'
    )

    tb_corona19_count_status >> tv_corona19_vaccine_stat_new
