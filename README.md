# QR Code Generator – Dockerized

This project is a Dockerized Python application that generates QR codes from user-provided URLs or text.  
The app runs consistently across different environments using a lightweight, secure Docker image and can be built and tested locally or via GitHub Actions.

---

## Features

- Generate QR codes from any URL or text string.
- Command-line interface with optional arguments.
- Saves QR codes as image files (PNG by default).
- Supports saving into a `qrcodes/` directory (useful with Docker volume mounts).
- Docker image based on `python:3.12-slim-bullseye`.
- Runs as a non-root user inside the container for better security.
- Ready to integrate with CI/CD using GitHub Actions.

---

## Project Structure

```text
.
├── main.py                 # QR Code Generator application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build instructions
├── Reflection_Document.pdf # Reflection on the project 
└── .github/
    └── workflows/
        └── ci.yml          # Example GitHub Actions workflow 
```

---

## How to Run Locally (Without Docker)

1. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
2. Install the necessary requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py --url https://github.com/ishajagtap
   ```

---

## How to Build and Run with Docker

1. **Build the Image**
   Run the following command in the root of the project to build the Docker image:
   ```bash
   docker build -t qr-code-generator-app .
   ```

2. **Run the Container**
   You can run the container in detached mode. To persist the generated QR codes onto your local machine, use a volume mount to bind your local `qrcodes` folder to the container's `/app/qrcodes` folder:

   ```bash
   # Create a local folder to store the output images
   mkdir qrcodes

   # Run the container (replace $(pwd)/qrcodes with the absolute path on Windows if needed)
   docker run -d --name qr-generator -v $(pwd)/qrcodes:/app/qrcodes qr-code-generator-app --url "https://github.com/ishajagtap"
   ```

3. **Check the Output**
   - Check the container logs to ensure it resolved successfully:
     ```bash
     docker logs qr-generator
     ```
   - You will see the newly generated QR code png image appear in your local `qrcodes` directory!

4. **Cleanup**
   Once you're done, stop and remove the container:
   ```bash
   docker stop qr-generator
   docker rm qr-generator
   ```
