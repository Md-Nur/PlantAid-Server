from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from static_data import crop_diseases

app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Green Spark": "PlantAid"}


potato_model = tf.keras.models.load_model("./models/potato/4/model.keras")
tomato_model = tf.keras.models.load_model("./models/tomato/1/model.keras")
pepper_model = tf.keras.models.load_model("./models/pepper/1/model.keras")

pata_model = tf.keras.models.load_model("./models/isPata/1/model.keras")
pata_class = ["Others", "মরিচ", "আলু", "টমেটো"]


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


def isPata(image_batch, pata_name):
    predictions = pata_model.predict(image_batch)
    predicted_class = pata_class[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    if predicted_class == "Others":
        return ["এটা (আলু/টমেটো/মরিচ)পাতা নয়! অন্য কিছু হতে পারে।", confidence]
    elif predicted_class != pata_name:
        return [f"এটা {pata_name} পাতা নয়! এটা {predicted_class} পাতা হতে পারে।", confidence]
    else:
        return [False, False]


@app.post("/predict/potato")
async def predict_potato(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    potato_diseases = crop_diseases[1]["diseases"]
    pata = isPata(img_batch, "আলু")
    if pata[0]:
        return {"warn": pata[0], "confidence": float(pata[1] * 100)}
    
    predictions = potato_model.predict(img_batch)
    predicted_class = potato_diseases[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {"class": predicted_class, "confidence": float(confidence * 100)}

@app.post("/predict/tomato")
async def predict_tomato(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    print(image)
    img_batch = np.expand_dims(image, 0)

    pata = isPata(img_batch, "টমেটো")
    if pata[0]:
        return {"warn": pata[0], "confidence": float(pata[1] * 100)}
    
    predictions = tomato_model.predict(img_batch)
    tomato_disesases = crop_diseases[2]["diseases"]
    predicted_class = tomato_disesases[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {"class": predicted_class, "confidence": float(confidence * 100)}


@app.post("/predict/pepper")
async def predict_pepper(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    pata = isPata(img_batch, "মরিচ")
    if pata[0]:
        return {"warn": pata[0], "confidence": float(pata[1] * 100)}
    
    predictions = pepper_model.predict(img_batch)
    pepper_disesases = crop_diseases[0]["diseases"]
    predicted_class = pepper_disesases[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {"class": predicted_class, "confidence": float(confidence * 100)}
