import openai
import os

os.environ["http_proxy"] = "127.0.0.1:49762"
os.environ["https_proxy"] = "127.0.0.1:49762"
# openai.proxy = proxies
openai.api_key = "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"


# completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system","content": "You are an AI research assistant. You use a tone that is technical and scientific."},
#         {"role": "user", "content": "Hello, who are you?"},
#         {"role": "assistant", "content": "Greeting! I am an AI research assistant. How can I help you today?"},
#         {"role": "user", "content": "Can you tell me about the creation of black holes?"}
#     ]
# )
# print(completion)


# # 一个封装 OpenAI 接口的函数，参数为 Prompt，返回对应结果
# def get_completion(prompt, model="gpt-3.5-turbo"):
#     """
#     prompt: 对应的提示
#     model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
#     """
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0,  # 模型输出的温度系数，控制输出的随机程度
#     )
#     # 调用 OpenAI 的 ChatCompletion 接口
#     return response.choices[0].message["content"]


class chatbot:
    def __init__(self):
        self.messages = [{"role": "system",
                          "content": "你是一名性格开朗的大学生，你很乐于与他人交流"}]

    def get_completion(self, prompt, model="gpt-3.5-turbo"):
        """
        prompt: 对应的提示
        model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
        """
        self.messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model=model,
            messages=self.messages,
            temperature=0,  # 模型输出的温度系数，控制输出的随机程度
        )
        # 调用 OpenAI 的 ChatCompletion 接口
        answer = response.choices[0].message["content"]
        self.messages.append({"role": "assistant", "content": answer})
        return answer



