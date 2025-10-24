import mysql.connector
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

env_User = os.getenv("user")
env_Password = os.getenv("password")
env_Host = os.getenv("host")


mydb = mysql.connector.connect(
    host = env_Host,
    port = 3306,
    user = env_User,
    password = env_Password,
    database = "musikk"
)
mycursor = mydb.cursor()



if mydb.is_connected():
    print("Tilkoblet!")




try: #Lager table og hvis den allerede finnes/ du får en error så printer den ut The tables already exist

    
    mycursor.execute("CREATE TABLE artister (id INT AUTO_INCREMENT PRIMARY KEY, artist VARCHAR(50), sanger INT, sjanger VARCHAR(50))")
    print(mycursor.rowcount, "record(s) affected")

    

    
    mydb = mysql.connector.connect(
    host = "10.200.14.24",
    port = 3306,
    user = "edmalema",
    password = "norge123",
    database = "musikk"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE sanger (id INT AUTO_INCREMENT PRIMARY KEY, navn VARCHAR(50), artist VARCHAR(50), lengde FLOAT(4,2) CHECK (lengde <= 99.99 AND lengde >= 0.01), Sjanger VARCHAR(50))")
    print(mycursor.rowcount, "record(s) affected")

    
except:
        print("The tables already exist")



if False == True: #gjør ikke denne delen av koden, jeg har den her for å minne meg på hva variablene het
    try:
        print("allerede lagd")
        #mydb = mysql.connector.connect(
        #host = "10.200.14.24",
        #port = 3306,
        #user = "edmalema",
        #password = "norge123",
        #database = "musikk"
        #)
        #mycursor = mydb.cursor()
        #sql = "INSERT INTO artister (artist, sanger, sjanger) VALUES (%s, %s, %s)"
        #val = [
        #    ('Drake', 0, 'pop'),
        #    ('Taylor swift',0, 'pop')
        #]
        #mycursor.executemany(sql, val)
        #mydb.commit()
        #print(mycursor.rowcount, "record inserted.")
    except:
        print("noe gikk feil")



    

    mydb = mysql.connector.connect(
    host = "10.200.14.24",
    port = 3306,
    user = "edmalema",
    password = "norge123",
    database = "musikk"
    )
    mycursor = mydb.cursor()


    sql = "INSERT INTO sanger (navn, artist, lengde, Sjanger) VALUES (%s, %s, %s, %s)"
    val = [
        ('i want to meet your madre', 'Drake', 4.32, 'pop'),
        ('gods plan','Drake', 5.57, 'rap'),
        ('fortnight', 'Taylor swift',4.10, 'pop')
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    try:
        print("Allerede lagd")
    except: #(FUNKER IKKE)
        mydb = mysql.connector.connect(
        host = "10.200.14.24",
        port = 3306,
        user = "edmalema",
        password = "norge123",
        database = "musikk"
        )
        mycursor = mydb.cursor()
        
        mycursor.execute(""" 
        DELIMITER $$ 
        CREATE PROCEDURE antallSanger() 
        BEGIN 
        DECLARE no INT DEFAULT 0; 
        loop: LOOP 
            SET no = no +1; 
            select no; 
            DECLARE antall INT DEFAULT 0; 
            DECLARE num INT DEFAULT 0; 
            secLoop: LOOP 
                SET num = num + 1; 
                select num ; 
                SELECT artist INTO @artistSang FROM sanger WHERE id = num;
                SELECT artist INTO @artistArtist FROM artister WHERE id = no;
                IF @artist = @artist 
                THEN 
                    SET antall = antall + 1; 
                select num ; 
                IF num = (SELECT * FROM sanger) 
                THEN 
                    LEAVE secLoop; 
                END IF;
            END LOOP secLoop; 
            UPDATE artister 
            SET sanger = antall 
            WHERE ID = no; 
            SELECT no; 
            IF no = (SELECT * FROM artister) 
            THEN 
                LEAVE loop; 
            END IF; 
        END LOOP loop; 
        SELECT no; 
        END $$ DELIMITER;
        
        
        """)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

#try:
#    mycursor.execute("CALL antallSanger();")
#    print(mycursor.rowcount, "record(s) affected")
#except:
#    print("error sorting")


def Sorter_Mengde(): #sorterer hvor mange sanger som enhver artist har lagd.
    mydb = mysql.connector.connect(
    host = "10.200.14.24",
    port = 3306,
    user = "edmalema",
    password = "norge123",
    database = "musikk"
    )
    mycursor = mydb.cursor()
        
    mycursor.execute("""
    UPDATE artister a
    JOIN (
    SELECT artist, COUNT(*) AS antall
    FROM sanger
    GROUP BY artist
    ) s ON a.artist = s.artist
    SET a.sanger = s.antall;
    """)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
Sorter_Mengde()


while True: #Looper igjen og igjen for ikke å stoppe programmet

    print("+------------+-----------------+")
    print("|  Lese (1)  |   Redigere (2)  |")
    print("+------------+-----------------+")
    InitQ = input(" ")
    if InitQ.lower() == "1": # Leser fra databasen
        while True:
            print("+--------------+-----------------+-------------+---------------------------+")
            print("|  Sanger (1)  |   Artister (2)  |   Exit (3)  |   Navnet til sang/artist  |")
            print("+--------------+-----------------+-------------+---------------------------+")

            ReadQ = input(" ")
            if ReadQ.lower() == "1": #skriver ut alle sangene
                mydb = mysql.connector.connect(
                host = "10.200.14.24",
                port = 3306,
                user = "edmalema",
                password = "norge123",
                database = "musikk"
                )
                mycursor = mydb.cursor()
                
                mycursor.execute("SELECT * FROM sanger")

                myresult = mycursor.fetchall()

                for x in myresult:
                    print(x)
            elif ReadQ.lower() == "2": #skriver ut alle artistene
                mydb = mysql.connector.connect(
                host = "10.200.14.24",
                port = 3306,
                user = "edmalema",
                password = "norge123",
                database = "musikk"
                )
                mycursor = mydb.cursor()
                
                mycursor.execute("SELECT * FROM artister")

                myresult = mycursor.fetchall()

                for x in myresult:
                    print(x)

            elif ReadQ.lower() == "3": #går tilbake
                break
            else: #hvis du skrev noe annet så antar den at det er navnet til sangen/artisten

                print("+----------------+---------------+")
                print("|  Artisten (1)  |   Sangen (2)  |")
                print("+----------------+---------------+")
                BestemtQ = input(" ")
                if BestemtQ.lower() == "1": 

                    try:
                        sql = f"SELECT * FROM artister WHERE artist ='{ReadQ}'"

                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()

                        for x in myresult:
                            print(x)
                    
                
                    
                        sql = f"SELECT * FROM sanger WHERE artist ='{ReadQ}'"

                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()

                        for x in myresult:
                            print(x)
                    except:
                        print("den artisten finnes ikke ")


                elif BestemtQ.lower() == "2":
                    try:
                        sql = f"SELECT * FROM sanger WHERE navn ='{ReadQ}'"

                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()

                        for x in myresult:
                            print(x)
                    except: 
                        print("den sangen finnes ikke")
                else:
                    print("error")
    elif InitQ.lower() == "2": #Redigerer databasen
        while True:
            print("+--------------+-----------------+-------------+")
            print("|  Artister (1)  |   Sanger (2)  |   Exit (3)  |")
            print("+--------------+-----------------+-------------+")
            TableQ = input(" ")
            if TableQ.lower() == "1": #Lar deg redigere artister tabellen
                while True:
                    print("+--------------+-----------------+--------+")
                    print("|  Add (1)  |   Update (2)  |   Exit (3)  |")
                    print("+--------------+-----------------+--------+")
                    ActionQ = input(" ")
                    if ActionQ.lower() == "1": #Lar deg legge til en ny artist
                        print("+--------------------------------------------+")
                        print("|  Hva heter artisten din? (case sensetive)  |")
                        print("+--------------------------------------------+")
                        NavnQ = input(" ")
                        print("+---------------------------------------------------+")
                        print("|  Hvilken sjanger er det {NavnQ} jobber mest med?  |")
                        print("+---------------------------------------------------+")
                        SjangerQ = input(" ")
                        mydb = mysql.connector.connect(
                        host = "10.200.14.24",
                        port = 3306,
                        user = "edmalema",
                        password = "norge123",
                        database = "musikk"
                        )
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO artister (artist, sanger, sjanger) VALUES (%s, %s, %s)"
                        val = [(NavnQ, 0, SjangerQ)]
                        mycursor.executemany(sql, val)
                        mydb.commit()
                        print(mycursor.rowcount, "record inserted.")

                        Sorter_Mengde()
                    elif ActionQ.lower() == "2": #Lar deg redigere sangen du vil redigere en artist
                        print("+--------------------------------------+")
                        print("|  Navn til artisten du vil redigere:  |")
                        print("+--------------------------------------+")
                        NavnQ = input(" ")
                        print("+---------------------------------+")
                        print("|  Hva skal det nye navnet være?  |")
                        print("+---------------------------------+")
                        NyttNavnQ = input(" ")
                        print("+------------------------------------+")
                        print("|  Hva skal den nye sjangeren være?  |")
                        print("+------------------------------------+")
                        NySjangerQ = input(" ")

                        mydb = mysql.connector.connect(
                        host = "10.200.14.24",
                        port = 3306,
                        user = "edmalema",
                        password = "norge123",
                        database = "musikk"
                        )
                        mycursor = mydb.cursor()
                        mycursor.execute(f"""
                        UPDATE artister 
                        SET artist = {NyttNavnQ}, sjanger = {NySjangerQ}
                        WHERE artist = {NavnQ}
                        """)


                        Sorter_Mengde()
                    elif ActionQ.lower() == "3":
                        break
                    else:
                        print("error")
            elif TableQ.lower() == "2": #Lar deg redigere sanger tabellen

                    print("+-----------+---------------+-------------+")
                    print("|  Add (1)  |   Update (2)  |   Exit (3)  |")
                    print("+-----------+---------------+-------------+")
                    ActionQ = input(" ")
                    if ActionQ.lower() == "1": #Lar deg legge til en ny sang

                        print("+-------------------------+")
                        print("|  Hva heter sangen din?  |")
                        print("+-------------------------+")
                        MusikkQ = input(" ")
                        print("+-------------------------------------------+")
                        print(f"|  Hvem lagde {MusikkQ}? (case sensetive):  |")
                        print("+-------------------------------------------+")
                        NavnQ = input(" ")
                        print("+------------------------------------+")
                        print(f"|  Hvor lang er {MusikkQ}? (float):  |")
                        print("+------------------------------------+")
                        LengdeQ = float(input(" "))
                        print("+---------------------------------+")
                        print(f"|  Hvilken sjanger er {MusikkQ}?  |")
                        print("+---------------------------------+")
                        SjangerQ = input(" ")

                        mydb = mysql.connector.connect(
                        host = "10.200.14.24",
                        port = 3306,
                        user = "edmalema",
                        password = "norge123",
                        database = "musikk"
                        )
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO sanger (navn, artist, lengde, Sjanger) VALUES (%s, %s, %s, %s)"
                        val = [
                            (MusikkQ, NavnQ, LengdeQ, SjangerQ)
                        ]
                        mycursor.executemany(sql, val)
                        mydb.commit()
                        print(mycursor.rowcount, "record inserted.")

                        Sorter_Mengde()

                    elif ActionQ.lower() == "2": #Lar deg redigere en sang
                        try:
                            print("+-------------------------------------+")
                            print("|  Hva heter sangen du vil forandre?  |")
                            print("+-------------------------------------+")
                            SangQ = input(" ")
                            print("+-------------------------+")
                            print("|  Hva skal sangen hete?  |")
                            print("+-------------------------+")
                            NySangQ = input(" ")
                            print("+---------------------+")
                            print("|  Hvem er artisten?  |")
                            print("+---------------------+")
                            NyArtistQ = input(" ")
                            print("+-----------------------------------------+")
                            print("|  Hvor lang er den nye sangen? (float):  |")
                            print("+-----------------------------------------+")
                            NyLengdeQ = float(input(" "))
                            print("+------------------------------------+")
                            print("|  Hva skal den nye sjangeren være?  |")
                            print("+------------------------------------+")
                            NySjangerQ = input(" ")

                            mydb = mysql.connector.connect(
                            host = "10.200.14.24",
                            port = 3306,
                            user = "edmalema",
                            password = "norge123",
                            database = "musikk"
                            )
                            mycursor = mydb.cursor()
                            mycursor.execute(f"""
                            UPDATE sanger 
                            SET navn = {NySangQ}, artist = {NyArtistQ}, lengde = {NyLengdeQ}, Sjanger = {NySjangerQ}
                            WHERE navn = {SangQ}
                            """)


                            Sorter_Mengde()
                        except:
                            print("En error oppså, var det en float du skrev?")
                        
                    elif ActionQ.lower() == "3":
                        break
                    else:
                        print("error")
            elif TableQ.lower() == "3":
                break
    else:
        print("Error")



