# MIT-AI-Hackathon
# PROJECT: [TRACK 1, CHALLANGE 3]
# TRACK 1: AGENTIC AI FOR DATASET BUILDING
 # Challange 3: Voice Agent for Moving Price Discovery: Build the Kelley Blue Book of Moving Costs

---

# 🚚 MovePricer – AI-Powered Voice Assistant for Moving Estimates

**MovePricer** is a cutting-edge, voice-enabled web platform that acts as your personal moving assistant. It allows users to speak or type queries, gather quotes from vendors, and generate a structured dataset for easy price comparison—all in real time.

## Features

### 🎙️ Voice/Text Agent for Data Collection

* Interact with the AI through **voice or text** using your browser.
* AI prompts users to provide:

  * Moving **route** (e.g., Boston → San Francisco)
  * **Services** required (e.g., packing, loading, insurance)
  * **Estimated delivery time**
  * **Flexibility** in date and load size
* Uses **AssemblyAI** for transcription and **Groq Cloud** for lightning-fast language responses.
* Stores, transcribes, and processes voice input to extract useful quote data.

### 📊 Structured Price Comparison Dataset

* Automatically normalizes company responses into a clean, exportable dataset.
* Stores variables like:

  * `Route`
  * `Company Name`
  * `Quote Amount`
  * `Included Services`
  * `Response Timestamp`
* Enables real-time generation of quote lists for comparison.

### 🖥️ Interactive Comparison UI

* Sleek interface to:

  * View collected quotes
  * Sort and filter by cost, services, or route
  * Simulate new requests with updated cities or requirements
* Export data to CSV for external analysis or client presentation.

### 🧠 Smart AI Agent

* AI responds both **visually** and **verbally** with natural, spoken replies.
* Conversational interface lets you ask:

  * “How much does it cost from NYC to LA?”
  * “Do you include packing services?”
  * “Can I move on the weekend?”
* All replies are spoken aloud and displayed in a chat window.

### 💾 Data Persistence

* Uses `localStorage` to remember conversations and results.
* Option to export dataset or clear session data at any time.

### ⚙️ Tech Stack

* **HTML, CSS, JavaScript**
* **AssemblyAI** – Speech-to-text
* **Groq Cloud** – AI language model inference
* **PYTHON 3.13** - BACKEND
* **Web Speech API** – Voice synthesis (Text-to-Speech)
* **LocalStorage** – Client-side data persistence
* **CSV Export** – Downloadable quote table


---
## LIVE DEMO:

## 📌 Browser Support

* ✅ **Firefox** – Microphone permissions must be manually enabled
* ✅ **Chrome** – Microphone permissions must be manually enabled
* ⚠️ **Safari** – Limited support for speech recognition

---

## 🔐 Privacy Notice

This project is for demonstration purposes. No real user data is sent to vendors. All inputs are simulated and handled client-side.

---


