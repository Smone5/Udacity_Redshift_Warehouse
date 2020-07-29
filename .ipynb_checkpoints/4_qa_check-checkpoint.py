import configparser
import psycopg2
import pandas as pd
from sql_queries import count_rows_queries, check_duplicate_queries


def check_rows(cur, conn):
    table_names = ['song_stage', 'event_stage','dim_user', 'dim_song', 'dim_artist', 'dim_time', 'fact_songplay']
    for i in range(len(count_rows_queries)):
        
        df = pd.read_sql(count_rows_queries[i], conn)
        value = df.values[0][0]
        print("Row count in table {}: {}".format(table_names[i], value))

        
def check_dups(cur, conn):
    
    def check_duplicates(query, conn, table):
        count_df = pd.read_sql(query, conn)
        count_s = count_df['count']
        total_count = 0
        for val in count_s:
            if val == 1:
                total_count += 0

        if total_count > 0:
            return(print("Rows duplicated in table {}".format(table)))

        else:
            return(print("No rows duplicated in table {}".format(table)))

    table_names = ['dim_user', 'dim_song', 'dim_artist', 'dim_time']

    for i in range(len(check_duplicate_queries)):
        print()
        print("Check Duplications Table {}...".format(table_names[i]))
        check_duplicates(check_duplicate_queries[i], conn, table_names[i])
        

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    host = config['CLUSTER']['DB_ENDPOINT']
    dbname = config['CLUSTER']['DB_NAME']
    user = config['CLUSTER']['DB_USER']
    password = config['CLUSTER']['DB_PASSWORD']
    port = config['CLUSTER']['DB_PORT']

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(host, dbname, user, password, port))
    cur = conn.cursor()
    
    check_rows(cur, conn)
    check_dups(cur, conn)
    

    conn.close()


if __name__ == "__main__":
    main()