'''Importing os to readfiles using os.listdir()'''
'''Importing re because I used regular expression after reading line.'''
import os
import re
'''Defined a method to get all input files. Looping through directory to get input files and calling familyrelation function to execute main code.'''
'''Used try, except to catch errors and handle.'''
def getInputFiles():
    for file in os.listdir("."):
        if file.startswith("t6") and file.endswith(".dat"):
            try:
                if os.path.getsize(file)==0:
                    raise TypeError("File is Empty")
                else:
                    familyRelation(file)
            except Exception as err:
                print(err)
            finally:
                print("----------")

'''Declared dictionaries which will be used in main code to get relations.'''
genders={'mother':'F','father':'M','son':'M','daughter':'F','brother':'M','sister':'F','husband':'M','wife':'F'}
reverses={'mother':'child','father':'child','son':'parent','daughter':'parent','brother':'sibling','sister':'sibling','husband':'spouse','wife':'spouse'}
supers={'mother':'parent','father':'parent','son':'child','daughter':'child','brother':'sibling','sister':'sibling','husband':'spouse','wife':'spouse'}

'''Defined Propogate methode to add all relations into respective dictionaries.'''
def propogate(hash):
    #propagating siblings to parents children.
    for parent in hash["child"].keys():
        children=hash["child"][parent]
        otherchildren=set()
        for child in children:
            if child in hash["sibling"].keys():
                sibling=hash["sibling"][child]
                otherchildren=otherchildren.union(sibling)
        children=children.union(otherchildren)
        hash["child"].update({parent:children})

    # propogating child's parent's spouse as his own parent
    for child in hash["parent"].keys():
        parents = hash["parent"][child]
        otherparent = set()
        for spouse in parents:
            if spouse in hash["spouse"].keys():
                parentspouse = hash["spouse"][spouse]
                otherparent = otherparent.union(parentspouse)
        parents = parents.union(otherparent)
        hash["parent"].update({child: parents})

    # propogating spouse's children as his own children
    for person in hash["spouse"].keys():
        personspouse=hash["spouse"][person]
        otherchildren=set()
        for spouse in personspouse:
            if spouse in hash["child"].keys():
                spousechildren=hash["child"][spouse]
                otherchildren=otherchildren.union(spousechildren)
        if person in hash["child"].keys():
            t=hash["child"][person]
            x=t.union(otherchildren)
            hash["child"].update({person:x})
        elif len(otherchildren)!=0:
            hash["child"].update({person:otherchildren})

    #propogating person's siblings parents and person's parents
    for person in hash["sibling"].keys():
        t=person
        siblings=hash["sibling"][person]
        othersiblingparent=set()
        for sibling in siblings:
            if sibling in hash["parent"].keys():
                siblingparents=hash["parent"][sibling]
                othersiblingparent=othersiblingparent.union(siblingparents)
        if person in hash["parent"]:
            x=hash["parent"][person]
            y=x.union(othersiblingparent)
            hash["parent"].update({person:y})
        elif len(othersiblingparent)!=0:
            hash["parent"].update({t:othersiblingparent})

    #propogating spouse hash frm parents hash.
    for person in hash["parent"].keys():
        parents=hash["parent"][person]
        if len(parents)==2:
            res=[]
            for k in parents:
                var1=k
                res.append(var1)
            hash["spouse"].update({res[0]:res[1]})
            hash["spouse"].update({res[1]:res[0]})
            for l in hash["spouse"].keys():
                if l in hash["gender"]:
                    gen=hash["gender"][l]
                    oppgen="M" if gen=="F" else "F"
                    spouseofl=hash["spouse"][l]
                    if spouseofl not in hash["gender"].keys():
                        hash["gender"].update({spouseofl:oppgen})

'''InitializeHash is a method to reset all dictionaries after executing one file and ready to store next file inputs.'''
hash={}
def initializeHash():
    hash["child"]={}
    hash["parent"]={}
    hash["spouse"]={}
    hash["gender"]={}
    hash["sibling"]={}

'''Main fnction to accept input file and store all relations in respective dictionaries.'''
'''Used Regex function to get the input line in desired format and handle all whitespaces, digits and tabs and starts executing.'''
'''Raised errors if the file contains any digits or alphanumeric values or if it is illegal.'''
def familyRelation(filepath):
    initializeHash()
    with open(filepath) as f:
        for lines in f.readlines():
            line=lines.lower()
            endwith=line.strip()[-1]
            if endwith==".":
                match=re.match(r'^[\s]*([a-z]+)\'s[\s]+([a-z]+)[\s]+is[\s]+([a-z]+)[\s]*\.[\s]*$', line)
                if match:
                    relation = match.group(2)
                    person1=match.group(1)
                    person2=match.group(3)
                    # print("relation",relation, "person1", person1, "person2", person2)
                    #Checking relation in supers dict
                    if relation in supers:
                        superkey=supers.get(relation)
                        updateHash(person1,person2,superkey)
                    if relation in genders:
                        genderkey=genders.get(relation)
                        if relation=="husband" or relation=="wife":
                            oppgender = "M" if genderkey == "F" else "F"
                            if person1 not in hash["gender"]:
                                hash["gender"].update({person1:oppgender})
                            else:
                                if hash["gender"][person1]!=oppgender:
                                    raise TypeError("Gender Conflicts")
                        if person2 not in hash["gender"]:
                            hash["gender"].update({person2:genderkey})
                        else:
                            if hash["gender"][person2]!=genderkey:
                                raise TypeError("Gender Conflicts")
                    #checking relation in reverse dict
                    if relation in reverses:
                        reversekey=reverses.get(relation)
                        updateHash(person2,person1,reversekey)
                else:
                    raise TypeError("Illegal File")
            elif endwith=="?":
                propogate(hash)
                match=re.match(r'^[\s]*who[\s]+is[\s]+([a-z]+)\'s+[\s]+([a-z]+)[\s]*\?[\s]*$', line)
                if match:
                    relation1= match.group(2)
                    person1=match.group(1)
                    #print("relation",relation1,"person1",person1)
                    if relation1 in supers:
                        superkey2=supers.get(relation1)
                        if person1 not in hash[superkey2]:
                            print("Unknown")
                            break
                        output=hash[superkey2][person1]
                        if relation1 in genders:
                            genderkey2=genders.get(relation1)
                            answer=''
                            for i in output:
                                if hash["gender"].get(i)==genderkey2:
                                    answer=i.title()
                            if answer:
                                print(answer)
                            else:
                                print("Gender Unknown")
                        else:
                            raise TypeError("Relation not found in genders")
                    else:
                        raise TypeError("Output Unknown")
                else:
                    raise TypeError("Illegal file")
            else:
                raise TypeError("Illegal file")

'''updateHash is a method to store key,value pair into dictionaries which relations are in supers and reverses.'''
'''Calling this function in main function where relation is in supers and reverses.'''
def updateHash(key,val,relationkey):
    if key not in hash[relationkey]:
        hash[relationkey].update({key:{val}})
    else:
        hash[relationkey][key].add(val)


getInputFiles()



