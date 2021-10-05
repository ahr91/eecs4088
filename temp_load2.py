import json
from nltk.tokenize import sent_tokenize
import gzip
#from io import StringIO


question = []
shortAnswer = []
longAnswer = []
shortAnswerModified = []
sample = []
anatCounter = 0
counter = 0


mFileName = 'nq-train-00.jsonl.gz'
for i in range(50):
    if i<10:
        mFileName = 'nq-train-0%d.jsonl.gz' % i
    else:
        mFileName = 'nq-train-%2d.jsonl.gz' % i

    with gzip.open(mFileName , 'rb') as mother_file:
    #with open('v1.0-simplified_simplified-nq-train.jsonl') as mother_file:
        #io = StringIO(json_file)
        #data = json.load(io)
        #data = json.load(json_file)
        lines = mother_file.readlines()
        for line in lines:

            #for p in data[0]:
            data = json.loads(line)
            #question.append(data[0])
            #shortAnswer.append(data[1])
            # shortAnswerSentences = sent_tokenize(p['long answer'])
            #longAnswer.append(data[2])
        
            #if str(line).find('Antarctica') != -1:
            #    print(data)
            #    sample = data
            if str(line).find('who lives in the imperial palace in tokyo?') != -1:
                anatCounter = anatCounter + 1
                sample.append(str(data))
                print(str(line) + "\n\n\n")
                #for key in list(data.keys()):

            counter  = counter + 1


            #print(list(data.keys()))
            #if shortAnswer[-1].strip() != "None":
            #    shortAnswerModified.append(longAnswer[-1])
            #else:
                #for sentence in longAnswerSentences:
                #    index = sentence.find(p['short answer'])
                #    if index != -1:
                #        longAnswerModified.append(sentence)
                #        break

            #    index = data[2].find(data[1])
            #    startingIndex = data[2].rfind(".", 0, index) + 1
            #    endingIndex = data[2].find(".", index + len(data[1])) + 1
            #    shortAnswerModified.append(data[2][startingIndex : endingIndex].strip())




print("Counter:")
print(counter)
print("\nAntarctica Counter:")
print(anatCounter)

#with open('question.txt', 'w', encoding="utf-8") as outfile:
#    outfile.write("\n".join(question))

#with open('shortAnswer.txt', 'w', encoding="utf-8") as outfile:
#    outfile.write("\n".join(shortAnswerModified))

#with open('longAnswer.txt', 'w', encoding="utf-8") as outfile:
#    outfile.write(("\n".join(longAnswer)))


with open('sample.txt', 'w', encoding="utf-8") as outfile:
    outfile.write("\n".join(sample))


#name = jsonObject['name']
#website = jsonObject['website']
#froms = jsonObject['from']

#print(name)
#print(website)
#print(froms)
