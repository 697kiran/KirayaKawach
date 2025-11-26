# 🛡️ KirayaKawach (Rent Shield)

**Building Trust in Bharat’s Rental Market with AI Forensics.**

> *Winner/Participant of the Build for Bharat Innovation Challenge*

## 📌 Overview
**KirayaKawach** (formerly Mera Nivas) is a lightweight, AI-powered forensic engine designed to detect digital forgery in rental documents. As real estate transactions in Tier 2/3 cities move to WhatsApp and digital channels, the risk of fake rent agreements, edited payment screenshots, and forged IDs is skyrocketing.

KirayaKawach solves this by combining **Error Level Analysis (ELA)** to spot "invisible" pixel tampering and **Multilingual OCR** (Hindi/English) to verify text consistency instantly.

---

## 🚀 Key Features

* **🕵️ Forensic ELA Scan:** Detects if an image has been "Photoshopped" or digitally altered by analyzing compression artifacts.
* **🇮🇳 Built for Bharat:** Native support for **Hindi and English** text extraction using deep learning OCR.
* **🔒 Privacy First:** The entire engine is optimized to run **locally on a CPU**, ensuring sensitive user documents never leave the device.
* **⚡ Lightweight & Fast:** No heavy GPUs required. Runs efficiently on standard hardware.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Computer Vision:** OpenCV (`cv2`), NumPy (For pixel-level forensic analysis)
* **OCR Engine:** EasyOCR (PyTorch backend)
* **Validation:** Pydantic (For structured data outputs)
* **Frontend (Future):** React/Streamlit (Planned)

---

## ⚙️ Installation Guide

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/697kiran/KirayaKawach.git](https://github.com/697kiran/KirayaKawach.git)
cd KirayaKawach
