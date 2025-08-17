# Playwright Python Test Automation Framework

Cross-platform test framework built with **Python**, **Playwright**, and **pytest**. The project follows the **Page Object Model** pattern and integrates with **Allure** for rich reporting.

## 🚀 Supported Platforms
- Web
- Mobile Web
- Android (emulated)
- iOS (emulated)
- API
- Performance

## 📦 Installation
```bash
pip install -r requirements.txt
python -m playwright install
```

## 🏗️ Structure
```
.
├── pages/                 # Page objects
├── tests/
│   ├── web/               # Web tests
│   ├── mobile_web/        # Mobile web tests
│   ├── android/           # Android emulation tests
│   ├── ios/               # iOS emulation tests
│   ├── api/               # API tests
│   └── performance/       # Simple performance checks
├── utils/                 # Configuration and factories
└── pytest.ini             # Pytest configuration
```

## ▶️ Running Tests
```bash
pytest
```

Run a specific suite:
```bash
pytest tests/web
```

## 📊 Allure Reports
Generate and open a report:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## ⚙️ Configuration
Environment variables can override defaults:
```bash
export BASE_URL="https://example.com"
export HEADLESS="false"
```

## 📄 License
MIT
