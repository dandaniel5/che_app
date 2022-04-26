FROM Python:3.7-alpine
ADD static/ /template main.py data.json /usr/src/app/
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
