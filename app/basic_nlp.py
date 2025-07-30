import json
import spacy

"""
    --| Part Of Speech of a given article
"""


# Carica modello italiano
nlp = spacy.load("it_core_news_sm")

# Leggi articoli dal file JSON
with open("../data/articles.json", "r", encoding="utf-8") as f:
    articoli = json.load(f)

# Prendi il primo articolo
articolo = articoli[0]
print(f"\n📄 Titolo: {articolo['titolo']}\n")
print(f"📰 Testo: {articolo['testo']}\n")

# Analizza il testo
doc = nlp(articolo["testo"])

print("🔹 TOKEN | LEMMA | POS")
print("-" * 40)
for token in doc:
    print(f"{token.text:15} {token.lemma_:15} {token.pos_}")

print("\n🔹 ENTITÀ RICONOSCIUTE")
print("-" * 40)
for ent in doc.ents:
    print(f"{ent.text:25} {ent.label_}")
