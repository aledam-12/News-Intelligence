import json
import spacy
from spacy import displacy

# Nome da cercare
NOME_TARGET = "Paolo Conti"

# Carica modello italiano
nlp = spacy.load("it_core_news_sm")

# 1️⃣ Carica tutti gli articoli
with open("../data/articles.json", "r", encoding="utf-8") as f:
    articoli = json.load(f)


# 🔎 Funzione per filtrare frasi dove NOME_TARGET è soggetto
def filtra_frasi_con_soggetto(doc, nome):
    frasi_rilevanti = []
    for sent in doc.sents:
        for ent in sent.ents:
            if ent.label_ == "PER" and nome.lower() in ent.text.lower():
                if any(token.dep_ == "nsubj" for token in ent):
                    frasi_rilevanti.append(sent)
                    break
    return frasi_rilevanti


# 2️⃣ Cicla su tutti gli articoli
frasi_trovate = []
for articolo in articoli:
    testo = articolo["testo"]
    titolo = articolo.get("titolo", "[Senza Titolo]")
    doc = nlp(testo)
    frasi = filtra_frasi_con_soggetto(doc, NOME_TARGET)

    if frasi:
        print(f"\n Titolo: {titolo}")
        print(f" Frasi trovate: {len(frasi)}")
        for frase in frasi:
            print(f"– {frase.text.strip()}")
        frasi_trovate.extend(frasi)

# 3️⃣ Visualizza con displacy solo se sono state trovate frasi
if not frasi_trovate:
    print(f"\n Nessuna frase trovata con '{NOME_TARGET}' come soggetto in tutti gli articoli.")
else:
    print(f"\n Totale frasi trovate: {len(frasi_trovate)}")

    # Visualizza ENTITÀ nelle frasi trovate
    for frase in frasi_trovate:
        displacy.render(frase, style="ent")

    # Visualizza ALBERO SINTATTICO
    for frase in frasi_trovate:
        displacy.render(frase, style="dep")

    # Avvia server per la prima frase trovata
    displacy.serve(frasi_trovate, style="dep")
