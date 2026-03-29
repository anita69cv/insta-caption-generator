# 📸 AI Instagram Caption Generator (Image-Based)

A **Generative AI project** that creates Instagram captions from uploaded images using a combination of **vision models + local LLMs**.

---

## 🚀 Features

* 🖼️ Upload any image
* 🧠 AI understands image content (BLIP model)
* ✨ Generates creative Instagram captions
* 😄 Includes emojis and hashtags
* ⚡ Runs locally using LM Studio (no API cost)

---

## 🧠 How It Works

1. User uploads an image
2. Image is processed using a **vision model (BLIP)**
3. The model generates a description of the image
4. Description is sent to a **local LLM (via LM Studio)**
5. AI generates Instagram captions

---

## 🛠️ Tech Stack

* Python
* Streamlit (UI)
* Transformers (Hugging Face)
* Torch
* LM Studio (Local LLM)

---

## 📁 Project Structure

```
insta-caption-generator/
│
├── app.py               # Main logic
├── image_caption.py     # Image → description (BLIP)
├── prompt.py            # Prompt engineering
├── ui.py                # Streamlit UI
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/insta-caption-generator.git
cd insta-caption-generator
```

---

### 2. Create virtual environment

```
python -m venv venv
```

Activate:

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup LM Studio

* Install LM Studio
* Download a model (Recommended: Gemma 1B / Mistral 7B)
* Start local server

```
http://127.0.0.1:1234
```

---

### 5. Run the app

```
streamlit run ui.py
```

---

## 🎯 Example Output

**Input:** Image of a dog at the beach

**Output:**

* Living my best paw-some life 🐶🌊 #DogLife
* Sandy paws, happy heart 🐾✨ #BeachVibes
* Sun, sea, and wagging tails ☀️🐕

---

## ⚡ Performance

* Works locally (no cloud cost)
* Faster with smaller models (Gemma 1B)
* First run may take time (model download)

---

## 🔥 Future Improvements

* 🎨 Better UI design
* 🖼️ Support multiple images
* 🤖 Use advanced models (LLaVA / BLIP-2)
* 🌐 Deploy online

---

## 💡 What I Learned

* Building multimodal AI systems
* Working with local LLMs
* Prompt engineering
* Streamlit app development

---

## 📌 Author

Your Name

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
