import csv
import os
csv_file_path = 'C:/Users/user/Desktop/Projects/VertexAI_Practice(EmotionText)/archive/Tweet_emotionsText.csv'

output_directory = 'C:/Users/user/Desktop/Projects/VertexAI_Practice(EmotionText)/CsvToText/outputFiles'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)


with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

   
    next(csv_reader, None)


    for index, row in enumerate(csv_reader, start=1):
        # 각 라인의 세 번째 컬럼(내용) 추출
        content = row[2].strip()
      
        txt_file_name = f'txt{index}.txt'
        txt_file_path = os.path.join(output_directory, txt_file_name)

    
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(content)

print("Done.")
