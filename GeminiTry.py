import google.generativeai as genai
from pathlib import Path
from textExtractor  import  TextExtractor
#as TextExtractor
genai.configure(api_key="AIzaSyBV7jCQG0bTndlhcHGkPy-8Ev1nRWhFFz0")


def get_java_files(directory):
    path = Path(directory)
    java_files = list(path.rglob('*.java'))
    return java_files



    #genai.upload_file(media / "Prompt.txt")

if __name__ == "__main__":
    files = get_java_files("/Users/salmaameer/Graduation Project/firstAttempt/JavaProject")
    txtFiles =[]
    for file in files:
        filePath = Path(file)
        file_name = filePath.stem+'.txt'
        Extractor = TextExtractor(file,file_name)
        Extractor.convert_java_to_txt()
        media = Path("/Users/salmaameer/Graduation Project/firstAttempt")
        f = genai.upload_file(media / file_name)
        txtFiles.append(f)

    
    model = genai.GenerativeModel("gemini-1.5-flash")
    nestedList = ["in only 100 words Detect if there is any SOLID principle violation",txtFiles]
    flatPrompt = [item for sublist in nestedList for item in sublist]
    response = model.generate_content(flatPrompt)
    print(response.text)



