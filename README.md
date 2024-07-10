Here is a more creative and visually appealing version of your instructions with added emojis:

# 🌐 Multilingual AI Assistant 🤖

## How to Run?

### 🚀 Steps:

1. **Clone the repository**

   ```bash
   Project repo: https://github.com/
   ```

2. **Create a conda environment after opening the repository**

   ```bash
   conda create -n llmapp python=3.8 -y
   ```

   ```bash
   conda activate llmapp
   ```

3. **Install the requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root directory and add your GOOGLE_API_KEY credentials as follows:**

   ```ini
   GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   ```

5. **Run the application**

   ```bash
   streamlit run app.py
   ```

   Now open up your browser and navigate to:

   ```bash
   localhost:8501
   ```

---

### 💻 Tech Stack Used:

- 🐍 Python
- 🌐 Google API
- 📊 Streamlit
- 🤖 PaLM2
- 🎙️ s2t (Speech-to-Text)
- 🗣️ t2s (Text-to-Speech)

---

## 🚀 How to Deploy Streamlit App on EC2 Instance

### 1. **Login to your AWS console and launch an EC2 instance**

### 2. **Run the following commands**

   **Note:** Make sure to do the port mapping to this port: **8501**

   ```bash
   sudo apt update
   ```

   ```bash
   sudo apt-get update
   ```

   ```bash
   sudo apt upgrade -y
   ```

   ```bash
   sudo apt install git curl unzip tar make sudo vim wget -y
   ```

   ```bash
   git clone "Your-repository"
   ```

   ```bash
   sudo apt install python3-pip
   ```

   ```bash
   pip3 install -r requirements.txt
   ```

   **Temporary Running:**

   ```bash
   python3 -m streamlit run app.py
   ```

   **Permanent Running:**

   ```bash
   nohup python3 -m streamlit run app.py &
   ```

   **Note:** Streamlit runs on port: **8501**

---
