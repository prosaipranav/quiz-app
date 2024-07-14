import mysql.connector as mysql_conn
import pandas as pd
mydb=mysql_conn.connect(host='localhost',user='root',password='1234',database='quiz_project')
curs=mydb.cursor()
curs.execute("select * from quiz_names order by quiz_name asc")
var1=curs.fetchall()

df = pd.DataFrame(var1, columns=['ID','Quiz Name'])
df
count=0
total_question=0

quiz_id=input("which Quiz do you want to Attend, Enter its corresponding ID : ")

query = "SELECT * FROM quiz_questions WHERE id = %s ORDER BY q_no ASC"
curs.execute(query, (quiz_id,))
rows=curs.fetchall()

print()

for r in rows:
    total_question+=1
    id1=r[0]
    q_no1=r[1]
    print(total_question,". ",r[2])
    query1="select * from quiz_options where id= %s and q_no= %s order by option_no asc "
    curs.execute(query1, (id1,q_no1,))
    rows1=curs.fetchall()
    for r1 in rows1:
        print("\t",r1[2],") ",r1[3])
    ans=int(input("Enter your option : ")) 
    query2="Select option_no from quiz_answers where id=%s and q_no=%s"
    curs.execute(query2, (id1,q_no1,))
    correct=curs.fetchone()  
    
    if(ans==correct[0]):
        count+=1
        print("Correct\n\n")
        
    else:
        print("incorrect")
        print("correct option : ",correct[0],"\n\n")
print("---------------------------------------------------------------------------------\n")
print("Total Number of Questions   : ",total_question)
print('Correct Answers             : ',count)
print("Wrong Answers               : ",total_question-count)
print("Your final Score Card       : ",count,"/",total_question)
curs.close()
mydb.close()