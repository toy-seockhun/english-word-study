import random

if __name__ == '__main__':
    while True:
        m = input("mode >> 1.add 2.arrange 3.test :: ")

        if m == "add" or m == "1" or m == "ADD":
            f = open('words.txt', 'a')
            while True:
                line = input("input contents as format word/mean >> ")
                if not line: break
                f.write(line + '\n')
            f.close()

        elif m == "arrange" or m == "2" or m == "ARRANGE":
            f = open('words.txt', 'r')
            while True:
                line = f.readline()
                if not line: break
                print(line.split('/')[0], end='')
                input(' / ')
                print(line.split('/')[1], end='')
            f.close()

        elif m == "test" or m == "3" or m =='test':
            f = open('words.txt', 'r')
            wordset = f.readlines()
            random.shuffle(wordset)
            k = int(input('input test size >> '))
            if len(wordset) < k:
                print('WORDSET MAX SIZE IS %d' % len(wordset))
                k = len(wordset)

            for i in range(k):
                line = wordset[i]
                if not line: break
                print(line.split('/')[0], end='')
                input(' / ')
                print(line.split('/')[1], end='')
            f.close()
        
        else: break