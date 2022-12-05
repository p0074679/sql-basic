import sqlite3

sqliteConnection = sqlite3.connect('Junk.db')
cursor = sqliteConnection.cursor()

#get the count of tables with the name Students
cursor.execute('''SELECT count(name)
                 FROM sqlite_master
                 WHERE type='table'
                 AND name='SoccerTeams';''')

#if the count is 1, then the table exists
if not cursor.fetchone()[0]==1:

  cursor.execute('''CREATE TABLE SoccerTeams (
                             num INTEGER PRIMARY KEY AUTOINCREMENT,
                             Name TEXT NOT NULL,
                             Rank INTEGER NOT NULL,
                             Coach TEXT);''')
  sqliteConnection.commit()
  print("SQLite SoccerTeams table created")
  
  sqlite_insert_query = """REPLACE INTO SoccerTeams
                       (Rank, Name)
                       VALUES (?, ?);"""

  sqlite_remove_query = """delete from SoccerTeams
                       where Rank = ?;"""
  
  recordsToInsert = [(1, 'Canada'),(2,'Croatia')]
  
  cursor.executemany(sqlite_insert_query, recordsToInsert)

  cursor.execute(sqlite_remove_query, (2,))
  sqliteConnection.commit()
  print("Total", cursor.rowcount, "Records deleted successfully from SoccerTeams table")

sqlite_select_query = """SELECT * from soccerteams"""

cursor.execute(sqlite_select_query)
records = cursor.fetchall()

print(records)

cursor.close()

sqliteConnection.close()