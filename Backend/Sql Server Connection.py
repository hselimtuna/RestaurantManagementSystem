import pyodbc

"""

-> Config'ler ayrı bir directory'de olacak back'in içinde değil

-> config'lerdeki db değerlerini config'den okuyacak böyle hard coded olmayacak 

doğrusu;
    conn =pyodbc.connect(f"Driver={config["key"]}"
                     f"Server={config["key_2"]};"      
                     
                     f"Database={config["key_3"]};"
                     "Trusted_Connection=yes;")
                     
config oluşturman için kullanacağın kütüphane configparser

-> https://docs.python.org/3/library/configparser.html burdan okuyarak bir config dosyası oluştur yeni oluşturacağın directory'nin içine 
        

"""

conn =pyodbc.connect("Driver={SQL Server};"
                     "Server=DESKTOP-O0K2KTB;"      
                     "Database=RMS;"
                     "Trusted_Connection=yes;")

'''
cursor=conn.cursor()
cursor.execute("SELECT * FROM loginscreen")

for i in cursor:
    print(i)
#Database connecting completed. -> logggg yazılacak buraya :) 
'''
