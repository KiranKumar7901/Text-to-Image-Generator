import os
import openai

key = "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"
openai.api_key = key

response = openai.Image.create(prompt="a white siamese cat",
                               n=1,
                               size="1024x1024")
image_url = response['data'][0]['url']
print(image_url)
