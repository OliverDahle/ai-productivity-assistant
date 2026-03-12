import openai
import os

# Authorization for the API Key, I stored the value in my .env file
token = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=token)

def generate_plan(prompt):
    # Generating a plan based on input
    try:
        response = client.chat.completions.create(
            # Specifying the model
            model="gpt-4",
            # Using system to specify the general role, and user to specify the user input
            messages=[
                {"role": "system", "content": "You are a personal productivity assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Return value is now the response from the model
        return response.choices[0].message.content
    except Exception as e:
        # Standard error handling
        return f"Error generating plan: {str(e)}"
