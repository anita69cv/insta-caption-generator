from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def get_image_description(image_path):
    # ✅ Step 1: Load image FIRST
    image = Image.open(image_path).convert('RGB')

    # ✅ Step 2: Then resize
    image = image.resize((256, 256))

    # ✅ Step 3: Process
    inputs = processor(image, return_tensors="pt")

    output = model.generate(**inputs)

    return processor.decode(output[0], skip_special_tokens=True)