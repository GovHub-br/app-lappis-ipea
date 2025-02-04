from typing import Dict, Any, Optional

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import logging
import json
from ...plugins.cliente_email import fetch_and_process_emails
from ...plugins.cliente_postgres import ClientPostgresDB
from ...helpers.postgres_helpers import get_postgres_conn

# Configurações básicas da DAG
default_args = {
    "owner": "Davi",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

COLUMN_MAPPING = {
    0: "ne_ccor",
    1: "ne_informacao_complementar",
    2: "ne_num_processo",
    3: "ne_ccor_descricao",
    4: "doc_observacao",
    5: "natureza_despesa",
    6: "natureza_despesa_1",
    7: "natureza_despesa_detalhada",
    8: "natureza_despesa_detalhada_1",
    9: "ne_ccor_favorecido",
    10: "ne_ccor_favorecido_1",
    11: "ne_ccor_ano_emissao",
    12: "item_informacao",
    13: "despesas_empenhadas_controle_empenho_saldo_moeda_origem",
    14: "despesas_empenhadas_controle_empenho_movim_liquido_moeda_origem",
    15: "despesas_liquidadas_controle_empenho_saldo_moeda_origem",
    16: "despesas_liquidadas_controle_empenho_movim_liquido_moeda_origem",
    17: "despesas_pagas_controle_empenho_saldo_moeda_origem",
    18: "despesas_pagas_controle_empenho_movim_liquido_moeda_origem",
}

EMAIL_SUBJECT = "consulta_por_execucao_emp_liq_pago"


# Configurações da DAG
with DAG(
    dag_id="email_empenhos_tesouro_ingest",
    default_args=default_args,
    description="Processa anexos dos empenhos vindo do email, formata e insere no db",
    schedule_interval="0 13 * * 1-6",
    start_date=datetime(2023, 12, 1),
    catchup=False,
) as dag:

    def process_email_data(**context: Dict[str, Any]) -> Optional[str]:
        creds = json.loads(Variable.get("email_credentials"))

        EMAIL = creds["email"]
        PASSWORD = creds["password"]
        IMAP_SERVER = creds["imap_server"]
        SENDER_EMAIL = creds["sender_email"]

        try:
            logging.info("Iniciando o processamento dos emails...")
            csv_data = fetch_and_process_emails(
                EMAIL,
                PASSWORD,
                IMAP_SERVER,
                SENDER_EMAIL,
                EMAIL_SUBJECT,
                COLUMN_MAPPING,
            )
            if not csv_data:
                logging.warning("Nenhum e-mail encontrado com o assunto esperado.")
                return None

            logging.info(
                "CSV processado com sucesso. Dados encontrados: %s", len(csv_data)
            )
            return csv_data
        except Exception as e:
            logging.error("Erro no processamento dos emails: %s", str(e))
            raise

    def insert_data_to_db(**context: Dict[str, Any]) -> None:
        """
        Função para inserir os dados no banco de dados.
        Os dados do CSV são recuperados do XCom.
        """
        try:
            task_instance: Any = context["ti"]
            csv_data: Any = task_instance.xcom_pull(task_ids="process_emails")

            if not csv_data:
                logging.warning("Nenhum dado para inserir no banco.")
                return

            postgres_conn_str = get_postgres_conn()
            db = ClientPostgresDB(postgres_conn_str)

            db.insert_csv_data(csv_data, "empenhos_tesouro", schema="siafi")
            logging.info("Dados inseridos com sucesso no banco de dados.")
        except Exception as e:
            logging.error("Erro ao inserir dados no banco: %s", str(e))
            raise

    # Tarefa 1: Processar os e-mails e retornar CSV
    process_emails_task = PythonOperator(
        task_id="process_emails",
        python_callable=process_email_data,
        provide_context=True,
    )

    # Tarefa 2: Inserir os dados no banco de dados
    insert_to_db_task = PythonOperator(
        task_id="insert_to_db",
        python_callable=insert_data_to_db,
        provide_context=True,
    )

    # Fluxo da DAG
    process_emails_task >> insert_to_db_task
