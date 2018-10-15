# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, BLOB, DateTime, PickleType, Index, desc, create_engine, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from airflow import configuration as conf
import subprocess 
import shlex

Base = declarative_base()
SQL_ALCHEMY_CONN = conf.get('core', 'SQL_ALCHEMY_CONN')

class DagRun(Base):
    __tablename__ = 'dag_run'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dag_id = Column(String(250))
    execution_date = Column(DateTime)
    state = Column(String(50))
    run_id = Column(String(250))
    external_trigger = Column(Integer)
    conf = Column(PickleType)
    end_date = Column(DateTime)
    start_date = Column(DateTime)

    def __repr__(self):
        return "<DagRun(dag_id='%s', execution_date='%s', state='%s', run_id='%s')>" % (
            self.dag_id, self.execution_date, self.state, self.run_id)

def main():
    engine = create_engine(SQL_ALCHEMY_CONN, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    nowdatetime = datetime.today()
    run_id = f'trig_run_id_{nowdatetime}'

    ele_desc = {}

    payload = {'element': ele_desc}

    dag_id = 'dag_id'
    task_id = 'task_id'
    dag_file_path = '/root/airflow/dags/dag_file_path.py'
    
    dag_run = DagRun(dag_id=dag_id, execution_date=nowdatetime, state='running', run_id=run_id, external_trigger=0, start_date=nowdatetime, 
        conf=payload)
    session.add(dag_run)

    session.commit()

    cmd = f'airflow run {dag_id} {task_id} {nowdatetime.isoformat()} --local --raw -sd {dag_file_path}'
    print(cmd)
    args = shlex.split(cmd)
    child = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while child.poll() is None:
        oneline = child.stderr.readline()
        oneline = oneline.decode('utf-8').replace('\n', '')
        assert not 'Traceback' in oneline, f'airflow subprocess exception'

    assert child.returncode == 0, 'airflow run return code is not 0 and error in it'
    pass

if __name__ == '__main__':
    main()