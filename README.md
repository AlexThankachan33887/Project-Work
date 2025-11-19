# 🕷️ Project-Work: Advanced Web Scraping System

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/scrapy-2.5%2B-green)](https://scrapy.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.0%2B-yellow)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success)](https://github.com/AlexThankachan33887/Project-Work)

**A robust, modular, and production-ready web scraping system engineered for extracting structured data from dynamic websites with cloud-native deployment capabilities.**

[Features](#-key-features) • [Installation](#-installation) • [Usage](#-usage-guide) • [Documentation](#-documentation) • [Contributing](#-contributing)

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
  - [Prerequisites](#prerequisites)
  - [Quick Start](#quick-start)
  - [Docker Setup](#docker-setup)
- [Project Structure](#-project-structure)
- [Usage Guide](#-usage-guide)
  - [Basic Usage](#basic-usage)
  - [Advanced Usage](#advanced-usage)
  - [Selenium Scraper](#selenium-scraper)
  - [Scrapy Spider](#scrapy-spider)
- [Configuration](#-configuration)
- [Data Pipeline](#-data-pipeline)
- [API Reference](#-api-reference)
- [Performance Optimization](#-performance-optimization)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Best Practices](#-best-practices)
- [Contributing](#-contributing)
- [Testing](#-testing)
- [Roadmap](#-roadmap)
- [FAQ](#-faq)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🌟 Overview

**Project-Work** is a sophisticated, enterprise-grade web scraping solution designed to automate data extraction from even the most complex and dynamic websites. Built with Python and leveraging the power of both Scrapy and Selenium, this system delivers structured, clean data ready for immediate integration into analytics pipelines, machine learning workflows, and business intelligence platforms.

### Why Project-Work?

- **🚀 Production-Ready**: Battle-tested architecture with error handling and recovery
- **📊 Data Quality**: Advanced data validation and cleaning pipelines
- **☁️ Cloud-Native**: Designed for deployment on AWS, GCP, Azure, or any cloud platform
- **🔄 Scalable**: Handles everything from small batches to massive data collection operations
- **🛡️ Resilient**: Built-in retry mechanisms, error logging, and graceful degradation
- **🎯 Focused**: Initially developed for real estate data (Bayut), easily extensible to any domain

---

## ✨ Key Features

### Core Capabilities

- **🔀 Dual-Engine Architecture**: Combines Scrapy's speed with Selenium's dynamic content handling
- **🌐 JavaScript Support**: Full rendering of SPA and AJAX-heavy websites
- **📝 Multiple Output Formats**: Export to JSON, CSV, XML, or databases
- **🔄 Automatic Retries**: Intelligent retry logic with exponential backoff
- **🎭 Anti-Detection**: User agent rotation, proxy support, and header randomization
- **📊 Data Validation**: Built-in schema validation and data cleaning
- **⚡ Concurrent Processing**: Multi-threaded scraping for maximum efficiency
- **📈 Progress Tracking**: Real-time monitoring and detailed logging
- **🗄️ Database Integration**: Direct export to MongoDB, PostgreSQL, MySQL
- **🔐 Proxy Support**: Rotating proxies to avoid IP bans
- **📧 Notifications**: Email/Slack alerts on job completion or errors
- **🧪 Testing Suite**: Comprehensive unit and integration tests

### Advanced Features

- **Custom Middleware**: Extensible middleware system for request/response processing
- **Pipeline Processing**: Multiple configurable data processing pipelines
- **Rate Limiting**: Intelligent throttling to respect server resources
- **Session Management**: Maintains cookies and sessions across requests
- **Authentication**: Support for login-required websites
- **Screenshot Capture**: Automated screenshot capabilities for debugging
- **Data Deduplication**: Automatic removal of duplicate entries
- **Incremental Scraping**: Only scrape new or updated content

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Web Scraping System                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐         ┌──────────────┐                 │
│  │   Selenium   │         │    Scrapy    │                 │
│  │   Scraper    │◄───────►│    Engine    │                 │
│  └──────┬───────┘         └──────┬───────┘                 │
│         │                         │                          │
│         └────────┬────────────────┘                          │
│                  │                                           │
│         ┌────────▼────────┐                                 │
│         │  Data Pipeline  │                                 │
│         │   Processing    │                                 │
│         └────────┬────────┘                                 │
│                  │                                           │
│         ┌────────▼────────┐                                 │
│         │  Data Storage   │                                 │
│         │  JSON/CSV/DB    │                                 │
│         └─────────────────┘                                 │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+** (Python 3.9+ recommended)
- **pip** (Python package manager)
- **Google Chrome/Chromium** (latest stable version)
- **ChromeDriver** (matching your Chrome version)
- **Git** (for cloning the repository)
- **Virtual Environment** (optional but recommended)

#### System Requirements

- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: Minimum 4GB (8GB+ recommended for large-scale scraping)
- **Storage**: 1GB+ free space
- **Network**: Stable internet connection

### Quick Start

#### 1. Clone the Repository

```bash
git clone https://github.com/AlexThankachan33887/Project-Work.git
cd Project-Work
```

#### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Or install manually
pip install scrapy selenium beautifulsoup4 pandas requests lxml
pip install fake-useragent scrapy-user-agents
pip install pymongo psycopg2-binary  # For database support
pip install python-dotenv  # For environment variables
```

#### 4. Configure ChromeDriver

**Option A: Automatic (Recommended)**
```bash
pip install webdriver-manager
```

**Option B: Manual**
```bash
# Download ChromeDriver
# Visit: https://chromedriver.chromium.org/downloads
# Choose version matching your Chrome browser

# On Linux/macOS
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

# On Windows
# Add ChromeDriver.exe to your PATH or project directory
```

#### 5. Verify Installation

```bash
python -c "import scrapy; import selenium; print('Installation successful!')"
```

### Docker Setup

For containerized deployment:

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$(wget -q -O - chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

CMD ["python", "selenium_scraper.py"]
```

**Build and Run:**
```bash
docker build -t web-scraper .
docker run -v $(pwd)/data:/app/data web-scraper
```

---

## 📁 Project Structure

```
Project-Work/
│
├── 📄 README.md                      # This file
├── 📄 requirements.txt               # Python dependencies
├── 📄 .env.example                   # Environment variables template
├── 📄 .gitignore                     # Git ignore rules
├── 📄 LICENSE                        # MIT License
│
├── 📂 intern/                        # Scrapy project directory
│   ├── scrapy.cfg                    # Scrapy deployment config
│   └── intern/
│       ├── __init__.py
│       ├── items.py                  # Data model definitions
│       ├── middlewares.py            # Custom middlewares
│       ├── pipelines.py              # Data processing pipelines
│       ├── settings.py               # Scrapy configuration
│       │
│       ├── 📂 spiders/               # Spider implementations
│       │   ├── __init__.py
│       │   ├── Bayut_102070392065.py # Bayut property spider
│       │   └── base_spider.py        # Base spider class
│       │
│       ├── 📂 utils/                 # Utility functions
│       │   ├── __init__.py
│       │   ├── validators.py         # Data validation
│       │   ├── cleaners.py           # Data cleaning
│       │   └── formatters.py         # Data formatting
│       │
│       └── 📂 data/                  # Output data directory
│           ├── bayut_data.json
│           ├── data.csv
│           └── formatted_data.json
│
├── 📂 scrapers/                      # Standalone scrapers
│   ├── __init__.py
│   ├── selenium_scraper.py           # Selenium-based scraper
│   ├── pages.py                      # Page object models
│   └── base_scraper.py               # Base scraper class
│
├── 📂 config/                        # Configuration files
│   ├── __init__.py
│   ├── settings.py                   # Global settings
│   └── logging.conf                  # Logging configuration
│
├── 📂 tests/                         # Test suite
│   ├── __init__.py
│   ├── test_scrapers.py
│   ├── test_pipelines.py
│   └── test_utils.py
│
├── 📂 scripts/                       # Utility scripts
│   ├── createfile.py                 # File creation utility
│   ├── setup.sh                      # Setup script
│   └── deploy.sh                     # Deployment script
│
├── 📂 docs/                          # Documentation
│   ├── API.md                        # API documentation
│   ├── CONTRIBUTING.md               # Contribution guide
│   └── DEPLOYMENT.md                 # Deployment guide
│
└── 📂 data/                          # Data directory
    ├── urls.csv                      # Input URLs
    ├── output/                       # Scraped data output
    └── logs/                         # Log files
```

---

## 💻 Usage Guide

### Basic Usage

#### Quick Start Example

```bash
# Run the Selenium scraper
python selenium_scraper.py

# Run the Scrapy spider
cd intern
scrapy crawl Bayut_102070392065 -o ../data/output/properties.json
```

### Advanced Usage

#### 1. Scraping with Custom URLs

Create a `urls.csv` file:
```csv
url,category,priority
https://www.bayut.com/property/details-12345.html,apartment,high
https://www.bayut.com/property/details-67890.html,villa,medium
```

Run the scraper:
```bash
python selenium_scraper.py --input urls.csv --output data/results.json
```

#### 2. Using Different Output Formats

```bash
# JSON output
scrapy crawl Bayut_102070392065 -o output.json

# CSV output
scrapy crawl Bayut_102070392065 -o output.csv

# JSON Lines
scrapy crawl Bayut_102070392065 -o output.jl

# XML output
scrapy crawl Bayut_102070392065 -o output.xml
```

#### 3. Filtering and Pagination

```python
# In your spider
class BayutSpider(scrapy.Spider):
    name = 'bayut'
    
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 100,  # Stop after 100 pages
        'CLOSESPIDER_ITEMCOUNT': 1000,  # Stop after 1000 items
    }
    
    def start_requests(self):
        # Add filters to URL
        url = 'https://www.bayut.com/for-rent/property/dubai/?price_max=100000'
        yield scrapy.Request(url, callback=self.parse)
```

### Selenium Scraper

#### Basic Selenium Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_property(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        
        # Wait for content to load
        wait = WebDriverWait(driver, 10)
        title = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'property-title'))
        ).text
        
        # Extract data
        data = {
            'title': title,
            'price': driver.find_element(By.CLASS_NAME, 'price').text,
            'location': driver.find_element(By.CLASS_NAME, 'location').text
        }
        
        return data
        
    finally:
        driver.quit()

# Usage
property_data = scrape_property('https://example.com/property/123')
print(property_data)
```

### Scrapy Spider

#### Custom Spider Example

```python
import scrapy
from intern.items import PropertyItem

class CustomSpider(scrapy.Spider):
    name = 'custom_spider'
    allowed_domains = ['example.com']
    start_urls = ['https://example.com/properties']
    
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS': 8,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    def parse(self, response):
        # Extract property listings
        for property in response.css('div.property-card'):
            item = PropertyItem()
            item['title'] = property.css('h2.title::text').get()
            item['price'] = property.css('span.price::text').get()
            item['location'] = property.css('span.location::text').get()
            
            # Follow detail page
            detail_url = property.css('a.details::attr(href)').get()
            if detail_url:
                yield response.follow(detail_url, self.parse_details, 
                                     meta={'item': item})
        
        # Pagination
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
    
    def parse_details(self, response):
        item = response.meta['item']
        item['description'] = response.css('div.description::text').get()
        item['bedrooms'] = response.css('span.bedrooms::text').get()
        item['bathrooms'] = response.css('span.bathrooms::text').get()
        yield item
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file:

```env
# Database Configuration
MONGO_URI=mongodb://localhost:27017/
MONGO_DATABASE=scraping_db

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=scraping_db
POSTGRES_USER=username
POSTGRES_PASSWORD=password

# Proxy Settings
USE_PROXY=true
PROXY_URL=http://proxy.example.com:8080
PROXY_USERNAME=user
PROXY_PASSWORD=pass

# API Keys
SCRAPING_API_KEY=your_api_key_here

# Notifications
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
EMAIL_SENDER=noreply@example.com
EMAIL_RECIPIENT=admin@example.com

# Scraping Settings
MAX_RETRIES=3
DOWNLOAD_DELAY=2
CONCURRENT_REQUESTS=16
```

### Scrapy Settings

Edit `intern/intern/settings.py`:

```python
# Crawl responsibly
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 16
DOWNLOAD_DELAY = 2

# User Agent Rotation
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    # Add more user agents
]

# Middleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'intern.middlewares.ProxyMiddleware': 750,
}

# Pipelines
ITEM_PIPELINES = {
    'intern.pipelines.ValidationPipeline': 100,
    'intern.pipelines.CleaningPipeline': 200,
    'intern.pipelines.DuplicationPipeline': 300,
    'intern.pipelines.DatabasePipeline': 400,
}

# AutoThrottle
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0

# Logging
LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/scrapy.log'
```

---

## 🔄 Data Pipeline

### Pipeline Architecture

```python
# intern/intern/pipelines.py

class ValidationPipeline:
    """Validates scraped data against schema"""
    def process_item(self, item, spider):
        if not item.get('title'):
            raise DropItem(f"Missing title in {item}")
        if not item.get('price'):
            raise DropItem(f"Missing price in {item}")
        return item

class CleaningPipeline:
    """Cleans and normalizes data"""
    def process_item(self, item, spider):
        # Remove extra whitespace
        item['title'] = ' '.join(item['title'].split())
        
        # Normalize price
        price = item['price'].replace(',', '').replace('AED', '').strip()
        item['price'] = float(price)
        
        return item

class DuplicationPipeline:
    """Removes duplicate items"""
    def __init__(self):
        self.ids_seen = set()
    
    def process_item(self, item, spider):
        item_id = item.get('property_id')
        if item_id in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item_id}")
        else:
            self.ids_seen.add(item_id)
            return item

class DatabasePipeline:
    """Saves items to database"""
    def open_spider(self, spider):
        # Initialize database connection
        self.client = pymongo.MongoClient(settings.MONGO_URI)
        self.db = self.client[settings.MONGO_DATABASE]
    
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        self.db[spider.name].insert_one(dict(item))
        return item
```

---

## 📚 API Reference

### Scraper Classes

#### SeleniumScraper

```python
from scrapers.selenium_scraper import SeleniumScraper

scraper = SeleniumScraper(
    headless=True,
    timeout=30,
    use_proxy=False
)

# Scrape single URL
data = scraper.scrape_url('https://example.com')

# Scrape multiple URLs
urls = ['https://example.com/page1', 'https://example.com/page2']
results = scraper.scrape_batch(urls)

# Save results
scraper.save_results(results, 'output.json')
```

#### Spider Methods

```python
class MySpider(scrapy.Spider):
    def start_requests(self):
        """Generate initial requests"""
        pass
    
    def parse(self, response):
        """Parse response and extract data"""
        pass
    
    def parse_details(self, response):
        """Parse detailed page"""
        pass
```

---

## 🚀 Performance Optimization

### Tips for Faster Scraping

1. **Use Concurrent Requests**
```python
CONCURRENT_REQUESTS = 32  # Increase for faster scraping
```

2. **Disable Unnecessary Middleware**
```python
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
}
```

3. **Use Scrapy Redis for Distributed Scraping**
```bash
pip install scrapy-redis
```

4. **Implement Caching**
```python
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 86400  # 24 hours
```

---

## 🌐 Deployment

### AWS Lambda Deployment

```python
# lambda_handler.py
import json
from selenium_scraper import scrape_properties

def lambda_handler(event, context):
    urls = event.get('urls', [])
    results = scrape_properties(urls)
    
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }
```

### Docker Compose

```yaml
version: '3.8'

services:
  scraper:
    build: .
    volumes:
      - ./data:/app/data
    environment:
      - MONGO_URI=mongodb://mongo:27017/
    depends_on:
      - mongo
  
  mongo:
    image: mongo:latest
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue: ChromeDriver version mismatch**
```bash
# Solution: Use webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
```

**Issue: IP blocked by website**
```python
# Solution: Use rotating proxies
ROTATING_PROXY_LIST = [
    'http://proxy1.com:8080',
    'http://proxy2.com:8080',
]
```

**Issue: Memory leak in long-running scrapes**
```python
# Solution: Implement periodic restarts
CLOSESPIDER_PAGECOUNT = 1000
```

---

## 📋 Best Practices

1. **Always respect robots.txt**
2. **Implement rate limiting**
3. **Use user agent rotation**
4. **Handle errors gracefully**
5. **Log all activities**
6. **Validate data before storage**
7. **Test on small datasets first**
8. **Monitor resource usage**
9. **Keep dependencies updated**
10. **Document your spiders**

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/

# Check code style
flake8 .
black --check .
```

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=intern --cov-report=html

# Run specific test
pytest tests/test_scrapers.py::test_bayut_spider
```

---

## 🗺️ Roadmap

- [ ] Add support for more e-commerce sites
- [ ] Implement GraphQL API
- [ ] Add ML-based data extraction
- [ ] Build web UI for monitoring
- [ ] Add support for browser fingerprinting evasion
- [ ] Implement CAPTCHA solving integration
- [ ] Create Docker orchestration templates

---

## ❓ FAQ

**Q: Is this legal?**  
A: Web scraping legality varies. Always check robots.txt and terms of service.

**Q: How do I avoid getting blocked?**  
A: Use proxies, rotate user agents, implement delays, and respect rate limits.

**Q: Can I scrape JavaScript-heavy sites?**  
A: Yes, use the Selenium scraper for dynamic content.

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Alex Thankachan**

- GitHub: [@AlexThankachan33887](https://github.com/AlexThankachan33887)
- LinkedIn: [Connect with me](https://linkedin.com/in/codered7)
- Email: alexthankachan95@gmail.com

---

## 🙏 Acknowledgments

- [Scrapy Documentation](https://docs.scrapy.org/)
- [Selenium WebDriver](https://www.selenium.dev/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/)
- All open-source contributors

---

## 📞 Support

- 📧 Email: support@project-work.com
- 💬 Discussions: [GitHub Discussions](https://github.com/AlexThankachan33887/Project-Work/discussions)
- 🐛 Issues: [GitHub Issues](https://github.com/AlexThankachan33887/Project-Work/issues)
- 📖 Documentation: [Full Docs](https://project-work.readthedocs.io)

---

**⭐ Star this repo if you find it helpful! ⭐**

Made with ❤️ by [Alex Thankachan](https://github.com/AlexThankachan33887)