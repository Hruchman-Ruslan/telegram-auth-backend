# Telegram Auth Backend & Frontend

Mini-site for Telegram authorization with 2FA support.

---

## 🚀 Running the Project Locally

### 1. Clone the repository

```bash
git clone <REPO_URL>
cd <REPO_FOLDER>
```

### 2. Create a Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

### 3 Install dependencies

```bash
pip install -r requirements.txt
```

### 4 Add your Telegram API keys:

```bash
API_ID=<your API_ID>
API_HASH=<your API_HASH>
```

### 5 Get your API_ID and API_HASH from my.telegram.org

### 6 Run the server

```bash
uvicorn app.main:app --reload
```

Sessions & Logs

Authorization logs and errors are stored in auth.log in the root folder.

User session files are stored in:

app/sessions_private/
