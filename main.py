
from  math import sqrt
def is_prime(nr):
    '''
    Verify if a number nr is prime
    :param nr: int
    :return: True if is prime, False otherwise
    '''
    if nr < 2:
        return False
    if nr != 2 and nr % 2 == 0:
        return False
    for d in range(3, int(sqrt(nr)) + 1, 2):
        if nr % d == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(244) == False
    assert is_prime(-5) == False
    assert is_prime(4) == False
    assert is_prime(2) == True
    assert is_prime(37) == True
def super_prim(n):
    if n > 0:
            if is_prime(n):
                return True
            else:
                return False

def lista_super_prime(lst):
    '''
        Returneaza o lista cu numere superprime
        :param lst: intregi
        :return: o lista cu numere superprime
        '''
    rez=[]
    for el in lst:
        if super_prim(el):
            rez.append(el)
    return rez
'''def test_lista_super_prime():
    assert lista_super_prime([3,57,3])==[3,57,3]
    assert lista_super_prime([2,4,67,12])==[2]
    assert lista_super_prime([2,3,5,7])==[2,3,5,7] '''
def min_numar_egal_nr(lst, nr):
    '''
    Det. celui mai mic număr din lst care are ultima cifra egala cu nr citit de la tastatura
    :param lst: int list
    :param nr: int
    :return: int (minimul din lista care are ultima cifra egala cu nr)
    '''
    min = None
    for el in lst:
        int_el = int(el)
        if int_el == nr:
             if min == None or int_el < min:
                min = int_el
    return min
def test_minim_numar_egal_nr():
    assert min_numar_egal_nr([4,34,7,2,65],7)==7
    assert min_numar_egal_nr([2,-5,0,8,23],8)==8
def list_numere_negative_nenule(lst):
    '''
    Return lista de numere negative si nenule
    :param lst: lista de numere intregi
    :return: o lista cu numere intregi negative
    '''
    rez = []
    for el in lst:
            if el < 0:
                rez.append(el)

    return rez
def test_lista_numere_negative_nenule():
    assert list_numere_negative_nenule([2,-5,0,56,23])==[-5]
    assert list_numere_negative_nenule([-5,-7,-4,3])==[-5,-7,-4]
    assert list_numere_negative_nenule([0,4,6,9])==[]
def read_list():
    '''
    Read list of floats
    :return: list of floats
    '''
    # list_str = input("Enter list items: ").split(" ")
    # lst = []
    # for el in list_str:
    #     lst.append(float(el))

    lst = [int(e) for e in input("Introduceti elementele listei: ").split(",")]
    return lst
def show_menu():
    '''
    Print menu
    :return:
    '''
    print('''
1. Citeste lista
2. Afișarea tuturor numerelor negative nenule din lista 
3. Afișarea celui mai mic numar care are ultima cifra egala cu un numar citit de la tastatura.
4. Afișarea tuturor numerelor care sunt superprime.
5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
6. Afisare lista
x. Iesire
    ''')
def main():
    lst = []
    while True:
        show_menu()
        cmd = input("Alegeti optiunea: ")
        if cmd == '1':
            lst = read_list()
        elif cmd == '2':
            rez = list_numere_negative_nenule(lst)
            print(rez)
        elif cmd == '3':
            nr = int(input("Introduceti  nr"))
            rez = min_numar_egal_nr(lst,nr)
            print(rez)
        elif cmd == '4':
            rez = lista_super_prime(lst)
            print(rez)
        elif cmd == '5':
            #rez = list_parte_intrega_nr_prim_caractere_invers(lst)
            print(rez)
        elif cmd == '6':
            print(lst)
        elif cmd == 'x':
            break
        else:
            print("Invalid command")
def run_tests():
    test_is_prime()
    test_lista_numere_negative_nenule()
    #test_lista_super_prime()
    test_minim_numar_egal_nr()

if __name__ == '__main__':
    run_tests()
    main()

