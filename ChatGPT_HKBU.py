import configparser
import requests
import os


class ChatGPT_HKBU():

    # def __init__(self, config_='./config.ini'):
    #     if type(config_) == str:
    #         self.config = configparser.ConfigParser()
    #         self.config.read(config_)
    #     elif type(config_) == configparser.ConfigParser:
    #         self.config = config_

    def submit(self, message):
        conversation = [{"role": "user", "content": message}]
        url = (os.environ['CHATGPT_BASICURL']) + "/deployments/" + (
            os.environ['CHATGPT_MODELNAME']) + "/chat/completions/?api-version=" + (
                  os.environ['CHATGPT_APIVERSION'])
        headers = {'Content-Type': 'application/json',
                   'api-key': (os.environ['CHATGPT_ACCESS_TOKEN'])}
        payload = {'messages': conversation}
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return 'Error:', response


if __name__ == '__main__':
    ChatGPT_test = ChatGPT_HKBU()
    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)
