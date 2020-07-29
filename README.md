# Project Data Warehouse


## Summary of Project
A data warehouse using a star schema built in Amazon Redshift. An ETL pipeline is used to create the data warehouse for a fictional Sparkify analytic team.

## How to Run Python Scripts
1. If Python libraries not installed already, in terminal run
        pip install -r requirements.txt
2. The first time you run the ETL, you need generate an Identity Access Management (IAM) user in Amazon Web Services (AWS). Save the key and secret to use in the configuration file *dwh.cfg*. The user should have the following policies:
    + AmazonRedshiftReadOnlyAccess
    + AdministratorAccess
and (AWS) administration privileges. 
**IMPORTANT NOTE:** When done creating the Redshift cluster it would be wise to remove the IAM secret from your dwh.cfg configuration file. 
3. Enter the IAM key and secret in the file *dwh.cfg* into the variables "KEY" and "SECRET". Continue to fill out the rest of the *dwh.cfg* with the appropriate information to create your Redshift cluster. Don't worry about the variables *DB_ENDPOINT* and *ARN*. Those variables input will be entered in later. 
4. Once the *dwh.cfg* file is complete, in terminal run:
        python 1_create_redshift.py 
This will create the Redshift cluster. At the end, record and save the *Endpoint* and *ARN* information into the *dwh.cfg* file. 
5. In the teriminal run: 
        python 2_create_tables.py
This will create the redshift tables to be populated in the next step.
6. In terminal run:
        python 3_etl.py
This load data from the sources files in AWS S3 to Redshift Analytic tables
7. In terminal run:
        python 4_qa_check.py
This will run some checks on the data to make sure the ETL process worked correctly.
8. When done using Redshift database, in terminal run:
        python 5_delete_redshift.py
        
   
## Explanation of Files
The project has three main types of files:
1. Python Scripts
2. Jupyter Notebooks
3. Configuration File
4. Bash file

### Python Scripts
In the main directory are (5) python scripts. Below is a breakdown of the scripts:
+ 1_create_redshift.py: Creates a Redshift cluster database on AWS
+ 2_create_tables.py: Creates Redshift tables
+ 3_etl.py: Run the ETL process to transfers the data from the source files from S3 to Redshift tables.
+ 4_qa_check.py: Does basic QA checks on the ETL process to make sure the data looks correct
+ 5_delete_redshift.py: Deletes the Redshift database and polices assigned.
+ sql_queries.py: This where all the SQL queries used in the all the python scripts above is stored.

### Notebooks
In the subdirectory *Notebooks* are Jupyter Notebooks that break down the python scripts into steps for easier debugging and future process improvement testing. 

### Configuration File
In the main directory is the file *dwh.cfg*. It is configuration file that needs information to run python scripts:
1. AWS: Defines the AWS Key and Secret to use for Redshift cluster creation
2. CLUSTER: Holds the information for Redshift cluster creation
3. IAM_ROLE: For accessing the Redshift cluster with appropriate privileges. 
4. S3: The paths in AWS to access the S3 source files for the ETL process. 

## Bash file
The Bash file *job_create.sh* runs all the python scripts to create the Redshift tables without having to run all the python scripts manually. 

## Schemas

### Star Schema for Analytic Tables
<img src="Notebooks/images/star_schema4.png" width="100%" />


### Schema for Staging Tables
<img src="Notebooks/images/sparkify_staging_tables2.png" width="75%" />