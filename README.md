# MIT-AI-Hackathon 2025
# PROJECT: [TRACK 1, CHALLANGE 3]
# TRACK 1: AGENTIC AI FOR DATASET BUILDING
 # Challange 3: Voice Agent for Moving Price Discovery: Build the Kelley Blue Book of Moving Costs

---

# MovePricer – AI-Powered Voice Assistant for Moving Estimates

**MovePricer** is a voice-enabled web platform that acts as your personal moving assistant. It allows users to speak or type queries, gather quotes from vendors, and generate a structured dataset for easy price comparison—all in real time.

## Features

### Voice/Text Agent for Data Collection

* Interact with the AI through **voice or text** using your browser.
* AI prompts users to provide:

  * Moving **route** (e.g., Boston → San Francisco)
  * **Services** required (e.g., packing, loading, insurance)
  * **Estimated delivery time**
  * **Flexibility** in date and load size
* Uses **AssemblyAI** for transcription and **Groq Cloud** for lightning-fast language responses.
* Stores, transcribes, and processes voice input to extract useful quote data.

### Structured Price Comparison Dataset

* Automatically normalizes company responses into a clean, exportable dataset.
* Stores variables like:

  * `Route`
  * `Company Name`
  * `Quote Amount`
  * `Included Services`
  * `Response Timestamp`
* Enables real-time generation of quote lists for comparison.

### Interactive Comparison UI

* Sleek interface to:

  * View collected quotes
  * Sort and filter by cost, services, or route
  * Simulate new requests with updated cities or requirements
* Export data to CSV for external analysis or client presentation.

### Smart AI Agent

* AI responds both **visually** and **verbally** with natural, spoken replies.
* Conversational interface lets you ask:

  * “How much does it cost from NYC to LA?”
  * “Do you include packing services?”
  * “Can I move on the weekend?”
* All replies are spoken aloud and displayed in a chat window.

### Data Persistence

* Uses `localStorage` to remember conversations and results.
* Option to export dataset or clear session data at any time.

### Tech Stack

* **HTML, CSS, JavaScript**
* **AssemblyAI** – Speech-to-text
* **Groq Cloud** – AI language model inference
* **PYTHON 3.13** - BACKEND
* **Web Speech API** – Voice synthesis (Text-to-Speech)
* **LocalStorage** – Client-side data persistence
* **CSV Export** – Downloadable quote table

# HOW IT WORKS:
* There are 2 boxes(for moving route and contact no) fill the boxes either by using the microphone or the text box.
* click on "start price discovery" .
* scroll down to see the result in the collected data section. 
* collected data section is initially empty. It fetches data when information is given on the given two boxes.
* user can save or export all the collected datas to csv by clicking "export csv".
* Lastly, There is an AI agent (scroll down to find the agent) in order to help users and answer to their queries.
  
  ---
 #sample questions you can ask the ai agent:
* i."How much to move a 3-bedroom house from Austin to Denver?"
* 2. "What's the average cost for moving cross-country?"
* 3. "Is it cheaper to move in winter?"
* 4. "What's the best pizza in Chicago?"
* 5. "What's tomorrow's weather forecast?"
* 6. "How long from NYC to LA?"
* 7. "What's your fastest delivery option?"
* viii."what is the cost from Chicago to Nyc".

 The link to the webpage is given below at 'live demo'
---
## LIVE DEMO: https://mit-ai-hackathon-aivoiceagent.netlify.app/

##  Browser Support

* **Firefox** – Microphone permissions must be manually enabled
* **Chrome** – Microphone permissions must be manually enabled
* **Safari** – Limited support for speech recognition

---
# Photos from the Hackathon
i. https://github.com/Deban-H/MIT-AI-Hackathon/blob/main/track1and-itsChallanges.jpg

ii. https://github.com/Deban-H/MIT-AI-Hackathon/blob/main/Photo1-SpeakersSession-fromTheHackathon.png

iii. https://github.com/Deban-H/MIT-AI-Hackathon/blob/main/Photo2-fromTheHackathon.png

## Privacy Notice

This project is for demonstration purposes. No real user data is sent to vendors. All inputs are simulated and handled client-side.

---


