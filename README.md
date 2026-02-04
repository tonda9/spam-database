# Czech Spam Email Database

Databáze českých spam a legitimních (ham) emailů pro trénink modelů strojového učení k rozpoznávání spamu.

## Obsah

Tato databáze obsahuje celkem **1400 emailů v češtině**:

### Spam Emaily (700 celkem)
- **500 sofistikovaných spam emailů** (`spam_emails/spam_sophisticated_*.txt`)
  - Phishing útoky na bankovní účty
  - Podvodné loterie a výhry
  - Falešné faktury
  - CEO fraud (podvody s šéfem)
  - Tech support scamy
  - Kryptoměnové podvody
  - Romance scamy

- **200 běžných spam emailů** (`spam_emails/spam_common_*.txt`)
  - Jednoduché spam zprávy
  - Viagra reklamy
  - Půjčky
  - Výprodeje
  - Casino reklamy

### Ham Emaily - Legitimní (700 celkem)
- **500 sofistikovaných legitimních emailů** (`ham_emails/ham_sophisticated_*.txt`)
  - Firemní komunikace
  - Potvrzení objednávek
  - Newslettery
  - Potvrzení schůzek
  - Pracovní emaily
  - Univerzitní komunikace
  - Bankovní výpisy
  - Pozvánky na akce

- **200 běžných legitimních emailů** (`ham_emails/ham_common_*.txt`)
  - Krátké osobní zprávy
  - SMS-styl zprávy
  - Rychlá komunikace mezi přáteli/kolegy

## Struktura

```
spam-database/
├── spam_emails/
│   ├── spam_sophisticated_0001.txt ... spam_sophisticated_0500.txt
│   └── spam_common_0001.txt ... spam_common_0200.txt
├── ham_emails/
│   ├── ham_sophisticated_0001.txt ... ham_sophisticated_0500.txt
│   └── ham_common_0001.txt ... ham_common_0200.txt
├── generate_emails.py          # Skript pro generování emailů
└── README.md                   # Tento soubor
```

## Použití

### Načtení dat v Pythonu

```python
import os
import glob

# Načíst všechny spam emaily
spam_emails = []
for filepath in glob.glob("spam_emails/*.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        spam_emails.append(f.read())

# Načíst všechny ham emaily
ham_emails = []
for filepath in glob.glob("ham_emails/*.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        ham_emails.append(f.read())

print(f"Načteno {len(spam_emails)} spam emailů")
print(f"Načteno {len(ham_emails)} ham emailů")
```

### Příprava pro ML model

```python
import pandas as pd

# Vytvořit DataFrame
data = []
for email in spam_emails:
    data.append({"text": email, "label": "spam"})
for email in ham_emails:
    data.append({"text": email, "label": "ham"})

df = pd.DataFrame(data)

# Rozdělit na train/test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42
)
```

## Charakteristiky

- **Jazyk**: Čeština
- **Formát**: UTF-8 text soubory
- **Velikost**: 1400 emailů
- **Rozdělení**: 50% spam, 50% ham
- **Typy**: Sofistikované i běžné příklady
- **Použití**: Trénink modelů pro detekci spamu

## Generování

Pro regenerování nebo rozšíření databáze použijte:

```bash
python3 generate_emails.py
```

## Licence

Tento dataset je vytvořen pro vzdělávací a výzkumné účely.

## Poznámky

- Všechny emaily jsou synteticky vygenerované
- Žádné osobní údaje nejsou reálné
- URL a telefonní čísla jsou fiktivní
- Emaily reprezentují typické vzory spam a legitimní komunikace v českém prostředí
