FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ADD opa-shim-server.py /
CMD [ "python", "./opa-shim-server.py" ]
