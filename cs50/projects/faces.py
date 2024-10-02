def main():
    ask = input()  
    converted_text = convert(ask)  
    print(converted_text)  

def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

main()
