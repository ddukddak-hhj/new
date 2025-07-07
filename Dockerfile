# 더 가볍고 보안성이 강화된 이미지 사용
FROM python:3.10-slim

WORKDIR /app

# 코드 복사
COPY . .

# 의존성 설치
RUN pip install --no-cache-dir flask

# 실행
CMD ["python", "app.py"]
