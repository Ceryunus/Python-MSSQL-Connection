import pandas as pd #veriyi düzenlemek için
import pyodbc       #MSSQL e bağlanmak için gerekli olam modül

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=serverismi;'
                      'Database=databeseismi;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
sql_query = pd.read_sql_query('SELECT * FROM databaseismi.dbo.tabloismi', conn)
print(sql_query)
print(type(sql_query))

#veri ekeleme
cursor.execute(
    '''
    INSERT INTO databaseismi.dbo.tabloismi (isim,soyisim,meslek,maas) VALUES ('Ayşe','gül','emekli',1995)

    '''
)
sql_query = pd.read_sql_query('SELECT * FROM databaseismi.dbo.tabloismi', conn)

print(sql_query)
