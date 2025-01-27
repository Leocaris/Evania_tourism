# # app.py code

# from flask import Flask, render_template, request, jsonify
# import pymysql

# app = Flask(__name__)

# # Database connection configuration
# db_config = {
#     'host': 'localhost',  # Update as needed
#     'user': 'root',       # Your MySQL username
#     'password': 'Grishma@2005',  # Your MySQL password
#     'database': 'TOURISM'  # Your database name
# }

# def get_db_connection():
#     connection = pymysql.connect(
#         host=db_config['host'],
#         user=db_config['user'],
#         password=db_config['password'],
#         database=db_config['database']
#     )
#     return connection

# # Frontend export
# @app.route('/')
# def index():
#     return render_template('query_page.html')

# # Query details
# @app.route('/execute_query', methods=['POST'])
# def execute_query():
#     data = request.get_json()
#     query = data.get('query')

#     if not query:
#         return jsonify({'success': False, 'message': 'No query specified'})

#     queries = {
#         "Option1": "SELECT PNAME, COUNT(*) AS NUMBER_OF_BOOKINGS FROM PREVIOUS_BOOKINGS GROUP BY PNAME ORDER BY NUMBER_OF_BOOKINGS DESC LIMIT 1;",
#         "Option2": "SELECT PNAME, PRICE FROM PACKAGE ORDER BY CAST(PRICE AS UNSIGNED) ASC LIMIT 1;",
#         "Option3": "SELECT PNAME, AVG(RATING) AS AVERAGE_RATING FROM RATINGS WHERE GENDER = 'Female' GROUP BY PNAME ORDER BY AVERAGE_RATING DESC LIMIT 1;",
#         "Option4": "SELECT PNAME, AVG(RATING) AS AVERAGE_RATING FROM RATINGS GROUP BY PNAME ORDER BY AVERAGE_RATING DESC LIMIT 3;",
#         "Option5": "SELECT B.PNAME, B.PHONE FROM BOOKINGS B JOIN CUSTOMERS C ON B.PHONE = C.PHONE WHERE C.COUNTRY = 'USA';",
#         "Option6": "SELECT C.CITY, COUNT(B.PHONE) AS TOTAL_BOOKINGS FROM CUSTOMERS C JOIN BOOKINGS B ON C.PHONE = B.PHONE GROUP BY C.CITY;",
#         "Option7": "SELECT C.FNAME, C.LNAME, C.EMAIL, C.PHONE, C.CITY, C.COUNTRY FROM CUSTOMERS C LEFT JOIN PREVIOUS_BOOKINGS PB ON C.PHONE = PB.PHONE WHERE PB.PHONE IS NULL;",
#         "Option8": "SELECT FNAME, LNAME, PHONE FROM PREVIOUS_BOOKINGS WHERE PNAME = 'Goa Getaway';",
#         "Option9": "SELECT FNAME, LNAME, PHONE FROM PREVIOUS_BOOKINGS WHERE PNAME = 'Rajasthan Royalty';",
#         "Option10": "SELECT PNAME, AVG(RATING) AS AVERAGE_RATING, COUNT(*) AS TOTAL_RATINGS FROM RATINGS GROUP BY PNAME;"
#     }


#     sql_query = queries.get(query)

#     if not sql_query:
#         return jsonify({'success': False, 'message': 'Invalid query option'})

#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor(pymysql.cursors.DictCursor)

#         print(f"Executing Query: {sql_query}")  # Debugging
#         cursor.execute(sql_query)
#         results = cursor.fetchall()
#         print(f"Results: {results}")  # Debugging

#         cursor.close()
#         connection.close()

#         return jsonify({'success': True, 'results': results})
#     except Exception as e:
#         print(f"Error: {str(e)}")  # Debugging
#         return jsonify({'success': False, 'message': str(e)})



# @app.route('/test-db')
# def test_db():
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         cursor.execute("SHOW TABLES;")
#         tables = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return f"Connected! Tables: {tables}"
#     except Exception as e:
#         return f"Error: {e}"



# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Grishma@2005',
    'database': 'TOURISM'
}

def get_db_connection():
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    return connection

# Routes

# Page-routes
@app.route('/')
def index():
    return render_template('index.html')  # Serve index.html

@app.route('/queries')
def queries():
    return render_template('query_page.html')  # Serve query_page.html

@app.route('/packages')
def packages():
    return render_template('package.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

# query-routes
@app.route('/execute_query', methods=['POST'])
def execute_query():
    data = request.get_json()
    query = data.get('query')

    queries = {
        "Option1": "SELECT PNAME, COUNT(*) AS NUMBER_OF_BOOKINGS FROM PREVIOUS_BOOKINGS GROUP BY PNAME ORDER BY NUMBER_OF_BOOKINGS DESC LIMIT 1;",
        "Option2": "SELECT PNAME, PRICE FROM PACKAGE ORDER BY CAST(PRICE AS UNSIGNED) ASC LIMIT 1;",
        "Option3": "SELECT PNAME, AVG(RATING) AS AVERAGE_RATING FROM RATINGS WHERE GENDER = 'Female' GROUP BY PNAME ORDER BY AVERAGE_RATING DESC LIMIT 1;",
        "Option4": "SELECT PNAME, AVG(RATING) AS AVERAGE_RATING FROM RATINGS GROUP BY PNAME ORDER BY AVERAGE_RATING DESC LIMIT 3;",
        "Option5": "SELECT B.PNAME, B.PHONE FROM BOOKINGS B JOIN CUSTOMERS C ON B.PHONE = C.PHONE WHERE C.COUNTRY = 'USA';",
        "Option6": "SELECT C.CITY, COUNT(B.PHONE) AS TOTAL_BOOKINGS FROM CUSTOMERS C JOIN BOOKINGS B ON C.PHONE = B.PHONE GROUP BY C.CITY;",
        "Option7": "SELECT C.FNAME, C.LNAME, C.EMAIL, C.PHONE, C.CITY, C.COUNTRY FROM CUSTOMERS C LEFT JOIN PREVIOUS_BOOKINGS PB ON C.PHONE = PB.PHONE WHERE PB.PHONE IS NULL;",
        "Option8": "SELECT FNAME, LNAME, PHONE FROM PREVIOUS_BOOKINGS WHERE PNAME = 'Goa Getaway';",
        "Option9": "SELECT FNAME, LNAME, PHONE FROM PREVIOUS_BOOKINGS WHERE PNAME = 'Rajasthan Royalty';",
        "Option10": "SELECT PNAME, AVG(RATING) AS AVERAGE_RATING, COUNT(*) AS TOTAL_RATINGS FROM RATINGS GROUP BY PNAME;"
    }

    sql_query = queries.get(query)

    if not sql_query:
        return jsonify({'success': False, 'message': 'Invalid query option'})

    try:
        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        cursor.execute(sql_query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify({'success': True, 'results': results})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
