# Czech Email Dataset for Spam/Ham Classification

## Dataset Overview

This dataset contains Czech language emails for training spam/ham classification models.

### Files

1. **spam.txt** - 500 spam emails (786 KB)
2. **ham.txt** - 1000 legitimate emails (372 KB)

### Format

Each email is separated by `===EMAIL===` and follows this structure:

```
Subject: <subject line>
From: <sender@email.com>
To: <recipient@email.com>
Date: <Czech format date>

<email body>
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
# Load spam emails
with open('spam.txt', 'r', encoding='utf-8') as f:
    spam_emails = f.read().split('===EMAIL===')

# Load ham emails  
with open('ham.txt', 'r', encoding='utf-8') as f:
    ham_emails = f.read().split('===EMAIL===')
```

### Notes

- Spam emails use realistic phishing and scam techniques seen in real attacks
- Ham emails include solicited business communications (these are legitimate)
- All content is synthetic but highly realistic
- Suitable for training binary classification models
