import pyodbc

scriptCon = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
    'Server={HC2817\\SQLEXPRESS};'
    'Database=GenDEV;'
    'Trusted_Connection=yes;')

scriptCursor = scriptCon.cursor()

scriptCursor.execute('SELECT * FROM dbo.GenTable1')

print(type(scriptCursor))

for row in scriptCursor:
    print(row)

scriptCursor.close()
scriptCon.close()
