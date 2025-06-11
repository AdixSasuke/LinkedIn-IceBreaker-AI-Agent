import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
  """scrape information from linkedin profile,
      Manually scrape the information from the Linkedin profile"""
  
  if mock:
    linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
    response = requests.get(
      linkedin_profile_url, 
      timeout = 10,
    )
  else:
    api_endpoint = "https://api.scrapin.io/enrichment/profile"
    params = {
      "apikey": os.environ["SCRAPIN_API_KEY"],
      "linkedInUrl": linkedin_profile_url
    }
    response = requests.get(
      api_endpoint,
      params = params,
      timeout = 10,
    )
  
  data = response.json().get("person")
  data = {
    k: v
    for k, v in data.items()
    if v not in ([], "", "", None) and k not in ["certifications"]
  }

  return data



if __name__ == "__main__":
  print(
    scrape_linkedin_profile(
      linkedin_profile_url = "https://www.linkedin.com/in/adityakhandelwal9/",
      mock=True
    )
  )