# AI-Powered Image Generator

## Project Overview
This project is a **text-to-image generation system** built using the open-source **Stable Diffusion Turbo (SD-Turbo)** model. It converts user-provided textual prompts into high-quality images. The project demonstrates hands-on experience with generative AI, deep learning frameworks, and creative applications.

**Features:**
- Accepts user text prompts to generate images.
- Adjustable parameters: number of images per prompt, style guidance (photorealistic, artistic, cartoon).
- Prompt engineering for enhanced quality (e.g., "highly detailed", "4K", "professional photo").
- Option to download generated images in PNG format.
- CPU fallback available for systems without GPU.

---

## Project Architecture
User Prompt (Frontend HTML/CSS/JS)
↓
Backend (Flask/Streamlit)
↓
SD-Turbo Model (PyTorch)
↓
Generated Images (Saved locally)

---
Hardware Requirements

GPU recommended for faster image generation.
CPU fallback available (image generation takes ~4–6 minutes per prompt).

---
Model Details

Model Name: Stable Diffusion Turbo (SD-Turbo)
Framework: PyTorch
Type: Latent Diffusion Text-to-Image Model

Description:
The SD-Turbo model generates high-quality images from text prompts. Text is encoded and transformed into a latent space, then progressively refined through denoising steps to produce the final image.

---
Limitations:

CPU generation is slow (~4–6 minutes per image).
Output quality depends on prompt specificity.

---
Usage Tips

Use descriptive prompts like: "a futuristic city at sunset, highly detailed, 4K, cinematic lighting".
Experiment with style guidance for artistic variations.
Negative prompts can help filter unwanted elements.

---
Future Improvements

Add GPU optimization and batch processing.
Integrate style transfer and fine-tuning on custom datasets.
Include automated content filtering and watermarking for ethical AI use.

---
## Setup & Installation

```bash
git clone https://github.com/Tejaswini107/AI-image-generator.git
cd AI-image-generator


uvicorn main:app --reload











