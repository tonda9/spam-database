# Czech Email Dataset for Spam/Ham Classification

## Dataset Overview

This dataset contains Czech language emails for training spam/ham classification models.

### Files

1. **spam.txt** - 500 spam emails (786 KB)
2. **ham.txt** - 1000 legitimate emails (372 KB)
3. **training_data.txt** - 300 training emails (200 HAM + 100 SPAM) in simple CSV format

### Format

#### spam.txt & ham.txt
Each email is separated by `===EMAIL===` and follows this structure:

```
Subject: <subject line>
From: <sender@email.com>
To: <recipient@email.com>
Date: <Czech format date>

<email body>
```

#### training_data.txt
Simple CSV format, one email per line:
```
<label>,<email text>
```
Where:
- `0` = HAM (legitimate email)
- `1` = SPAM (phishing/scam)

Example:
```
0,Dobrý den, vaše objednávka byla přijata.
1,Váš účet vyžaduje okamžité ověření na bezpecnost-uctu.cz
```

### Spam Categories

- Banking phishing (Česká spořitelna, ČSOB, Komerční banka)
- Delivery scams (Česká pošta, DHL, PPL)
- Investment/crypto scams
- Tech support scams (Microsoft, Norton, Avast)
- Lottery/prize scams
- Fake invoices (ČEZ, T-Mobile, hosting)
- Romance/dating scams
- Job offer scams
- Real estate scams  
- Healthcare/pharma spam
- Insurance scams
- Tax/government impersonation

### Ham Categories

- Personal: friends/family conversations, invitations, plans
- Work: meetings, projects, reports, vacation requests
- E-commerce: order confirmations, shipping updates, receipts
- Services: appointments, renewals, account notifications
- Newsletters: legitimate subscriptions
- Education: course info, university communication
- Community: neighborhood notices, event announcements
- Travel: booking confirmations, travel updates
- Banking: legitimate transaction notifications
- Government: official notices

### Dataset Statistics

- **Total emails**: 1,500 (500 spam + 1,000 ham)
- **Language**: Czech
- **Date range**: 2020-2026
- **Average email length**: 200-400 words
- **Format**: Plain text with structured headers

### Quality Features

✓ High diversity - no template repetition
✓ Realistic Czech language and style  
✓ Various formality levels
✓ Diverse email addresses and names
✓ Mixed date formats (Czech style)
✓ Sophisticated spam (not caricatures)
✓ Each email is unique

### Usage

```python
# Load spam emails (original format)
with open('spam.txt', 'r', encoding='utf-8') as f:
    spam_emails = f.read().split('===EMAIL===')

# Load ham emails (original format)
with open('ham.txt', 'r', encoding='utf-8') as f:
    ham_emails = f.read().split('===EMAIL===')

# Load training data (CSV format)
import csv
training_data = []
with open('training_data.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        label = int(row[0])
        text = row[1]
        training_data.append((label, text))
```

### Training Data (training_data.txt)

The `training_data.txt` file contains 300 compact training emails specifically designed for quick prototyping and model training:

**Composition:**
- 200 HAM emails (label: 0)
  - 70 newsletters/promo for existing customers
  - 70 system emails (invoices, password changes, order confirmations)
  - 40 personal or work communication
  - 20 neutral announcements
- 100 SPAM emails (label: 1)
  - 40 realistic phishing (account verification, security)
  - 30 payment or delivery problems
  - 30 investment/financial scams written subtly

**Features:**
- Each email is 1-5 sentences (concise format)
- Mix of formal and informal Czech language
- Includes variants with and without diacritics
- Realistic Czech phishing techniques
- No exaggerated spam (no CAPSLOCK floods, no emoji abuse)
- Shuffled labels for training

**Generation:**
To regenerate or create similar datasets, use:
```bash
python3 generate_training_data.py
```

### Notes

- Spam emails use realistic phishing and scam techniques seen in real attacks
- Ham emails include solicited business communications (these are legitimate)
- All content is synthetic but highly realistic
- Suitable for training binary classification models
