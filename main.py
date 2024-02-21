import logging
from openai import OpenAI
import argparse

logging.basicConfig(level=logging.INFO)

class PersonalizedContentGenerator:
    def __init__(self):
        # Normally, an API key should be securely fetched from environment variables or secure storage
        self.conversation_memory = []
        self.client = OpenAI()  # Ensure secure API Key management
        self.project_idea = ""
        self.project_code = ""

    def generate_educational_content(self, model_type, subject, difficulty, target_audience, length=300):
        """
        Generates educational content based on given parameters.
        """
        prompt = f"Generate an educational content piece about {subject} that is '{difficulty}' difficulty, tailored for {target_audience}, approximately {length} words."
        system_message = f"Creating content about {subject}, Difficulty: {difficulty}, Audience: {target_audience}, Length: {length} words."
        content = self.generate_response(model_type, prompt, system_message)
        return content

    def generate_response(self, model_type, prompt, system_message=""):
        """
        Sends a request to the OpenAI API and returns the generated response.
        """
        messages = [{"role": "system", "content": system_message}, {"role": "user", "content": prompt}]
        response = self.client.chat.completions.create(model=model_type, messages=messages)
        content = response.choices[0].message.content
        logging.info(f"Response received: {content}")
        return content

def parse_arguments():
    """Configure and parse command-line arguments"""
    parser = argparse.ArgumentParser(description='Generate Personalized Educational Content')
    parser.add_argument('--model', default='gpt-4-0125-preview',choices=['gpt-4-0125-preview', 'gpt-3.5-turbo-0125'], required=True, help='Model to use for generating content')
    parser.add_argument('--subject', required=True, help='Subject of the educational content')
    parser.add_argument('--difficulty', required=True, help='Difficulty level of the content')
    parser.add_argument('--audience', required=True, help='Target audience for the content')
    parser.add_argument('--length', type=int, default=300, help='Approximate length of the content in words', required=False)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    content_generator = PersonalizedContentGenerator()
    generated_content = content_generator.generate_educational_content(
        model_type=args.model,
        subject=args.subject,
        difficulty=args.difficulty,
        target_audience=args.audience,
        length=args.length
    )
    print(f"\nGenerated Educational Content:\n{generated_content}\n")
