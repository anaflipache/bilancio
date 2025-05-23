from flask import Flask, request, render_template, redirect
from werkzeug.utils import redirect

from repository.bilancio_repository import *
from model.bilancio import Bilancio


app = Flask(__name__)


@app.get("/")
def get_index():
    lista_bilancio = elenco_bilancio_repo()
    saldo = saldo_totale_repo()
    return render_template("index.html", lista_bilancio=lista_bilancio, saldo=saldo)


# funzione per ottenere form page -> localhost:5000/form (GET)
@app.get("/form")
def get_form():
    return render_template("form.html")


@app.post("/form")
def gestione_form():
    dati_form = request.form
    print(dati_form, type(dati_form))
    bilancio = Bilancio(data=dati_form.get("data"), descrizione=dati_form.get("descrizione"), importo=dati_form.get("importo"), tipo=dati_form.get("tipo"))
    registrazione_bilancio_repo(bilancio)
    return redirect("/")


@app.get("/elimina")
def gestione_eliminazione():
    id_bilancio = request.args.get("id")
    eliminazione_bilancio_repo(id_bilancio)
    return redirect("/")



# eseguibilità
if __name__ == "__main__":
    app.run(debug=True)

