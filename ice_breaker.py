from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
import os
from dotenv import load_dotenv

load_dotenv()

def ice_breaker_with(linkedin_profile_url: str) -> str:
    """
    Given a LinkedIn profile URL, generate an ice breaker message about the person
    """
    # Scrape LinkedIn profile information
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )
    
    # Extract the person's name from LinkedIn data
    person_name = linkedin_data.get('full_name', 'this person')
    
    # Create the prompt template
    simple_parser = StrOutputParser()
    summary_template = """
    Given the LinkedIn information about {name}: {information}
    
    Please provide:
    1. A short summary about this person (2-3 sentences)
    2. Two interesting facts about them that could be used as conversation starters
    
    Format your response in a friendly, conversational tone.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["name", "information"], 
        template=summary_template
    )

    # Initialize the LLM with Gemini
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.environ["GEMINI_API_KEY"],
        temperature=0.7
    )

    # Create the chain
    chain = summary_prompt_template | llm | simple_parser

    # Generate the ice breaker
    res = chain.invoke(input={
        "name": person_name,
        "information": linkedin_data
    })

    return res

if __name__ == "__main__":
    # Example usage
    linkedin_url = "https://www.linkedin.com/in/adityakhandelwal9/"
    
    try:
        ice_breaker_message = ice_breaker_with(linkedin_url)
        print(ice_breaker_message)
    except Exception as e:
        print(f"Error: {e}")