import os
import csv

def list_directory_structure(root_dir, output_file):
  with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    for dirpath, dirnames, filenames in os.walk(root_dir):
      for dirname in sorted(dirnames):
        writer.writerow([os.path.join(dirpath, dirname)])
      for filename in sorted(filenames):
        writer.writerow([os.path.join(dirpath, filename)])

if __name__ == "__main__":
  root_directory = 'images'
  output_file = 'file_names.csv'
  list_directory_structure(root_directory, output_file)