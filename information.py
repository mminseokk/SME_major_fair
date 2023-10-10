import openai
openai.api_key = "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"

def major(department_name):
    message_content1 = f"{department_name}에 대해 간략한 설명을 50글자 내외로 알려줘 "
    #생활 속 예시 
    message_content2 = f"{department_name} 전공 과목이 실생활에서 어떻게 사용되는지  간략한 설명을 120글자 내외로 알려줘 "

    message_content = message_content1 + "\n" +  message_content2
    # API 호출
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "user", "content": message_content}
      ],
      max_tokens = 700 
    )

    return response.choices[0].message['content'].strip()
    