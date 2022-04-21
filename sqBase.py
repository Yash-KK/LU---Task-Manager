import sqlite3




connection = sqlite3.connect("text.db")
connection.execute("""
                   CREATE TABLE IF NOT EXISTS todo(
                       id INTEGER PRIMARY KEY,
                       task TEXT NOT NULL
                   );
                   
                   """)

# Retriving Data from database
def show():
    query = 'SELECT * FROM todo;'
    return connection.execute(query)

"""
Inserting Data into Database
"""
def insertData(task):
    query = "INSERT INTO todo(task) VALUES(?);"
    connection.execute(query, (task,))
    connection.commit()

# Deleting data from database
def deleteById(taskid):
    query = "DELETE FROM todo WHERE id = ?;"
    connection.execute(query, (taskid,))
    connection.commit()
    
def deleteBytask(taskval):
    query = "DELETE FROM todo WHERE task = ?;"
    connection.execute(query, (taskval,))
    connection.commit()
        
# Updating data from database
def updateData(taskid, newtask):
    query = "UPDATE todo SET task = ? WHERE id = ?;"
    connection.execute(query, (newtask,taskid))
    connection.commit()
# insertData("Delete this task")

# deleteById(5)

# updateData(1,"Record Updated!")

# """
# Retriving Data from DataBase
# """
# query = 'SELECT * FROM todo;'
# for rows in connection.execute(query):
#     print(rows)


