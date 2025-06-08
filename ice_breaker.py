from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
import os

if __name__ == "__main__":
    simple_parser = StrOutputParser()
    google_api_key = os.getenv("GEMINI_API_KEY")
    
    summary_template = """
                        given the linkedin information {information}
                        1. a short summary
                        2. two interesting facts about them"""

    summary_prompt_template = PromptTemplate(input_variables = ["information"], template = summary_template)

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

    chain = summary_prompt_template | llm | simple_parser
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/khandelwalchhavi/")
    res = chain.invoke(input={"information": linkedin_data})

    print(res)