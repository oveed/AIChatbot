import openai
import config
openai.api_key = config.api_key
print("What is your name? ")
name=input()
print("What is your age? ")
age=int(input())
print("What is your hobby? What are you interested in?")
hobby=input()
info = 'what is the best programming language for a ' + str(age) + ' yo person who is interested in ' + hobby + " in one word"
# Choosing the programming launguage 
completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": info }]
    )
result = completion['choices'][0]['message']['content']
print("\n Hello " + name + ", the best tool / programming language for you to dive into the world of programming is : " + result )

# Getting started
print("\n Do you want to get started with " + result + "?" + "\n (Y/n): ")
if input() == "Y" :
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": " \n how to get started with " + result + " keep it short \n" }]
    )
    print(completion['choices'][0]['message']['content'])

    # First project
    print(" \nAre you ready to start your first project? " + "\n (Y/n): ")
    if input() == "Y" :
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "\n Give me a first project with " + result + " keep it short \n" }]
        )
        paragraph=completion['choices'][0]['message']['content']
        def remove(text, target):
            modified_text = text.replace(target, '')
            return modified_text
        modified_paragraph = remove(paragraph, '```'+result)
        modified_paragraph = remove(paragraph, '```')
        print(modified_paragraph)
        
        # More projects
        print(" \n More projects? " + "\n (Y/n): ")
        x=input()
        while x=="Y":
            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "\n Give me a medium difficulty project with " + result + " keep it short \n" }]
            )
            paragraph=completion['choices'][0]['message']['content']
            def remove(text, target):
                modified_text = text.replace(target, '')
                return modified_text
            modified_paragraph = remove(paragraph, '```'+result)
            modified_paragraph = remove(paragraph, '```')
            print(modified_paragraph)
            print(" \n More projects? " + "\n (Y/n): ")
            x=input()
        print("Any questions? \n")
        question=input()
        if question.upper()=="NO":
            print("Okay, Glad I helped.")
        else:
            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question }]
            )
            print(completion['choices'][0]['message']['content'])
    else:
        print("Any questions? \n")
        question=input()
        if question.upper()=="NO":
            print("Okay, Glad I helped.")
        else:
            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question }]
            )
            print(completion['choices'][0]['message']['content'])
        
else:
    print("Any questions? \n")
    question=input()
    if (question.upper()=="NO") or (question.upper()=="N"):
        print("Okay, glad I helped. \n \n \n ")
    else:
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question }]
        )
        print(completion['choices'][0]['message']['content'])

    
