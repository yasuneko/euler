import itertools
import random
import string
import unittest

def answer(document, searchTerms):
    document_list = document.split()

    if len(searchTerms) == 1:
        if searchTerms[0] in document_list:
            return searchTerms[0]
        else:
            return ""

    searchTerms = sorted(searchTerms)

    searchItem_dict = {}
    for item in searchTerms:
        location_list = [i for i, x in enumerate(document_list) if x == item]
        searchItem_dict[item] = location_list

    short_groups = []

    searchItem_list = []
    for key in searchItem_dict:
        searchItem_list.extend(searchItem_dict[key])
    searchItem_list = sorted(searchItem_list)


    location_items = {}
    location_locations = {}
    for searchItem in searchItem_list:
        location_items[searchItem] = set()
        location_items[searchItem].add(document_list[searchItem])
        location_locations[searchItem] = set()
        location_locations[searchItem].add(searchItem)

    for i in range(len(searchItem_list) - 1):
        for j in range(i+1,len(searchItem_list)):
            short_groups.append((searchItem_list[j] - searchItem_list[i], (searchItem_list[i], searchItem_list[j])))

    short_groups = sorted(short_groups)

    complete_list = []
    for i in range(len(short_groups)):
        short_group = short_groups[i]
        front, back = short_group[1]
        if document_list[back] not in location_items[front]:
            location_items[front].add(document_list[back])
            location_locations[front].add(back)

            if sorted(list(location_items[front])) == searchTerms:
                complete_list.append(front)

        if complete_list and ((i + 1 >= len(short_groups)) or (short_groups[i + 1][0] > short_group[0])):
            min_length = None
            min_value = None
            for complete in complete_list:
                x = sorted(list(location_locations[complete]))
                length = x[-1] - x[0]
                if not min_length:
                    min_length = length
                    min_value = complete
                elif min_length > length:
                    min_length = length
                    min_value = complete

            locations = sorted(list(location_locations[min_value]))
            return " ".join(document_list[locations[0]:locations[-1] + 1])

class TestCases(unittest.TestCase):
    def tests(self):
        self.assertEqual(answer("many google employees can program", ["google", "program"]), "google employees can program")
        self.assertEqual(answer(" many google employees can program ", ["google", "program"]), "google employees can program")
        self.assertEqual(answer("world there hello hello where world", ["hello", "world"]), "world there hello")
        self.assertEqual(answer("hopping", ["hop"]), "")
        self.assertEqual(answer("hop", ["hop"]), "hop")
        self.assertEqual(answer("a b c d a", ["a", "c", "d"]), "c d a")
        self.assertEqual(answer("ay bee bee cee ay bee dee bee ay", ["ay", "cee", "dee"]), "cee ay bee dee")
        self.assertEqual(answer("ex wy ay bee zee ay bee cee dee ee eff zee ex ay wy", ["ex", "wy", "zee"]), "zee ex ay wy")
        self.assertEqual(answer("x y a b z a b c w a b c d e f g h i j k l m n o p x y a b c z a w", ["w", "x", "y", "z"]), "x y a b c z a w")
        self.assertEqual(answer("w a x b y c z a b c d e f g h i j k l m n o p w x a b y c d z", ["w", "x", "y", "z"]), "w a x b y c z")
        self.assertEqual(answer("w a b x z y y z a b c w", ["w", "x", "y", "z"]), "w a b x z y")
        self.assertEqual(answer("x a b y z y a x", ["x", "y", "z"]), "z y a x")
        self.assertEqual(answer("x a b c d e f g h y i j k l m z", ["x", "z"]), "x a b c d e f g h y i j k l m z")
        self.assertEqual(answer("x a b c d e f g h y i j k l m z", ["x", "y", "z"]), "x a b c d e f g h y i j k l m z")
        self.assertEqual(answer("x a b c d e f g h y i j k l m z", ["y"]), "y")
        self.assertEqual(answer("a b a b a b a b a b a b", ["a", "b"]), "a b")
        self.assertEqual(answer("b a b a b a b a b a b", ["a", "b"]), "b a")
        self.assertEqual(answer("a b c d d", ["a", "b", "c", "d"]), "a b c d")
        self.assertEqual(answer("d y z c x a b x c y z d", ["a", "b", "c", "d"]), "d y z c x a b")
        self.assertEqual(answer("d y z c a x b c y z d", ["a", "b", "c", "d"]), "d y z c a x b")
        self.assertEqual(answer("b x y a c z a c eff zee d", ["a", "b", "c", "d"]), "b x y a c z a c eff zee d")
        self.assertEqual(answer("a aa aaa b c d", ["a", "aa", "b", "c", "d"]), "a aa aaa b c d")
        self.assertEqual(answer("a a b b x c y d d e e", ["a", "b", "c", "d", "e"]), "a b b x c y d d e")
        self.assertEqual(answer("a b c d", ["a", "b", "c", "d"]), "a b c d")
        self.assertEqual(answer("a b c", ["a", "b", "c"]), "a b c")

if __name__ == '__main__':
    #unittest.main()
    #bqwdz a bh bh uatftfs a bh bh uatftfs a a uatftfs a uatftfs a uatftfs a bqwdz bqwdz a a bqwdz bqwdz bh a ['bh', 'a', 'a', 'uatftfs', 'bqwdz']
    #document = "dnuezhsusq jxhqebl orobdws dnuezhsusq zzdq nniz g dnuezhsusq g jxhqebl o orobdws dpzq g zzdq jxhqebl orobdws dnuezhsusq nniz g zzdq jxhqebl dnuezhsusq o o g g g o g zzdq g orobdws zzdq dpzq dpzq g nniz g nniz dpzq orobdws g jxhqebl g nniz g g o dpzq"
    #terms = ['g', 'g', 'o', 'zzdq', 'orobdws', 'g', 'dnuezhsusq', 'dpzq', 'jxhqebl', 'nniz']
    #print answer(document, terms)
    #exit()
    #document = "ltuwfg jndrkmm wrqqatiggf dlauachngc dlauachngc vha dfttmabjsm tnappdlo j oemksos f dyacxq vajqivhnp axsffjjeju bgsqmofsu vem jqnv vem bgsqmofsu oemksos dfttmabjsm vem vajqivhnp jndrkmm dlauachngc athh athh dlauachngc dyacxq tnappdlo ltuwfg qrvq j vha axsffjjeju bgsqmofsu f ltuwfg axsffjjeju dfttmabjsm wrqqatiggf oemksos oemksos axsffjjeju dfttmabjsm dyacxq athh axsffjjeju f j jqnv f wrqqatiggf ro tnappdlo vem ltuwfg j tnappdlo jndrkmm dyacxq ro wrqqatiggf athh qrvq ltuwfg qrvq ro jqnv j vajqivhnp vha vha f f f vajqivhnp jndrkmm f vem dyacxq tnappdlo ro jndrkmm wrqqatiggf dfttmabjsm f ro dlauachngc bgsqmofsu jqnv vha bgsqmofsu qrvq f oemksos vajqivhnp athh jqnv qrvq"
    #terms = ['f', 'ltuwfg', 'dyacxq', 'dlauachngc', 'tnappdlo', 'axsffjjeju', 'wrqqatiggf', 'vajqivhnp', 'qrvq', 'vha', 'jqnv', 'jndrkmm', 'j', 'athh', 'oemksos', 'bgsqmofsu', 'ro', 'vem', 'f', 'dfttmabjsm']
    #print answer(document, terms)

    #exit()
    terms = set()
    term_count = 100
    while len(terms) < term_count:
        terms.add(''.join(random.choice(string.ascii_lowercase) for x in range(random.randint(1, 10))))
    print len(terms)
    document = []
    for term in terms:
        document.extend([term] * 5)

    print len(document)
    random.shuffle(document)

    document = " ".join(document)

    print document, terms
    print answer(document, terms)

    exit()

    extra_count = random.randint(term_count,500)
    extra = []
    for l in range(extra_count):
        extra.append(''.join(random.choice(string.ascii_lowercase) for x in range(random.randint(1, 10))))

    print term_count, extra_count

    document = terms + extra

    random.shuffle(document)
    document = " ".join(document)
    print document, terms
    print answer(document, terms)

    exit()
    #terms = ["aa", "bb", "cc", "dd", "ee"]
    #extra = ["ww", "xx", "yy", "zz"]
    for k in range(1):
        document = []
        for term in terms + extra:
            print [term] * random.randint(1, 10)
            document.extend([term] * random.randint(1, 10))
        random.shuffle(document)
        document = " ".join(document)
        print document, terms
        print answer(document, terms)
    '''
    document = terms + terms + terms + ["ww", "xx", "yy", "zz"] + ["ww", "xx", "yy", "zz"] + ["ww", "xx", "yy", "zz"] + ["ww", "xx", "yy", "zz"]
    for k in range(1000):
        document = terms + terms + terms + ["ww", "xx", "yy", "zz"] + ["ww", "xx", "yy", "zz"] + ["ww", "xx", "yy", "zz"] + ["ww", "xx", "yy", "zz"]
        random.shuffle(document)
        document = " ".join(document)

        print document, terms
        print answer(document, terms)
    '''
