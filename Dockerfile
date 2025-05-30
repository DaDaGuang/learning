FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY ./app ./app

CMD ["python","-m","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
