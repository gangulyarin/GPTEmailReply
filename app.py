import openai
import config

openai.api_key = config.API_KEY

Body = '''Hi Martin,
I have an exciting new feature request for you. Our users have been asking for a personalized dashboard that provides an overview of their account activity and statistics.
I would appreciate it if you could start working on this feature and provide an estimate for the development effort required.
Regards, 
Bill.
'''
response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Create a reply to this email:\n" + Body,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )
print(response["choices"][0]["text"])