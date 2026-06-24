# Simple Cybersecurity Password Analyzer

A lightweight Python application designed to demonstrate the core principles of defensive programming, password entropy, and user input validation. 

This project serves as a practical, foundational exploration into mitigating basic authentication vulnerabilities.

## 🛠️ Security Features Implemented

1. **Dictionary Attack Mitigation:** The script instantly flags highly common, historically leaked passwords (such as `123456` or `qwerty`) to prevent basic automated credential-guessing attacks.

2. **Complexity & Entropy Evaluation:** Uses conditional logic to programmatically verify structural strength requirements, including:
   - Minimum character length threshold (8 or more characters).
   - Numerical inclusion parsing (0-9).
   - Character casing verification (Uppercase/Lowercase variation).

3. **Dynamic Feedback Loop:** Provides real-time warning logs and computes a final security rating (`STRONG`, `MEDIUM`, or `WEAK`) to encourage secure user behavior.

## 🚀 How To Run Locally

Ensure you have Python installed, then execute the script via your terminal:

```bash
python password_analyzer.py
