from openai import OpenAI
client = OpenAI()

def generate_tests(schema):
    prompt = f"""
    Generate dbt tests for this schema:
    {schema}
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
