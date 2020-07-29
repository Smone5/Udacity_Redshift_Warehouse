# Bash file to execute all scripts for creating Redshift database

python 1_create_redshift.py
python 2_create_tables.py
python 3_etl.py
python 4_qa_check.py
