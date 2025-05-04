FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (without Node.js and npm)
RUN apt-get update -y && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire application code
COPY seo.py .
COPY . .

# Streamlit configuration
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

# Verify the path to index.html
RUN ls -l /usr/local/lib/python3.11/site-packages/streamlit/static/index.html

# Run the SEO script to modify index.html
RUN python seo.py



EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]