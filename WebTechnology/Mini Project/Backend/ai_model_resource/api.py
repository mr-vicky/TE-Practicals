import base64
import requests


class SuggestModel:

    def __init__(self) -> None:
        self.endpoint = "https://api-inference.huggingface.co/models/prompthero/openjourney-v4"
        self.headers = {"Authorization": "Bearer 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"}

    def __image_to_base64(self, image):
        base64_image = None
        try:
            base64_image = base64.b64encode(image)
            base64_image = 'data:image/jpeg;base64,' + base64_image.decode('utf-8')
        except Exception as err:
            print("An exception has occured")
        
        return base64_image

    def generate_image(self,dialogue):
        image = None
        payload = {
	    "inputs": str(dialogue),
        }
        try:
            response = requests.post(self.endpoint, headers=self.headers, json=payload)
            image_bytes = response.content
        except Exception as err:
            print("An error occured while generating an image")

        b64_image = None

        if image_bytes:
            b64_image = self.__image_to_base64(image_bytes)
        else:
            image_bytes = requests.get("https://picsum.photos/200")
            b64_image = self.__image_to_base64(image_bytes)

        return b64_image

