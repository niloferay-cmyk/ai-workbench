import os
import sys
from dotenv import load_dotenv
from openai import OpenAI,AuthenticationError,APIConnectionError

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")



if not api_key :
    print("ERROR: OPENAI_API_KEY not found!")
    sys.exit(1)
    
print(api_key)

client=OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
print(client)
MODEL=os.getenv("OPENAI_MODEL","gpt-4.1-mini")
#---------------- THE CALL-------------------
print("Sending prompt:What is gen AI in one sentence ?")
try:
    response=client.chat.completions.create(model=MODEL,
     messages=[
        {"role":"system",
               "content":"You are a helpful assistant.Be Concise"},
        {"role":"user",
          "content":"What is generative AI in one sentence?"},
        ],
     temperature=0.7,
     max_tokens=100,
     )

#response +errors
    print(f"Response:{response.choices[0].message.content}")
    print(f"Tokens user: {response.usage.total_tokens}")

except AuthenticationError:
    print("Error invalid API key")
except APIConnectionError:
    print("error cannot connect.check your internet")
except Exception as e:
    print(f"Unexpected error: {e}")