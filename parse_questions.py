def parse_to_csv(file_f):
    f = open(file_f, 'r')
    files = f.readlines()
    f.close()
    new = open('parsed.txt', 'w')
    for text in files:
        text = text.strip()
        question_text = text[text.find(':')+1:text.find('Answer')].strip()
        option = text[text.find('Option'):text.find('Correct')].split("Option")
        options = list(map(lambda a: a.strip(), option))
        options_list = list(filter(None, options))
        correct = int(float(text[-1]))
        print(correct)
        title = ['NewQuestion,MC,,,\n', 'QuestionText,{},,,\n'.format(question_text), 'Points,1,,,\n', 'Difficulty,1,,,\n']
        i = 0
        option_row = []
        while i < len(options_list):
            point = 0
            if i == (correct - 1):
                point = 100
            word = 'Option,' + str(point) + ',' + options_list[i]+',,\n'
            option_row.append(word)
            i += 1
        final = title + option_row + [',,,,\n,,,,\n']
        new.writelines(final)
    new.close()
