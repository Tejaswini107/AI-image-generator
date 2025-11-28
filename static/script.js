const generateBtn = document.getElementById("generateBtn");
const loader = document.getElementById("loader");
const resultImage = document.getElementById("resultImage");
const downloadBtn = document.getElementById("downloadBtn");

generateBtn.onclick = async () => {
    const prompt = document.getElementById("prompt").value.trim();
    if (!prompt) {
        alert("Please enter a prompt!");
        return;
    }

    loader.style.display = "block";
    resultImage.style.display = "none";
    downloadBtn.style.display = "none";

    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt })
    });

    const data = await response.json();
    const imgData = data.image;

    loader.style.display = "none";
    resultImage.src = imgData;
    resultImage.style.display = "block";

    // Download button
    downloadBtn.href = imgData;
    downloadBtn.style.display = "inline-block";
};
