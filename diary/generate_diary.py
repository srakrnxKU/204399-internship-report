import pandas as pd
import os
import os.path

file_path = 'images'

entries = pd.read_csv('diary.csv')
images = os.listdir(file_path)
entry_format = '''
\\begin{{figure}}
    \\centering
    \\includegraphics[0.8\\textwidth]{{{src}}}
    \\caption{{{caption}}}
\\end{{figure}}

{description}
'''

for index, row in entries.iterrows():
    date = "{:02d}{:02d}{}".format(row['y'], row['m'], row['d'])
    pretty_date = "{}/{}/{}".format(row['d'], row['m'], row['y']+543)
    matching_files = [i for i in images if date in i]
    if len(matching_files) > 0:
        full_image_path = os.path.join(file_path, matching_files[0])
        print(entry_format.format(src=full_image_path, caption="ภาพการฝึกงานวันที่ {}".format(
            pretty_date), description=row['description']))
