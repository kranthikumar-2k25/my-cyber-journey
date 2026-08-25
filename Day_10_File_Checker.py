print("--- FILE CHECKER ---")

file1 = "data.gz"
file2 = "data.bz2"
file3 = "data.tar"
file4 = "data.txt"

if file1.endswith(".gz"):
  print("it is gzip file. use:gunzip [filename] command")
if file2.endswith(".bz2"):
  print("it is the bzip2 file. use:bunzip2 [filename] command")
if file3.endswith(".tar"):
  print("it is a tar file . use:tar -xvf [filename] command")
if file4.endswith(".txt"):
  print("it may be asc2 file do cat the file after checking the file [filename] command")




print("--- AUTOMATED FILE CHECKER ---")

suspicious_files = ["data.gz", "auto.bz2", "text.tar", "password.txt", "malware.bin"]

for filename in suspicious_files:
  if filename.endswith(".gz"):
    print(f"{filename} is gzip. use : gunzip {filename} command")
  elif filename.endswith(".bz2"):
    print(f"{filename} is bunzip2. use :bunzip2 {filename} command")
  elif filename.endswith(".tar"):
    print(f"{filename} is tar. use tar -xvf {filename} command")
  elif filename.endswith(".txt"):
    print(f"{filename}  is txt file. use the file {filename} command and if it is ASC2 file. cat {filename} command after to get the data inside")
  
  else:
    print(f"{filename} is unknown. use file {filename} command")
