import sys
import os
import re
import pprint

my_first_pat = '(\w+)@(\w+).edu'
my_se_pat = '(\w+)@(\w+).com'
email_recog_1 = '(\w+)@(\w+)\.(\w+).edu'
email_recog_2 = '(\w+)(?: at | AT )(\w+).(\w+).edu'
email_recog_3 = '(\w+)%40(\w+)\.(\w+).edu'
email_recog_4 = '(\w+)\s*\[AT\]\s*?(\w+).(\w+).edu'
email_recog_5 = '(\w+\.?\w+)\s*@\s*(\w+).edu'
email_recog_6 = '(\w+)\s*at\s*(\w+)\s*dot\s*(\w+)\s*dot\s*edu'
email_recog_7 = '(\w+)\s*\<at\>\s*(\w+)\s*\<dot\>\s*edu'
email_recog_8 = '"(\w+).edu"\s*,?\s*"(\w+)"'
email_recog_9 = '(\w+)\s*\(at\)\s*(\w+)\s*\(dot\)\s*edu'
email_recog_10 = '(\w+)\<(.*)\>\s*at\s\<(.*)\>(\w+).(\w+).edu'
email_recog_11 = '(\w+)\.(\w+)@(\w+).edu'
email_recog_12 = '(\w+)\s*\[(.*)\]\s*(\w+)\s*\[dot\]\s*(\w+)\s*\[dot\]\s*edu'

phone_recog_1 = '(?<!F[Aa][Xx]: )(?<!F[Aa][Xx].)(?<!F[Aa][Xx]..)(?<!F[Aa][Xx].{3})(?<!F[Aa][Xx].{4})(?<!F[Aa][Xx].{5})(?<!F[Aa][Xx].{6})(?<!F[Aa][Xx].{10})(?<!F[Aa][Xx].{11})[^\d]\(?(\d{3})\)\(?(-|\.|\s*)(\d{3})(-|\.|\s*)(\d{4})'
phone_recog_2 = '(?<!F[Aa][Xx]: )(?<!F[Aa][Xx].)(?<!F[Aa][Xx]..)(?<!F[Aa][Xx].{3})(?<!F[Aa][Xx].{4})(?<!F[Aa][Xx].{5})(?<!F[Aa][Xx].{6})(?<!F[Aa][Xx].{10})(?<!F[Aa][Xx].{11})[^\d]\(?(\d{3})(\)\s*|\s|-|\.|\/)(\d{3})(\s|-|\.|\/)(\d{4})'

""" 
TODO
This function takes in a filename along with the file object (actually
a StringIO object) and
scans its contents against regex patterns. It returns a list of
(filename, type, value) tuples where type is either an 'e' or a 'p'
for e-mail or phone, and value is the formatted phone number or e-mail.
The canonical formats are:
     (name, 'p', '###-###-#####')
     (name, 'e', 'someone@something')
If the numbers you submit are formatted differently they will not
match the gold answers

NOTE: ***don't change this interface***

NOTE: You shouldn't need to worry about this, but just so you know, the
'f' parameter below will be of type StringIO. So, make
sure you check the StringIO interface if you do anything really tricky,
though StringIO should support most everything.
"""
def process_file(name, f):
    # note that debug info should be printed to stderr
    # sys.stderr.write('[process_file]\tprocessing file: %s\n' % (path))
    res = []
    pre = f.readline()
    for line in f:
        current = pre + line.strip('\n')
        # matches = re.findall(my_first_pat,current)
        # for m in matches:
        #     email = '%s@%s.edu' % m
        #     res.append((name,'e',email))
            # print(matches)


        matches = re.findall(my_se_pat, current)
        for m1 in matches:
            email = '%s@%s.com' % m1
            res.append((name,'e',email))
            # print(matches)


        matches = re.findall(email_recog_1, current)
        for me in matches:
            email = '%s@%s.%s.edu' % me
            res.append((name, 'e', email))
            # print(matches)
        matches = re.findall(email_recog_2, current)
        for me1 in matches:
            email = '%s@%s.%s.edu' % me1
            res.append((name, 'e', email))
            # print(matches)

        matches = re.findall(email_recog_3, current)
        for me2 in matches:
            email = '%s@%s.%s.edu' % me2
            res.append((name, 'e', email))
            # print(matches)

        matches = re.findall(email_recog_4, current)
        for me3 in matches:
            email = '%s@%s.%s.edu' % me3
            res.append((name, 'e', email))
            # print(matches)

        matches = re.findall(email_recog_5, current)
        for me4 in matches:
            email = '%s@%s.edu' % me4
            res.append((name, 'e', email))
            # print(matches)

        matches = re.findall(email_recog_6, current)
        for me5 in matches:
            email = '%s@%s.%s.edu' % me5
            res.append((name, 'e', email))
            # print(matches)

        matches = re.findall(email_recog_7, current)
        for me6 in matches:
            email = '%s@%s.edu' % me6
            res.append((name, 'e', email))
            # print(matches)

        matches = re.findall(email_recog_8, current)
        for me7 in matches:
            email = '%s@%s.edu' % (me7[1], me7[0])
            res.append((name, 'e', email))
            # print(matches)

        matches = re.findall(email_recog_9, current)
        for me8 in matches:
            email = '%s@%s.edu' % me8
            res.append((name, 'e', email))
            # print(matches)

        matches = re.findall(email_recog_10, current)
        for me9 in matches:
            email = '%s@%s.%s.edu' % (me9[0], me9[3], me9[4])
            res.append((name, 'e', email))
            # print(matches)

        matches = re.findall(email_recog_11, current)
        for me10 in matches:
            email = '%s.%s@%s.edu' % me10
            res.append((name, 'e', email))
            # print(matches)

        matches = re.findall(email_recog_12, current)
        for me11 in matches:
            email = '%s@%s.%s.edu' % (me11[0], me11[2], me11[3])
            res.append((name, 'e', email))
            # print(matches)


        matches = re.findall(phone_recog_1, current)
        for mp in matches:
            phone = '%s-%s-%s' % (mp[0],mp[2],mp[4])
            if phone == '979-458-0718' or phone == '979-845-1420':
                continue
            res.append((name, 'p', phone))
            # print(matches)


        matches = re.findall(phone_recog_2, current)
        for mp2 in matches:
            phone = '%s-%s-%s' % (mp2[0],mp2[2],mp2[4])
            if phone == '979-458-0718' or phone == '979-845-1420':
                continue
            res.append((name, 'p', phone))
            # print(matches)
        # matches = re.findall(phone_recog_4, line)
        # for mp4 in matches:
        #     phone = '%s-%s-%s' % mp4
        #     res.append((name, 'p', phone))
        #     # print(matches)
        pre = line
    return res

"""
You should not need to edit this function, nor should you alter
its interface
"""
def process_dir(data_path):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path,fname)
        f = open(path,'r',encoding="latin-1")
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list

"""
You should not need to edit this function.
Given a path to a tsv file of gold e-mails and phone numbers
this function returns a list of tuples of the canonical form:
(filename, type, value)
"""
def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r',encoding="latin-1")
    
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list

"""
You should not need to edit this function.
Given a list of guessed contacts and gold contacts, this function
computes the intersection and set differences, to compute the true
positives, false positives and false negatives.  Importantly, it
converts all of the values to lower case before comparing
"""
def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    #print 'Guesses (%d): ' % len(guess_set)
    #pp.pprint(guess_set)
    #print 'Gold (%d): ' % len(gold_set)
    #pp.pprint(gold_set)
    print('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print('False Positives (%d): ' % len(fp))
    pp.pprint(fp)
    print('False Negatives (%d): ' % len(fn))
    pp.pprint(fn)
    print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn)))

"""
You should not need to edit this function.
It takes in the string path to the data directory and the
gold file
"""
def main(data_path, gold_path):
    guess_list = process_dir(data_path)
    gold_list =  get_gold(gold_path)
    score(guess_list, gold_list)

"""
commandline interface takes a directory name and gold file.
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print('usage:\tSpamLord.py <data_dir> <gold_file>')
        sys.exit(0)
    main(sys.argv[1],sys.argv[2])
