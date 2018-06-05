import psycopg2
import sys
import time 

con = None
summ = 0
def toSql(inp):   # Perevod integer v sql datu
  inpDateStart = inp
  inpDateStart = """'"""+str(inpDateStart)+"""'"""
  date ="""TO_DATE(""" + inpDateStart+ """,'yyyymmdd')"""
  return date
try:
    con = psycopg2.connect("host='dev.db-support.ru' dbname='sibgurman' user='sibgurman' password='sibgurman'")   
    cur = con.cursor()
    print("Enter start date(yyyymmdd): ")
    dateStart = toSql(input())
    print("Enter end date(yyyymmdd): ")
    dateEnd = toSql(input())
    print("Enter articles for indexation: ")
    inp =[int(i) for i in input().split()] # stroka v massiv integer
   
    cur.execute("""select "common_salesdetail"."realizationDate", summa, articul_id  FROM common_salesdetail 
                   where "common_salesdetail"."realizationDate" BETWEEN """ + dateStart + """  AND """+ dateEnd + """ """) # sql zapros
    while True:
        row = cur.fetchone()
        if row == None:
            break
        if (inp.count(row[2]) > 0): # esli v massive articulov est danniy to etot element summiruetsya
         summ += row[1]
    print("Sum: ")
    print(summ)
finally:   
    if con:
        con.close()
