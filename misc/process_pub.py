# generate pub folders from csv template

import os
import csv
from shutil import copyfile

with open('collections.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  next(csv_reader)
  for item in csv_reader:
    abbr = item[0]
    try:
      pub_dir = "publications/"+abbr
      os.mkdir(pub_dir)
    except FileExistsError:
      print("ERROR:", abbr, "exists!")

    f_index = open(pub_dir+"/index.md", 'w+')
    content_index = []

    content_index.append("---")
    content_index.append("title: \"%s\"" % item[1])
    content_index.append("authors: [%s]" % item[2])
    content_index.append("date: %s" % item[3])
    content_index.append("doi: \"%s\"" % item[5])
    content_index.append("publishDate: %s" % item[3])
    content_index.append("publication_types: [\"%s\"]" % item[4])
    content_index.append("publication: \"%s\"" % item[6])
    content_index.append("publication_short: \"%s\"" % item[7])

    # abstract
    content_index.append("abstract: \"")
    print("item9", item[9])
    with open("files/"+item[9], 'r') as f_abs:
      content_index.append(f_abs.readline())
    content_index.append('\"')

    content_index.append("tags: [%s]" % item[13])
    # FIXME
    # content_index.append("featured: %s" % item[14])
    content_index.append("featured: true")

    if os.path.isfile("files/" + item[8]):
      copyfile("files/"+item[8], "publications/"+abbr+"/"+abbr+".pdf")

    content_index.append("url_code: %s" % item[10])
    content_index.append("url_poster: %s" % item[11])
    if item[11]:
      # copy the poster to pub folder
      copyfile("files/" + item[11], "publications/" + abbr + "/" + item[11])
    content_index.append("url_slides: %s" % item[12])
    if item[12]:
      # copy the slides to pub folder
      copyfile("files/" + item[12], "publications/" + abbr + "/" + item[12])

    content_index.append("projects: [%s]" % item[15])

    content_index.append("---")

    for line in content_index:
      f_index.write(line)
      f_index.write('\n')

    print("Paper:", abbr, "added!")

