key_x = "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"
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
openai.api_key = "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"
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?,用100个字中文回答"}
    ],
  stream= True
  
)

print(response)
for i in response:
  try:
    chunk_message = i['choices'][0]['delta']["content"]  # extract the message
    print(chunk_message,)
  except:
    print("*")
    
  # print("-"*50)
  
  # print(i)
  