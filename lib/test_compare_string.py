import os 
import dotenv
from openai import OpenAI
import google.generativeai as genai

dotenv.load_dotenv()
GEMINI_API_KEY = os.getenv('GEMENI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

client = OpenAI()

def compare_string_gemini(string1, string2):
    response = model.generate_content(f" Compare the following two strings and determine how familiar they are. If they are suspected to match or be related, return the value 5. If not, return the value 4. Only return a single digit integer (4 or 5) based on the comparison. String 1: {string1}  String 2: {string2}")
    print(response.text)
    
def compare_string_openai(string1, string2):
    prompt = f" Compare the following two strings and determine how familiar they are. If they are suspected to match or be related, return the value 5. If not, return the value 4. Only return a single digit integer (4 or 5) based on the comparison. String 1: {string1}  String 2: {string2}"
    result = client.chat.completions.create(
        messages=[
    {"role": "system", "content": prompt},
    ],
        model="gpt-3.5-turbo",
    )


    return result.choices[0].text.strip()




var = input("openai or gemeni or llama: ")
if var == 'o':
    print(compare_string_openai("Wells Fargo ", "Walls fargo Se"))
elif var == 'g':
    print(compare_string_gemini("Wells Fargo ", "Walls fargo Se"))


#give it time, just made the api keys and see if they work