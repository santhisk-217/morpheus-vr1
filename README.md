Morpheus: A Serverless Generative VR Engine

Morpheus is a "Generative Reality" engine that allows users to generate immersive 3D Virtual Reality (VR) worlds instantly from simple text prompts. Hosted on Google Cloud Run, it leverages a Python logic engine to construct A-Frame (WebVR) scenes in real-time, accessible directly in the browser without any downloads.

🚀 Live Demo

Deployed App: Click here to try Morpheus VR: https://morpheus-vr-749319087812.us-central1.run.app/

Note: Requires a WebGL-compatible browser (Chrome, Firefox, Edge).

📖 Overview

Traditional Generative AI focuses on 2D images. Morpheus takes this a step further by generating spatial, navigable environments.

Users enter a prompt like "Neon City" or "Blue Car", and the backend procedurally generates the HTML/A-Frame code required to render that scene in 3D. The result is a lightweight, instant VR experience.

🏗 Architecture

The project follows a serverless, event-driven architecture:

Frontend: HTML5 + A-Frame (WebVR framework).

Backend: Python (Flask).

Infrastructure: Containerized with Docker and deployed on Google Cloud Run.

Visual Flow

User Input ("Red Car") ->

Flask Backend (Parses keywords: "Red", "Car") ->

Logic Engine (Constructs <a-box> & <a-cylinder> entities) ->

Frontend (Renders 3D Scene in Browser).

🛠 Tech Stack

Language: Python 3.9

Web Framework: Flask

3D Framework: A-Frame (HTML5 WebVR)

Cloud Platform: Google Cloud Run (Serverless)

Containerization: Docker

📦 Installation & Local Run

To run Morpheus locally on your machine:

Clone the repository:

git clone [https://github.com/yourusername/morpheus-vr.git](https://github.com/yourusername/morpheus-vr.git)
cd morpheus-vr


Install Dependencies:

pip install flask gunicorn


Run the App:

python app.py


Open Browser:
Go to http://localhost:8080

🎮 How to Use

Open the application URL.

Type a prompt into the text box.

Try: "Neon City" (Cyberpunk skyline)

Try: "Red Car" (3D Vehicle)

Try: "Alien Forest" (Planetary landscape)

Click "Generative Reality".

Wait 1-2 seconds for the world to generate.

Controls:

Desktop: Use W, A, S, D keys to walk. Click and drag mouse to look around.

Mobile: Move your phone to look around (Gyroscope).

🏆 Build & Blog Marathon 2025

This project was built for the Google Cloud Build & Blog Marathon to demonstrate the power of serverless architecture in delivering immersive media experiences.

Created by [Your Name]
