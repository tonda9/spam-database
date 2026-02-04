#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Czech spam and ham emails for ML training
"""

import os
import random

# Sophisticated spam templates in Czech
SOPHISTICATED_SPAM = [
    # Banking/Finance phishing
    "Vážený kliente,\n\nVaše transakce v částce {amount} Kč vyžaduje potvrzení. Klikněte na následující odkaz pro autorizaci: {link}\n\nČeská spořitelna\nOdděleníbezpečnosti",
    "Dobrý den,\n\nDetekovali jsme neautorizovanou aktivitu na Vašem účtu. Pro zabránění zablokování účtu prosím ověřte své údaje na: {link}\n\nS pozdravem,\nKomerční banka",
    "Upozornění o bezpečnosti\n\nNa Vašem účtu byla provedena podezřelá transakce {amount} Kč. Okamžitě ověřte na {link}\n\nRaiffeisenbank",
    
    # Lottery/Prize scams
    "Gratulujeme!\n\nVyhráli jste {amount} Kč v loterii České Sazky! Pro výběr výhry zadejte své údaje: {link}\n\nČeská loterie",
    "VÝHRA! Vyhráli jste evropskou loterii - {amount} EUR! Vyplňte formulář pro převod: {link}",
    
    # Fake invoices
    "Faktura č. {invoice}\n\nDlužná částka: {amount} Kč\nSplatnost: {date}\n\nPro úhradu klikněte: {link}\n\nÚčetní oddělení",
    
    # CEO fraud
    "Dobrý den,\n\nPotřebuji naléhavě provést převod {amount} Kč. Je to důvěrné. Potvrďte na: {link}\n\nJan Novák\nŘeditel",
    
    # Tech support scams
    "BEZPEČNOSTNÍ VÝSTRAHA\n\nVáš počítač je infikován virem! Okamžitě nainstalujte antivirovou aktualizaci: {link}\n\nMicrosoft Česká republika",
    
    # Cryptocurrency scams
    "Investiční příležitost století!\n\nBitcoin vzroste o 500%! Investujte nyní minimálně {amount} Kč: {link}\n\nCrypto Solutions",
    
    # Romance scams
    "Ahoj,\n\nJsem Maria z Prahy. Ráda bych tě poznala. Podívej se na můj profil: {link}\n\nS láskou, Maria",
]

# Common spam templates
COMMON_SPAM = [
    "KLIKNI ZDE! Výhra {amount} Kč!!! {link}",
    "Viagra za super cenu! Jen {amount} Kč! Objednej na {link}",
    "Půjčka ihned! {amount} Kč bez registru! {link}",
    "ZDARMA iPhone 15! Zaregistruj se: {link}",
    "Hubni snadno! Ztratil jsem 20kg za měsíc! {link}",
    "Domácí práce! Vyděláš {amount} Kč denně! {link}",
    "ROLEX hodinky jen {amount} Kč!!! {link}",
    "Casino online! Bonus {amount} Kč zdarma! {link}",
    "Zvětši penis o 10cm! Zaručený výsledek! {link}",
    "VÝPRODEJ!!! Vše za {amount} Kč! {link}",
]

# Sophisticated ham (legitimate) templates
SOPHISTICATED_HAM = [
    # Business emails
    "Dobrý den,\n\nRádi bychom Vás pozvali na firemní školení dne {date} v {time} hod. Téma: \"Nové trendy v oboru\".\n\nProsím potvrďte účast.\n\nS pozdravem,\n{name}\nPersonální oddělení",
    
    "Vážený pane {name},\n\nOdesíláme Vám smlouvu k podpisu ve formátu PDF v příloze. Lhůta pro podpis je {date}.\n\nV případě dotazů nás kontaktujte.\n\nS úctou,\nPrávní oddělení",
    
    # Confirmations
    "Dobrý den,\n\nVaše objednávka č. {invoice} byla úspěšně zpracována a odeslána. Sledovací číslo: {tracking}\n\nOčekávaný termín doručení: {date}\n\nS pozdravem,\nZákaznický servis",
    
    # Newsletters
    "Novinky z našeho obchodu\n\nVážení zákazníci,\n\nV tomto týdnu nabízíme slevu 20% na vybrané produkty. Akce platí do {date}.\n\nTěšíme se na Vaši návštěvu.\n\nVáš tým",
    
    # Appointment confirmations
    "Potvrzení schůzky\n\nDobrý den,\n\nPotvrdzujeme Vaši schůzku dne {date} v {time} hod. s panem doktorem {name}.\n\nOdborná ambulance\nTel: {phone}",
    
    # Work related
    "Ahoj {name},\n\nPřipomínám zítřejší poradu v {time} hod. Budeme probírat Q1 výsledky.\n\nDíky,\n{sender}",
    
    # University/Education
    "Vážení studenti,\n\nInformujeme Vás o změně místnosti přednášky dne {date}. Nová místnost: {room}.\n\nKatedra informatiky\nVŠE Praha",
    
    # Banking (legitimate)
    "Výpis z účtu\n\nDobrý den,\n\nV příloze zasíláme měsíční výpis z Vašeho účtu za období {date}.\n\nČeská spořitelna",
    
    # Event invitations
    "Pozvánka na konferenci\n\nVážení hosté,\n\nPozýváme Vás na konferenci \"Digitální transformace\" dne {date}. Registrace na www.conference.cz\n\nOrganizační tým",
    
    # Family/Friends
    "Ahoj {name},\n\nJak se máš? Dlouho jsme se neviděli. Máš čas na kávu příští týden?\n\nNapiš mi,\n{sender}",
]

# Common ham templates
COMMON_HAM = [
    "Ahoj, dnes večer kino? {name}",
    "Nezapomeň koupit mléko cestou domů.",
    "Meeting zítra ve {time}.",
    "Díky za včerejší pomoc!",
    "Posílám dokumenty v příloze.",
    "Můžeš mi zavolat?",
    "Jsem v zácpě, přijdu pozdě.",
    "Skvělá práce na projektu!",
    "Oběd ve {time}?",
    "Všechno nejlepší k narozeninám!",
]

def generate_spam_email(sophisticated=True, index=0):
    """Generate a spam email"""
    templates = SOPHISTICATED_SPAM if sophisticated else COMMON_SPAM
    template = random.choice(templates)
    
    # Fill in placeholders
    amount = random.choice([5000, 10000, 15000, 25000, 50000, 100000, 250000])
    link = f"http://malware-site-{random.randint(1000, 9999)}.com/phishing"
    invoice = f"INV-{random.randint(10000, 99999)}"
    date = f"{random.randint(1, 28)}.{random.randint(1, 12)}.2024"
    
    email = template.format(
        amount=amount,
        link=link,
        invoice=invoice,
        date=date
    )
    
    return email

def generate_ham_email(sophisticated=True, index=0):
    """Generate a legitimate email"""
    templates = SOPHISTICATED_HAM if sophisticated else COMMON_HAM
    template = random.choice(templates)
    
    # Fill in placeholders
    names = ["Jan Novák", "Petr Svoboda", "Marie Nováková", "Jana Dvořáková", "Tomáš Černý"]
    name = random.choice(names)
    sender = random.choice(["Martin", "Lucie", "Pavel", "Tereza", "Jakub"])
    date = f"{random.randint(1, 28)}.{random.randint(1, 12)}.2024"
    time = f"{random.randint(8, 18)}:{random.choice(['00', '15', '30', '45'])}"
    phone = f"+420 {random.randint(600, 799)} {random.randint(100, 999)} {random.randint(100, 999)}"
    tracking = f"CP{random.randint(100000000, 999999999)}CZ"
    room = f"A-{random.randint(100, 500)}"
    
    email = template.format(
        name=name,
        sender=sender,
        date=date,
        time=time,
        phone=phone,
        tracking=tracking,
        room=room,
        invoice=f"OBJ-{random.randint(10000, 99999)}"
    )
    
    return email

def main():
    """Generate all emails"""
    print("Generating Czech email database for ML training...")
    
    # Generate sophisticated spam (500)
    print("Generating 500 sophisticated spam emails...")
    for i in range(500):
        email = generate_spam_email(sophisticated=True, index=i)
        with open(f"spam_emails/spam_sophisticated_{i+1:04d}.txt", "w", encoding="utf-8") as f:
            f.write(email)
    
    # Generate common spam (200)
    print("Generating 200 common spam emails...")
    for i in range(200):
        email = generate_spam_email(sophisticated=False, index=i)
        with open(f"spam_emails/spam_common_{i+1:04d}.txt", "w", encoding="utf-8") as f:
            f.write(email)
    
    # Generate sophisticated ham (500)
    print("Generating 500 sophisticated ham emails...")
    for i in range(500):
        email = generate_ham_email(sophisticated=True, index=i)
        with open(f"ham_emails/ham_sophisticated_{i+1:04d}.txt", "w", encoding="utf-8") as f:
            f.write(email)
    
    # Generate common ham (200)
    print("Generating 200 common ham emails...")
    for i in range(200):
        email = generate_ham_email(sophisticated=False, index=i)
        with open(f"ham_emails/ham_common_{i+1:04d}.txt", "w", encoding="utf-8") as f:
            f.write(email)
    
    print("\nDone! Generated:")
    print("- 700 spam emails (500 sophisticated + 200 common)")
    print("- 700 ham emails (500 sophisticated + 200 common)")
    print("Total: 1400 emails for ML training")

if __name__ == "__main__":
    main()
