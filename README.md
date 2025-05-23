
# AI-Enhanced Playwright + Pytest Hybrid Framework (Python)

This is a complete hybrid automation framework that combines:
- **Playwright** for UI automation
- **Pytest** for test running
- **Requests** for API testing
- **OpenCV** for visual comparisons
- **Transformers** and **Sentence Transformers** for AI-based smart locators
- **HTML and Allure reporting**
- **Mock API test support**
- Clean modular structure with Page Object Model (POM)

---

## ✅ Setup Instructions

### 1. Install Python

Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)

**During installation**, check:
```
☑ Add Python to PATH
```

Then install.

---
## Recommended VS Code Extensions

The following VS Code extensions can improve your development experience while working on this project:

* **Python** by **Microsoft**: Provides syntax highlighting, debugging, and code completion for Python.
* **Playwright Test for VSCode** by **Playwright**: Provides syntax highlighting, code completion, and debugging for Playwright tests.
* **Pylance** by **Microsoft**: Provides advanced code completion, debugging, and refactoring for Python.
* **Code Runner** by **Jun Han**: Allows you to run your tests and scripts with a single click.
* **Test Explorer** by **Microsoft**: Provides a UI for running and debugging your tests.

These extensions can help you write, run, and debug your tests more efficiently.

---
### 2. Create and Activate Virtual Environment

Open a terminal inside the project folder:

```bash
python -m venv venv
```

Activate it:

- Windows:
```bash
venv\Scripts\activate
```

- macOS/Linux:
```bash
source venv/bin/activate
```

---

### 3. Install All Dependencies

```bash
pip install -r requirements.txt
```
pip install playwright
---

### 4. Install Playwright Browsers

```bash
playwright install
```

---

## ▶️ Run Tests

### UI Tests
```bash
pytest tests/ui/
```

### API Tests
```bash
pytest tests/api/
```

### Mock API Test
```bash
pytest tests/mocks/
```

---

## 📊 Reports

### HTML Report
```bash
pytest --html=reports/test_report.html
```

### Allure Report

Make sure Allure is installed. Install via Scoop (on Windows):

```bash
scoop install allure
```

Then run:

```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## Features Overview

### Page Object Model

Example: `pages/login_page.py`

```python
login = LoginPage(page)
login.login("user", "pass")
```

### AI Utilities

- `ai_utils/visual_comparator.py` — compare screenshots
- `ai_utils/smart_locator.py` — suggest selectors using NLP

### Step Generator

Add readable logs using:

```python
from utils.steps_generator import generate_step
generate_step("Login success validated", True)
```

---

## Folder Structure

```
├── ai_utils/               # AI-based utilities (NLP, image comparison)
├── pages/                  # Page Object files
├── tests/
│   ├── api/                # API tests
│   ├── mocks/              # Mock API tests
│   └── ui/                 # UI tests
├── utils/                  # Helper modules
├── data/                   # Test data if any
├── reports/                # HTML and Allure test reports
├── requirements.txt
├── pytest.ini
├── conftest.py
└── README.md
```

---

## Coming Up

- Docker integration
- CI (GitHub Actions / Azure Pipelines)
- Slack/email notification hooks

---

Happy Testing!
#   f u l l _ p l a y w r i g h t _ a i _ f r a m e w o r k  
 