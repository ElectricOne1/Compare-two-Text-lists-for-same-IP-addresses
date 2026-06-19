def compare_txt_files(file1, file2):
### Created by Domenic Di Cello, ElectricOne1 on GitHub--Put YOUR 2 text file names Exact Paths @with open 
    with open("/home/Ip1.txt", 'r') as f:
        list1 = set(line.strip() for line in f if line.strip())
      ### Put YOUR file names and paths here in place of "home/IP .txt " etc...  
    with open("/home/Ip2.txt", 'r') as f:
        list2 = set(line.strip() for line in f if line.strip())

    # This finds IPs that are in BOTH files
    matches = list1.intersection(list2)
    
    print(f"Found {len(matches)} matches between the two files.")
    for ip in matches:
        print(f"Match found: {ip}")

# Example: compare_txt_files(Put your Files/Paths @'servers.txt', 'websites_List.txt' or Ip1.txt an Ip2.txt)
compare_txt_files("/home/Ip1.txt", "/home/Ip2.txt")