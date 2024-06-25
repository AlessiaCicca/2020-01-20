from database.DB_connect import DBConnect
from model.artista import Artista
from model.connessione import Connessione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getRuoli():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct a.`role` as ruolo
from authorship a"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["ruolo"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(ruolo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct a.*
from artists a, authorship a2 
where a.artist_id=a2.artist_id 
and a2.`role` =%s """

        cursor.execute(query,(ruolo,))

        for row in cursor:
            result.append(Artista(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessioni(ruolo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.a1 as v1,t2.a2 as v2, count(distinct t1.e1) as peso
from 
(select eo.exhibition_id as e1,a.artist_id as a1
from authorship a, exhibition_objects eo 
where a.`role` =%s and a.object_id =eo.object_id) as t1,
(select eo.exhibition_id as e2,a.artist_id as a2
from authorship a, exhibition_objects eo 
where a.`role` =%s and a.object_id =eo.object_id) as t2
where t1.a1<t2.a2 and t1.e1=t2.e2
group by t1.a1,t2.a2 """

        cursor.execute(query,(ruolo,ruolo,))

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result