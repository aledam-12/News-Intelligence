import json
import spacy

nlp = spacy.load("it_core_news_sm")

def extract_svo(doc):
    svos = []
    for token in doc:
        if token.pos_ == "VERB":
            soggetto = [w.text for w in token.lefts if w.dep_ in ("nsubj", "nsubj:pass")]
            oggetto = [w.text for w in token.rights if w.dep_ in ("obj", "obl", "xcomp")]
            if soggetto and oggetto:
                svos.append({
                    "entità": soggetto + oggetto,
                    "relazione": token.lemma_
                })
    return svos

def process_article(article):
    doc = nlp(article["testo"])
    svos = extract_svo(doc)
    return svos

if __name__ == "__main__":
    with open("../data/articles.json", "r", encoding="utf-8") as f:
        articoli = json.load(f)

    articolo = articoli[0]  # scegliamo il primo per esempio
    doc = nlp(articolo["testo"])

    print(f"\n📄 Titolo: {articolo['titolo']}\n")
    print("🔹 Soggetto-Verbo-Oggetto trovati:")

    svos = process_article(articolo)
    print(json.dumps(svos, indent=2, ensure_ascii=False))

    # Salvataggio in JSON
    with open("../output/svos.json", "w", encoding="utf-8") as f:
        json.dump(svos, f, indent=2, ensure_ascii=False)
