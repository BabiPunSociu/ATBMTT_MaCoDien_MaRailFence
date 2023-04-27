
# Rail Fence

def showMenu():
    print('Chon cac chuc nang sau')
    print('1. Ma hoa')
    print('2. Giai ma')
    print('0. Thoat')
    return int(input('Lua chon cua ban la: '))  # luaChon

def nhapSoNguyen(mes):
    while True:
        a = input(mes).strip()
        try:
            a = int(a)
            return a 
        except ValueError:
            print('Loi. Ban phai nhap so')
       
def inmtran():
    global mtran
    for x in mtran:
        print(x)

def ma_hoa(str_, khoa):
    global mtran

    # Tao ma tran rong kich thuoc: khoa x len(str_) 
    mtran = [[' ' for i in range(len(str_))] for j in range(khoa)]

    ban_ma = '' 
    di_xuong = True # Nghich bien
    i,j = 0,0   # Toa do de duyet ma tran
    # Xep cac chu cai o ban ro vao cac vi tri de tao thanh duong zic-zac (hinh giong chu W)
    for c in str_:
        mtran[i][j] = c 
        if i == 0:
            di_xuong = True
        if i == len(mtran)-1:
            di_xuong = False

        if di_xuong == True:
            i += 1
        if di_xuong == False:
            i -= 1
        j += 1

    for c in mtran:
        for x in c:
            if x != " ":
                ban_ma += str(x)
    return ban_ma


def giai_ma(str_, khoa):
    global mtran

    # Buoc 1: Tao ma tran rong kich thuoc: khoa x len(str_) 
    mtran = [[' ' for i in range(len(str_))] for j in range(khoa)]
    
    # Buoc 2: Dien cac '*' vao cac vi tri danh dau thanh duong zic-zac:
    di_xuong = True # Nghich bien
    i,j = 0,0   # Toa do de duyet ma tran
    # Xep cac '*' vao cac vi tri de tao thanh duong zic-zac (hinh giong chu W)
    for x in range(len(str_)):
        mtran[i][j] = '*' 
        if i == 0:
            di_xuong = True
        if i == len(mtran)-1:
            di_xuong = False

        if di_xuong == True:
            i += 1
        if di_xuong == False:
            i -= 1
        j += 1
    inmtran()
    print()
    # Buoc 3: Duyet lan luot cac vi tri của mtran de dien ban_ma vao cac vi tri
    index = 0 # Tao chi so index de duyet cac vi tri của string ban_ma
    for i in range(khoa):
        for j in range(len(str_)):
            if mtran[i][j] == '*':
                mtran[i][j] = str_[index]
                index += 1
    inmtran()

    # Buoc 4: Duyet ma tran, doc ket qua theo hinh zic-zac va tra ve ket qua -> ban ro
    ban_ro = ""
    di_xuong = True
    i,j = 0,0
    for x in range(len(str_)):
        ban_ro += str(mtran[i][j])
        if i == 0:
            di_xuong = True
        if i == len(mtran)-1:
            di_xuong = False

        if di_xuong == True:
            i += 1
        if di_xuong == False:
            i -= 1
        j += 1
    return ban_ro

if __name__ == "__main__":
    while True:

        global mtran    # De tao ma tran zic zac

        luaChon = -1
        while luaChon<0 or luaChon>2:
            luaChon = showMenu()
        if luaChon == 0:
            print('Bye...')
            break
        elif luaChon ==1:
            # Ma hoa

            ban_ro = input('Nhap ban ro: ').upper().strip()
            khoa = -1
            # Nhap khoa k
            while khoa <= 0:
                khoa = nhapSoNguyen('Nhap khoa k (k la so nguyen duong): k = ')
            ban_ma = ma_hoa(ban_ro, khoa)
            print('Hien ma tran ne:')
            inmtran()
            print("Ban ma:",ban_ma)
            if input("Nhap bat ki de tiep tuc, nhap 'x' de thoat. Lua chon cua ban: ").strip().upper() == 'X':
                print('Bye...')
                break
        else:
            # Giai ma

            ban_ma = input('Nhap ban ma: ').upper().strip()
            # Nhap khoa k
            while khoa <= 0:
                khoa = nhapSoNguyen('Nhap khoa k (k la so nguyen duong): k = ')
            ban_ro = giai_ma(ban_ma, khoa) 
            print('Ban ro:,',ban_ro) 
            if input("Nhap bat ki de tiep tuc, nhap 'x' de thoat. Lua chon cua ban: ").strip().upper() == 'X':
                print('Bye...')
                break


