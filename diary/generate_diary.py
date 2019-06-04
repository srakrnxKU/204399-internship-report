import pandas as pd
import os
import os.path

this_directory = os.path.dirname(os.path.realpath(__file__))
file_path = 'images'

entries = pd.read_csv('diary.csv')
images = os.listdir(file_path)
print(images)
picture_entry = '''
\\section*{{{section}}}
\\begin{{figure}}[h]
    \\centering
    \\includegraphics[width=0.5\\textwidth]{{{src}}}
    \\caption{{{caption}}}
\\end{{figure}}
'''

img = open("diaryimgs.tex", "w")

for index, row in entries.iterrows():
    date = "{}{:02d}{:02d}".format(row['y'], row['m'], row['d'])
    pretty_date = "{}/{}/{}".format(row['d'], row['m'], row['y']+543)
    print(date)
    matching_files = [i for i in images if date in i]
    if len(matching_files) > 0:
        full_image_path = os.path.join(
            this_directory, file_path, matching_files[0])
        img.write(picture_entry.format(src=full_image_path, section="ภาพการฝึกงานวันที่ {}".format(
            pretty_date), caption=row['caption']))
    else:
        img.write("% Image for {} not found.\n".format(pretty_date))

img.close()
