from flask import Flask, escape, request, jsonify
import ibm_db_dbi
import ibm_db

app = Flask(__name__)

db = 'MOVIE'
hostname = '165.165.131.79'
port = '50000'
userid = 'db2inst1'
pwd = 'db2admin'

conn_str = 'database={0};hostname={1};port={2};protocol=tcpip;uid={3};pwd={4}'.format(db, hostname, port, userid, pwd)
ibm_db_conn = ibm_db.connect(conn_str, '', '')

# Connect using ibm_db_dbi
conn = ibm_db_dbi.Connection(ibm_db_conn)

@app.route('/hello')
def hello():
    return 'Hello, the world is yours!'

@app.route('/api')
def api():
    # Fetch data using ibm_db_dbi
    select = "SELECT * FROM MOVIE.BASICS FETCH FIRST 50 ROWS ONLY"
    cur = conn.cursor()
    cur.execute(select)
    return jsonify(cur.fetchall())
    cur.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
