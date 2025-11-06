# python
# gemini_api_fixed.py
# .env 파일에서 GEMINI_API_KEY를 읽어와 genai 클라이언트를 생성하고 간단한 요청을 보냅니다.

from dotenv import load_dotenv
import os
from google import genai
from datetime import datetime, date

# .env 파일에서 환경 변수 불러오기
load_dotenv()

# 환경 변수 읽기
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY가 설정되어 있지 않습니다. .env 파일을 만들거나 'export'로 설정하세요.")

# API 키를 명시적으로 전달하여 클라이언트 생성
client = genai.Client(api_key=api_key)

# Get current date
today = date.today()
current_date = today.strftime("%Y-%m-%d")

# 간단한 요청(예제)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Today is {current_date}. How many days until Christmas?",
)
print(response.text)

# 간단한 요청(예제)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"What is the weather usually like around that time?",
)
print(response.text)