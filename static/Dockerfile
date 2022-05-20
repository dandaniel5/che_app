FROM Python:3.10
ADD static/ /template main.py data.json /usr/src/app/
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
