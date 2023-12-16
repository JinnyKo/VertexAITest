import csv
import os

# CSV 파일 경로
csv_file_path = 'C:/Users/user/Desktop/Projects/VertexAI_Practice(EmotionText)/archive/Tweet_emotionsText.csv'

# 텍스트 파일 저장 디렉토리
output_directory = 'C:/Users/user/Desktop/Projects/VertexAI_Practice(EmotionText)/CsvToText/outputFiles'

# 디렉토리가 없으면 생성
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# CSV 파일 읽기
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # 헤더 건너뛰기
    next(csv_reader, None)

    # 라인별로 데이터 추출 및 저장
    for index, row in enumerate(csv_reader, start=1):
        # 각 라인의 세 번째 컬럼(내용) 추출
        content = row[2].strip()

        # 텍스트 파일 이름 지정
        txt_file_name = f'txt{index}.txt'

        # 텍스트 파일 경로 지정
        txt_file_path = os.path.join(output_directory, txt_file_name)

        # 텍스트 파일에 내용 저장
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(content)

print("텍스트 파일로 저장이 완료되었습니다.")
