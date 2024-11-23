## DOCX to PDF Converter Web Application
# Project Overview
This project provides a web-based solution to process Word documents (.docx) and convert them into PDF format. Users can upload .docx files, view file metadata, and download the generated PDFs. The application is built with a user-friendly interface, Dockerized for portability, and deployable on Kubernetes for scalability.
# Features
Upload .docx files for conversion to PDF.

View file metadata (e.g., file size, creation date).

Download the converted PDF files.

Password protection for PDFs (bonus feature).

Scalable architecture using Kubernetes.

Fully containerized using Docker for easy deployment.

CI/CD pipeline implemented with GitHub Actions for automated Docker builds.

Comprehensive documentation and a working demonstration video included.

# Getting Started
1. Prerequisites
   
Python 3.9+

Docker

Kubernetes (kubectl recommended for local testing)

Git

2. Running the Application Locally
   
Clone the repository: git clone https://github.com/kashishsingla111/docx-to-pdf.git

cd docx-to-pdf

Install dependencies: pip install -r requirements.txt

Run the Flask application: python app.py

Access the application at http://localhost:5000.

3. Running with Docker
   
Build the Docker image: docker build -t docx-to-pdf .

Run the container: docker run -p 5000:5000 docx-to-pdf

4. Deploying on Kubernetes
   
Apply the deployment and service manifests:

kubectl apply -f kubernetes/deployment.yml

kubectl apply -f kubernetes/service.yml

Forward the service port to access the application: kubectl port-forward service/docx-to-pdf-service 8080:80

Access the application at http://localhost:8080.

Access through local host: http://localhost/
![image](https://github.com/user-attachments/assets/7f2fca0e-5a4e-455d-92df-e859994a9fe2)


5. CI/CD Pipeline
   
This project includes a **GitHub Actions workflow** for automated Docker builds and pushes to Docker Hub. The workflow is located in .github/workflows/docker-build.yml. Ensure you set the following GitHub repository secrets:

DOCKER_USERNAME: Your Docker Hub username.

DOCKER_PASSWORD: Your Docker Hub password.

# Additional Resources

Project Documentation: A comprehensive PDF document detailing the project is included in the repository (wordtopdf.pdf).

Demonstration Video: Watch the application in action (docxtopdf.mp4).

Full Code: wordtopdf.zip contains all the files necessary for running the website, put your details of docker hub and github and run your website NOW !

# Future Enhancements

Add support for batch file uploads and conversion.

Enable user authentication for added security.

Expand the metadata extraction for detailed reports.

Implement advanced PDF customization options (e.g., watermarking).

# Contributors

Kashishsingla111

# License

This project is licensed under the MIT License - see the LICENSE file for details.
