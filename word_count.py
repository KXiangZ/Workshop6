text_input=input("Enter text:").strip()
text_store=text_input.split(" ")
count_dict={}

for text in text_store:
    if text in count_dict:
        count_dict[text]+=1
    else:
        count_dict[text]=1

for text,count in sorted(count_dict.items()):
    print(text+":"+str(count)+"\n")
