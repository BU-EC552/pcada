import requests

NUM_COMPANIES = 5

if __name__ == '__main__':

    f = open("./template.yaml", "r")
    lines = f.readlines()

    f.close()

    content_lines = []
    for line in lines:
        if '#' not in line:
            processed_line = line.strip()
            if len(processed_line) != 0:
                content_lines.append(processed_line)
    
    for line in content_lines:
        print(line)

    for i in range(0, NUM_COMPANIES):
        response = requests.get("http://127.0.0.1:5000/company/%s" % (i+1))
        data = response.json()
        main_dict = data['main']
        frag_dict = data['fragment']
        plasmid_dict = data['plasmid']
        

        new_content = []
        for field in main_dict.keys():
            for line in content_lines:
                if field in line and field != "synthetic-fragment-cost" and field != "synthetic-plasmid-cost":
                    mod_line = line.replace("$", str(main_dict[field]['0'])) + "\n"
                    new_content.append(mod_line)

        new_content.append("synthetic-fragment-cost:\n")

        for j in range(0, len(frag_dict['fragment-cost'])):
            new_content.append("  " + str(frag_dict['fragment-cost'][str(j)]) + ":\n")
            new_content.append("    fixed: " + str(frag_dict['fixed'][str(j)]) + "\n")
            new_content.append("    cost: " + str(frag_dict['cost'][str(j)]) + "\n")

        new_content.append("synthetic-plasmid-cost:\n")

        for j in range(0, len(plasmid_dict['plasmid-cost'])):
            new_content.append("  " + str(plasmid_dict['plasmid-cost'][str(j)]) + ":\n")
            new_content.append("    fixed: " + str(plasmid_dict['fixed'][str(j)]) + "\n")
            new_content.append("    cost: " + str(plasmid_dict['cost'][str(j)]) + "\n")

        config_file = open("config" + str(i+1) + ".yaml", "w") 
        config_file.writelines(new_content)

        config_file.close()   