import mysql.connector as mysql_conn
import pandas as pd
mydb=mysql_conn.connect(host='localhost',user='root',password='1234',database='quiz_project')
curs=mydb.cursor()
quiz_name = input("Enter Name of Quiz: ")

check_query = "SELECT id FROM quiz_names WHERE quiz_name = %s"
curs.execute(check_query, (quiz_name,))
existing_quiz = curs.fetchone()

if existing_quiz:
    print("Quiz name already exists. Please provide another quiz name.")
else:
    query1 = "SELECT count(id) FROM quiz_names"
    curs.execute(query1)
    quiz_id = curs.fetchone()[0]+1
    
    insert_query = "INSERT INTO quiz_names(id,quiz_name) VALUES (%s,%s)"
    curs.execute(insert_query, (quiz_id,quiz_name))
    
    n = int(input("Total Number of Questions: "))
    
    for i in range(1, n+1):
        print("\n...................................\n")
        print("Enter question Number", i, ": ")
        question = input()
        
        query2 = "INSERT INTO quiz_questions VALUES (%s, %s, %s)"
        curs.execute(query2, (quiz_id, i, question))
    
        print("Enter options:\n")
        for j in range(1, 5):
            print("Enter Option", j, ": ")
            option = input()
            query3 = "INSERT INTO quiz_options (id, q_no, option_no, options_) VALUES (%s, %s, %s, %s)"
            curs.execute(query3, (quiz_id, i, j, option))
    
        correct = int(input("Enter the correct option: "))  
        query4 = "INSERT INTO quiz_answers (id, q_no, option_no) VALUES (%s, %s, %s)"
        curs.execute(query4, (quiz_id, i, correct))
    
    mydb.commit()
    
    print("\n------------------------------------------------------------------------\n")
    print("\nCongratulations !! Your Quiz Successfully Created !!\n ")

curs.close()
mydb.close()
    