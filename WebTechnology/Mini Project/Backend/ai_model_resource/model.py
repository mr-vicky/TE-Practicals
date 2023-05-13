from diffusers import StableDiffusionPipeline
import torch
import base64
import requests
import os


class SuggestModel:

    def __init__(self) -> None:
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        self.model_id = "runwayml/stable-diffusion-v1-5"
        self.model = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16)

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
        try:
            image = self.model(dialogue).images[0]
        except Exception as err:
            print("An error occured while generating an image")

        b64_image = None

        if image:
            b64_image = self.__image_to_base64(image)
        else:
            image = requests.get("https://picsum.photos/200")
            b64_image = self.__image_to_base64(image)

        return b64_image

