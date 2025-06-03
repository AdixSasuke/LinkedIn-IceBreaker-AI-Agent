# 🧊 Ice Breaker - AI-Powered LinkedIn Profile Analyzer

An intelligent ice breaker generator that analyzes LinkedIn profiles and creates personalized conversation starters using Google's Gemini AI.

## ✨ Features

-   🔍 **LinkedIn Profile Scraping**: Extracts comprehensive profile information
-   🤖 **AI-Powered Analysis**: Uses Google Gemini AI for intelligent insights
-   💬 **Personalized Ice Breakers**: Generates conversation starters based on profile data
-   🎯 **Professional Networking**: Perfect for sales, recruiting, or networking
-   🚀 **Easy to Use**: Simple function call with LinkedIn URL

## 🛠️ Installation

### Prerequisites

-   Python 3.11 or higher
-   LinkedIn profile URLs
-   Google Gemini API key
-   Scrapin.io API key (for LinkedIn data extraction)

### Setup

1. **Clone the repository**

    ```cmd
    git clone https://github.com/AdixSasuke/LinkedIn-IceBreaker-AI-Agent
    cd ice_breaker
    ```

2. **Create a virtual environment**

    ```cmd
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. **Install dependencies**

    ```cmd
    pip install -r requirements.txt
    ```

4. **Configure environment variables**

    Create a `.env` file in the project root:

    ```properties
    GEMINI_API_KEY=your_gemini_api_key_here
    SCRAPIN_API_KEY=your_scrapin_api_key_here
    ```

    **Getting API Keys:**

    - **Gemini API**: Get your free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
    - **Scrapin API**: Sign up at [Scrapin.io](https://scrapin.io/) for LinkedIn data extraction

## 🚀 Usage

### Basic Usage

```python
from ice_breaker import ice_breaker_with

# Generate ice breaker for a LinkedIn profile
linkedin_url = "https://www.linkedin.com/in/username/"
ice_breaker_message = ice_breaker_with(linkedin_url)
print(ice_breaker_message)
```

### Command Line Usage

```cmd
python ice_breaker.py
```

## 📋 Example Output

```
**Summary:**
John is a seasoned software engineer with 8+ years of experience in full-stack development, currently working as a Senior Developer at TechCorp. He's passionate about building scalable web applications and has recently been diving deep into machine learning and AI technologies.

**Interesting Facts:**
1. John recently completed a marathon in under 4 hours - you could ask him about his training routine or favorite running routes!
2. He's been contributing to an open-source project that helps developers optimize database queries - a great conversation starter about his technical interests and community involvement.
```

## 🏗️ Project Structure

```
ice_breaker/
├── ice_breaker.py          # Main application file
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── README.md             # This file
└── third_parties/
    ├── __init__.py
    └── linkedin.py       # LinkedIn scraping functionality
```

## 🔧 Configuration

### Environment Variables

| Variable          | Description                          | Required |
| ----------------- | ------------------------------------ | -------- |
| `GEMINI_API_KEY`  | Google Gemini AI API key             | Yes      |
| `SCRAPIN_API_KEY` | Scrapin.io API key for LinkedIn data | Yes      |

### AI Model Settings

The application uses `gemini-1.5-flash` model with:

-   **Temperature**: 0.7 (balanced creativity)
-   **Output**: Structured summary + 2 interesting facts

## 🔍 How It Works

1. **Profile Extraction**: Scrapes LinkedIn profile data using Scrapin.io API
2. **Data Processing**: Cleans and structures the profile information
3. **AI Analysis**: Sends data to Google Gemini for intelligent analysis
4. **Ice Breaker Generation**: Creates personalized conversation starters

## 🛡️ Privacy & Ethics

-   Only processes publicly available LinkedIn information
-   Respects LinkedIn's terms of service
-   Uses ethical AI practices for content generation
-   No personal data is stored permanently

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

**API Key Errors**

-   Ensure your `.env` file is in the project root
-   Verify your API keys are valid and active
-   Check API quotas and usage limits

**LinkedIn Scraping Issues**

-   Verify the LinkedIn URL format is correct
-   Check Scrapin.io API status and limits
-   Ensure the profile is publicly accessible

**Model Errors**

-   Confirm `gemini-1.5-flash` model availability
-   Check your Gemini API quota
-   Verify internet connectivity

### Getting Help

1. Review API documentation for Gemini and Scrapin.io
2. Create a new issue with detailed error information

## 📊 Dependencies

-   `langchain` - LLM framework and orchestration
-   `langchain-google-genai` - Google Gemini integration
-   `requests` - HTTP requests for API calls
-   `python-dotenv` - Environment variable management

---

Made with ❤️ for better professional networking
