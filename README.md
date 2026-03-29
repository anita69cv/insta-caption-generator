# 📸 AI Instagram Caption Generator (Image-Based)

A **Generative AI project** that creates Instagram captions from uploaded images using a combination of **vision models + local LLMs**.

## 🚀 Features
* 🖼️ Upload any image
* 🧠 AI understands image content (BLIP model)
* ✨ Generates creative Instagram captions
* 😄 Includes emojis and hashtags
* ⚡ Runs locally using LM Studio (no API cost)

## 🧠 How It Works
1. User uploads an image
2. Image is processed using a **vision model (BLIP)**
3. The model generates a description of the image
4. Description is sent to a **local LLM (via LM Studio)**
5. AI generates Instagram captions

## 🛠️ Tech Stack
* Python
* Streamlit (UI)
* Transformers (Hugging Face)
* Torch
* LM Studio (Local LLM)

## 📁 Project Structure
insta-caption-generator/
│
├── app.py               # Main logic
├── image_caption.py     # Image → description (BLIP)
├── prompt.py            # Prompt engineering
├── ui.py                # Streamlit UI
├── requirements.txt
└── README.md

## ⚙️ Setup Instructions
### 1. Clone the repository

git clone https://github.com/your-username/insta-caption-generator.git
cd insta-caption-generator
```

---

### 2. Create virtual environment

python -m venv venv

Activate:
* Windows:

venv\Scripts\activate

* Mac/Linux:

source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Setup LM Studio

* Install LM Studio
* Download a model (Recommended: Gemma 1B / Mistral 7B)
* Start local server

### 5. Run the app
streamlit run ui.py


**Input:**
https://github.com/anita69cv/insta-caption-generator/blob/main/images.jpg

**Output:**




