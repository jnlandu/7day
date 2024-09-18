# Configurations
# source .venv/bin/activate

export AIRFLOW_HOME=${PWD}/airflow
# AIRFLOW_VERSION=2.3.3
# PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# # Install Airflow (may need to upgrade pip)
# pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# Initialize DB (SQLite by default)
# airflow db init

# Make sure AIRFLOW_HOME is exported as variable in the terminal you use
# Inside airflow.cfg set load_examples=False and run airflow db reset -y

AIRFLOW_VERSION=2.10.1
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
# For example: 3.8
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-no-providers-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.10.1/constraints-no-providers-3.8.txt
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"