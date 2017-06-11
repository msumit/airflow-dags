"""
This is only an example DAG to highlight usage of [QuboleOperator](http://docs.qubole.com/en/latest/user-guide/airflow/qubole-operator-api.html) in various 
scenarios, some of these tasks may or may not work based on your QDS account setup.

Run a shell command from Qubole Analyze against your Airflow cluster with following to
trigger it manually `airflow trigger_dag example_qubole_operator`.


*Note: Make sure that connection `qubole_default` is properly set before running this example. 
Please be aware that it might spin up clusters to run these examples.*
"""

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.qubole_operator import QuboleOperator

seven_days_ago = datetime.combine(datetime.today() - timedelta(1),
                                  datetime.min.time())

default_args = {
    'owner': 'sumit',
    'start_date': datetime(2017,1,15,00,30,00),
    'depends_on_past': False 
}

dag = DAG('depends_on_past4', default_args=default_args, schedule_interval=None)

dag.doc_md = __doc__

t2 = QuboleOperator(
    task_id='spark_cmd',
    command_type="sparkcmd",
    note_id="36995",
    qubole_conn_id='qubole_prod',
    arguments='{"name":"hello world"}',
    dag=dag)

t1 = BashOperator(
    task_id='task_1',
    bash_command='echo 1',
    dag=dag)
