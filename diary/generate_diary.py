import pandas as pd
import os
import os.path

this_directory = os.path.dirname(os.path.realpath(__file__))
file_path = 'images'

entries = pd.read_csv('diary.csv')
images = os.listdir(file_path)
entry_format = '''
\\subsection*{{{caption}}}
\\begin{{figure}}[h]
    \\centering
    \\includegraphics[width=0.5\\textwidth]{{{src}}}
    \\caption{{{caption}}}
\\end{{figure}}

{description}
'''

f = open("diary.tex", "w")

for index, row in entries.iterrows():
    date = "{:02d}{:02d}{}".format(row['y'], row['m'], row['d'])
    pretty_date = "{}/{}/{}".format(row['d'], row['m'], row['y']+543)
    matching_files = [i for i in images if date in i]
    if len(matching_files) > 0:
        full_image_path = os.path.join(
            this_directory, file_path, matching_files[0])
        f.write(entry_format.format(src=full_image_path, caption="ภาพการฝึกงานวันที่ {}".format(
            pretty_date), description=row['description']))
    else:
        f.write("% Image for {} not found.\n".format(pretty_date))

f.close()
