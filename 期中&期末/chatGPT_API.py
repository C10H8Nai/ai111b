import openai
import os

# Set the API key and model

dict_temp = {}
pyDir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(pyDir, "key.txt") , "r") as keyfile:
    for line in keyfile.readlines():
        line = line.strip()
        k = line.split(':')[0]
        v = line.split(':')[1]
        dict_temp[k] = v
    openai.api_key = dict_temp['CHATGPT_KEY']

model_engine = "gpt-3.5-turbo"

def callGPT(itemlist):
    # Generate a response from the model
    start_idx = 0
    result = ''
    while start_idx < len(itemlist):
        end_idx = min(start_idx + 1600, len(itemlist))
        sub_list = itemlist[start_idx:end_idx]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": f"請以繁體中文回答，{sub_list}"}
            ]
        )
        for choice in response.choices:
            result += choice.message.content
        #print(start_idx)
        start_idx = end_idx
    return(result)

# Manual print the response
'''
while True:
    itemlist = input("請輸入：")
    if itemlist != "quit":
        result = callGPT(itemlist)
        print(result)
    else:
        break
'''