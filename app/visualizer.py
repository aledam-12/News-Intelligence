import json
import spacy
from spacy import displacy


nlp = spacy.load("it_core_news_sm")

# 1️⃣ Carica un articolo
with open("../data/articles.json", "r", encoding="utf-8") as f:
    articoli = json.load(f)

articolo = articoli[0]
doc = nlp(articolo["testo"])

# 2️⃣ Visualizza ENTITÀ
displacy.render(doc, style="ent")

# 3️⃣ Visualizza ALBERO SINTATTICO
displacy.render(doc, style="dep")

displacy.serve(doc, style="dep")