
result = ['assignment_id,highest_grade']

with open('data1.yml') as f:
    lines = f.readlines()
    curPath = "data1.yml"
    curNest = [{"leadingSpaces": -1, "name": "data1.yml"}]

    numberOfLines = len(lines)
    i = 0
    while i < numberOfLines:
        line = lines[i]
        leadingSpaces = len(line) - len(line.lstrip())
        
        while curNest[-1]['leadingSpaces'] >= leadingSpaces:
            curNest.pop()
        curNest.append({"leadingSpaces": leadingSpaces, "name": line.split(':')[0].strip()})
        
        if line.strip().startswith('assignment'):
            j = i + 1
            highScore = -1
            highStudent = ""

            while j < numberOfLines:
                scoreLine = lines[j]
                if scoreLine.strip() == "":
                    break
                
                leadingSpaces = len(scoreLine) - len(scoreLine.lstrip())
                if  leadingSpaces <= curNest[-1]['leadingSpaces']:
                    break
                
                score = float(scoreLine[:-1].split(": ")[1])
                if score > highScore:
                    highScore = score
                    highStudent = scoreLine.split(": ")[0].strip()
                
                j = j + 1
            
            output = "\""
            for dir in curNest:
                output += dir['name']
                if dir['name'].startswith('assignment') == False:
                    output += "/"
            output += "\"," + highStudent
            
            result.append(output)
            i = j
            continue
        i = i + 1

with open("output.csv", "w") as myfile:
    lst = map(str, result)  
    line = "\n".join(lst)
    myfile.write(line)
    



    
