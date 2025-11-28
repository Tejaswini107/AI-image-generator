from fastapi import FastAPI
from pydantic import BaseModel
import torch
from diffusers import StableDiffusionPipeline
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import base64
from io import BytesIO

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

# ⚡ SD-Turbo (best balance of speed + quality)
model_id = "stabilityai/sd-turbo"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)
pipe.to("cpu")


@app.post("/generate")
def generate(data: Prompt):
    image = pipe(
        data.prompt,
        num_inference_steps=20,   # good quality, still fast
        guidance_scale=1.0        # turbo works best around 1.0
    ).images[0]

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    return {"image": "data:image/png;base64," + img_str}


# Serve UI
app.mount("/", StaticFiles(directory="static", html=True), name="static")
