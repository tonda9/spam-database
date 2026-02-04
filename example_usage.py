#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example script demonstrating how to load and use the Czech spam/ham email database
"""

import os
import glob
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

def load_emails():
    """Load all emails from the database"""
    spam_emails = []
    ham_emails = []
    
    # Load spam emails
    for filepath in sorted(glob.glob("spam_emails/*.txt")):
        with open(filepath, "r", encoding="utf-8") as f:
            spam_emails.append(f.read())
    
    # Load ham emails
    for filepath in sorted(glob.glob("ham_emails/*.txt")):
        with open(filepath, "r", encoding="utf-8") as f:
            ham_emails.append(f.read())
    
    return spam_emails, ham_emails

def prepare_dataset(spam_emails, ham_emails):
    """Prepare dataset for ML training"""
    data = []
    
    # Add spam emails
    for email in spam_emails:
        data.append({"text": email, "label": 1})  # 1 = spam
    
    # Add ham emails
    for email in ham_emails:
        data.append({"text": email, "label": 0})  # 0 = ham
    
    df = pd.DataFrame(data)
    
    # Shuffle the data
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return df

def train_simple_model(df):
    """Train a simple Naive Bayes classifier"""
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
    )
    
    # Vectorize text
    vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # Train model
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)
    
    # Predict
    y_pred = model.predict(X_test_vec)
    
    return model, vectorizer, y_test, y_pred

def main():
    print("=" * 60)
    print("Czech Spam Email Database - Example Usage")
    print("=" * 60)
    
    # Load emails
    print("\n1. Loading emails...")
    spam_emails, ham_emails = load_emails()
    print(f"   ✓ Loaded {len(spam_emails)} spam emails")
    print(f"   ✓ Loaded {len(ham_emails)} ham emails")
    print(f"   ✓ Total: {len(spam_emails) + len(ham_emails)} emails")
    
    # Show sample emails
    print("\n2. Sample emails:")
    print("\n   SPAM example:")
    print("   " + "-" * 56)
    print("   " + spam_emails[0].replace("\n", "\n   "))
    
    print("\n   HAM example:")
    print("   " + "-" * 56)
    print("   " + ham_emails[0].replace("\n", "\n   "))
    
    # Prepare dataset
    print("\n3. Preparing dataset...")
    df = prepare_dataset(spam_emails, ham_emails)
    print(f"   ✓ Dataset shape: {df.shape}")
    print(f"   ✓ Label distribution:\n{df['label'].value_counts()}")
    
    # Train model
    print("\n4. Training simple classifier...")
    model, vectorizer, y_test, y_pred = train_simple_model(df)
    
    # Evaluate
    print("\n5. Model evaluation:")
    print(f"   Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\n   Classification Report:")
    report = classification_report(y_test, y_pred, target_names=["Ham", "Spam"])
    for line in report.split("\n"):
        print("   " + line)
    
    # Test on custom examples
    print("\n6. Testing on custom examples:")
    
    test_examples = [
        "Výhra 100000 Kč! Klikni zde!",
        "Ahoj, jak se máš? Půjdeme zítra na kávu?",
        "Váš účet byl zablokován. Ověřte na http://phishing.com",
        "Dobrý den, zasíláme fakturu v příloze. S pozdravem"
    ]
    
    for example in test_examples:
        example_vec = vectorizer.transform([example])
        prediction = model.predict(example_vec)[0]
        label = "SPAM" if prediction == 1 else "HAM"
        print(f"\n   Text: {example}")
        print(f"   Prediction: {label}")
    
    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)

if __name__ == "__main__":
    main()
