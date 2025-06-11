# 🧊 Ice Breaker - AI-Powered LinkedIn Profile Analyzer

A Python application that scrapes LinkedIn profiles and generates AI-powered summaries with interesting facts to help break the ice in conversations.

## 🌟 Features

-   **LinkedIn Profile Scraping**: Automatically extracts information from LinkedIn profiles using ScrapIn API
-   **AI-Powered Analysis**: Uses Google's Gemini AI to generate intelligent summaries
-   **Conversation Starters**: Provides interesting facts perfect for ice-breaking conversations
-   **Easy to Use**: Simple command-line interface with minimal setup

## 🛠️ Tech Stack

-   **Python 3.8+**
-   **LangChain**: For AI chain orchestration
-   **Google Gemini AI**: For natural language processing
-   **ScrapIn API**: For LinkedIn profile scraping
-   **python-dotenv**: For environment variable management

## 📋 Prerequisites

Before running the application, you'll need to obtain API keys for:

1. **Google Gemini API Key**

    - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
    - Create a new API key
    - Copy the API key for use in your `.env` file

2. **ScrapIn API Key**
    - Visit [ScrapIn.io](https://scrapin.io/)
    - Sign up for an account
    - Get your API key from the dashboard

## 🚀 Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd ice_breaker
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
   Create a `.env` file in the project root with the following content:
    ```env
    GEMINI_API_KEY=your_google_gemini_api_key_here
    SCRAPIN_API_KEY=your_scrapin_api_key_here
    ```

## 📦 Dependencies

Install the required packages:

```bash
pip install langchain-google-genai
pip install langchain-core
pip install python-dotenv
pip install requests
```

Or update the `requirements.txt` file with:

```
langchain-google-genai
langchain-core
python-dotenv
requests
```

## 🎯 Usage

1. **Basic Usage:**

    ```bash
    python ice_breaker.py
    ```

2. **Modify the LinkedIn URL:**
   Edit the `linkedin_profile_url` in `ice_breaker.py` to analyze different profiles:

    ```python
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/your-target-profile/"
    )
    ```

3. **Mock Mode for Testing:**
   Use the mock mode to test without consuming API credits:
    ```python
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",
        mock=True
    )
    ```

## 📁 Project Structure

```
ice_breaker/
├── ice_breaker.py              # Main application file
├── requirements.txt            # Python dependencies
├── .env                       # Environment variables (create this)
├── agents/
│   ├── __init__.py
│   └── linkedin_lookup_agent.py  # LinkedIn lookup agent (future enhancement)
└── third_parties/
    ├── __init__.py
    └── linkedin.py            # LinkedIn scraping utilities
```

## 🔧 Configuration

### Environment Variables

| Variable          | Description                                | Required |
| ----------------- | ------------------------------------------ | -------- |
| `GEMINI_API_KEY`  | Your Google Gemini API key                 | Yes      |
| `SCRAPIN_API_KEY` | Your ScrapIn API key for LinkedIn scraping | Yes      |

### API Rate Limits

-   **Gemini Free Tier**: Limited requests per day/minute
-   **ScrapIn**: Check your plan limits
-   The application uses `gemini-1.5-flash` for better rate limit handling

## 📖 Example Output

```
Based on the LinkedIn information, here's a summary:

**Short Summary:**
John Doe is a Senior Software Engineer at Tech Corp with 5+ years of experience
in full-stack development, specializing in React and Node.js applications.

**Two Interesting Facts:**
1. He built a mobile app that reached 100K downloads in its first month
2. He's a certified scuba diver and has explored coral reefs in 15+ countries
```

## 🚨 Error Handling

The application includes robust error handling for common issues:

-   **Quota Exceeded**: Provides helpful guidance when API limits are reached
-   **Missing API Keys**: Clear error messages for configuration issues
-   **Network Issues**: Timeout handling for API requests

## 🔮 Future Enhancements

-   [ ] Complete the LinkedIn lookup agent implementation
-   [ ] Add support for multiple profile analysis
-   [ ] Implement caching to reduce API calls
-   [ ] Add web interface using Streamlit or Flask
-   [ ] Support for other social media platforms
-   [ ] Export results to different formats (PDF, JSON, etc.)

## ⚠️ Important Notes

1. **Respect Rate Limits**: Both APIs have rate limits. Use responsibly.
2. **Privacy**: Only scrape public LinkedIn profiles and respect privacy settings.
3. **Terms of Service**: Ensure compliance with LinkedIn's and API providers' terms of service.
4. **API Costs**: Monitor your API usage to avoid unexpected charges.

## 🐛 Troubleshooting

### Common Issues

1. **"ResourceExhausted" Error:**

    - You've hit the Gemini API rate limit
    - Wait a few hours or upgrade to a paid plan
    - Consider using mock mode for testing

2. **"GEMINI_API_KEY not found" Error:**

    - Ensure your `.env` file is in the project root
    - Check that the API key is correctly set
    - Restart your terminal/IDE after creating the `.env` file

3. **LinkedIn Scraping Fails:**
    - Verify your ScrapIn API key
    - Check if the LinkedIn URL is public and valid
    - Use mock mode for testing

## 📄 License

This project is for educational purposes. Please ensure compliance with all relevant terms of service and privacy policies.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section
2. Review the API documentation
3. Create an issue in the repository

---

**Happy Ice Breaking! 🧊✨**
