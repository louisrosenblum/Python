def process_seasons(input_file, output_file):
    data = open(str(input_file),"r")
    for i in data:
        z = i.split()
        print(z)
        process_season(output_file, i+1,z[i][0], z[i][1])
        print("")
        

process_seasons("soccer-in.txt", "dota2.txt")
