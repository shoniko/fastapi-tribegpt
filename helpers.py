
import openai


def chat_openai(prompt, system_text="",token_limit=2048):
    chat_query = [{"role":"system", "content": system_text}, {"role":"user", "content": prompt}]

    response = openai.ChatCompletion.create(
            messages=chat_query,    
            # model="gpt-4-0314",
            model = "gpt-3.5-turbo",
            temperature=0,
            max_tokens=token_limit,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=' ;'
            )    
    output = response["choices"][0]["message"]["content"]


def generate_roadmap():
    prompt = '''
    
    '''
    system_prompt = ''

    roadmap = chat_openai(prompt, system_prompt)
    return roadmap

def generate_ideas():
    prompt = '''
    
    '''
    system_prompt = ''
    ideas = chat_openai(prompt, system_prompt)
    ideas = ideas.split('\n')
    return ideas

