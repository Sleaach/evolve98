import google.generativeai as genai

def genaii():
 try:
  genai.configure(api_key="AIzaSyDWoJAFMI-t5tBYZOpz9cE4AXPFOR4OSQ4")
  
  generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

  safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

  convo = model.start_chat(history=[
])
  print("\nÇıkış için 'q'")
  while True:
   send = input("\n\nAI: ")
   if send == "q":
    break
   convo.send_message(send)
   print(f"\n{convo.last.text}")
 except Exception as e:                                                                                                           
  print(e)
