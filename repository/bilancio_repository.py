import pymysql
from model.bilancio import Bilancio


def _get_connection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="bilancio_familiare"
    )


def elenco_bilancio_repo():
    try:
        with _get_connection() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM operazioni"
                cursor.execute(sql)
                risultato = cursor.fetchall()
                return [Bilancio(id, data, descrizione, importo, tipo) for id, data, descrizione, importo, tipo in risultato]
    except Exception as e:
        print(e)
        return None


# funzione per registrare un oggetto Persona nel db
def registrazione_bilancio_repo(bilancio):
    try:
        with _get_connection() as connection:
            with connection.cursor() as cursor:
                sql= "INSERT INTO operazioni (data, descrizione, importo, tipo) VALUES(%s,%s,%s, %s)"
                valori = bilancio.data, bilancio.descrizione, bilancio.importo, bilancio.tipo
                cursor.execute(sql, valori)
                connection.commit()
    except Exception as e:
        print(e)



def eliminazione_bilancio_repo(id):
    try:
        with _get_connection() as connection:
            with connection.cursor() as cursor:
                sql= "DELETE FROM operazioni WHERE id=%s"
                valori = id,
                cursor.execute(sql, valori)
                connection.commit()
    except Exception as e:
        print(e)


def saldo_totale_repo():
    try:
        with _get_connection() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT importo,tipo FROM operazioni"
                cursor.execute(sql)
                risultato = cursor.fetchall()
                totale =0
                for importo, tipo in risultato:
                    if tipo.lower() == "entrata":
                        totale += float(importo)
                    else:
                        totale -= float(importo)
                return totale
    except Exception as e:
        print(e)
