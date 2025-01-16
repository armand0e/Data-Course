
import string
data = 'Jack and jill were walking up the hill on the way to the Supermarket to get some mineral water when Jack tripped over a pothole in the road.He fell down and broke his smartphone.    "Oh dear!" said jack;actually,he didn’t say "Oh dear",he used some words that Jill was sure his mother wouldn’t approve of and went on to make some descriptive comments on what he thought of the state of the roads leading up the hill.jill was so shocked that she didn’t look where she was going and fell down,too, tumbling all the way down the hill;  jack got up and went home to mend his phone.    jill suggested using her granny’s remedy of vinegar and brown paper to fix the phone; Jack replied with a comment that got him grounded for a week during which time he repaired his phone with duct tape and superglue but it was never the same again .'
# ====================================
# Do not change the code before this

def replace_names(data, names):
    # find each lowercase name in our data, replace with a correctly capitalized name from our name dicitionary
    for i in names:
        data = data.replace(i, names[i])
    return data

def fix_punctuation(data):
    # replace all semicolons with periods
    quotation_num = 0
    data = data.replace(';', '.')
    # for each character in data 
    for i in range(len(data)):
        # if the character is punctuation
        if data[i] in string.punctuation:
            if data[i] == '"':
                quotation_num += 1
            # make sure the next character exists
            if i + 1 < len(data):
                # if the next character is not punctuation, whitespace
                if data[i+1] not in string.punctuation + string.whitespace:
                    # if the character isn't the starting quotation mark dont add a space after it
                    if data[i] == '"' and quotation_num % 2 != 0:
                        continue
                    # add a space after the punctuation
                    data = data[:i+1] + ' ' + data[i+1:]
                    
                # make sure there isn't any duplicate punctuation
                if data[i] == data[i+1]:
                    data = data[:i] + data[i+2:]
    return data

def fix_sentences(data):
    sentences = data.split('.')
    # for each sentence in the list of sentences
    for i in range(len(sentences)):
        sentence = sentences[i]
        # if the sentence is empty, or only 1 character, skip it
        if len(sentence) <= 1:
            continue
        # fix the spacing of each sentence
        sentence = sentence.strip()
        # replace the first character of the sentence with an uppercase version
        new_sentence = sentence[0].upper() + sentence[1:]
        sentence = new_sentence
        sentences[i] = sentence
    # concatenate the list of sentences into a single string with ".  " between each sentence
    return '.  '.join(sentences)

# ====================================
# Do not change the code after this

def ocr_format(text):
    '''
    Return a string containing the text formatted as follows:
    - Sentences must start with a capital letter.
    - Sentences must be separated by two spaces.
    - Commas must be followed by a single space.
    - Semi-colons must be replaced with full stops.
    - Duplicate punctuation must be removed.

    Hint: You will need to write a lookup list into your code 
          so that you can check for proper names and ensure that 
          they are capitalised appropriately.

    Arguments
    text: a string of text received from the OCR

    Examples 
    ocr_format(data) returns the following formatted string
    'Jack and Jill were walking up the hill on the way to the Supermarket to get some mineral water when Jack tripped over a pothole in the road.  He fell down and broke his smartphone.  "Oh dear!" said Jack.  Actually, he didn’t say "Oh dear", he used some words that Jill was sure his mother wouldn’t approve of and went on to make some descriptive comments on what he thought of the state of the roads leading up the hill.  Jill was so shocked that she didn’t look where she was going and fell down, too, tumbling all the way down the hill.  Jack got up and went home to mend his phone.  Jill suggested using her granny’s remedy of vinegar and brown paper to fix the phone.  Jack replied with a comment that got him grounded for a week during which time he repaired his phone with duct tape and superglue but it was never the same again.  '
    '''
    # ====================================
    # Do not change the code before this
    
    names = { 'jack' : 'Jack',  'jill' : 'Jill'}
    text = fix_punctuation(text)
    text = replace_names(text, names)
    text = fix_sentences(text)
    return text
    
def main():
    print(ocr_format(data))

if __name__ == '__main__':
    main()


