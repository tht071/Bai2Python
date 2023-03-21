import pandas as pd

docFile = pd.read_excel('input.xlsx')

def sapXep(file):
    f = file
    f = f.iloc[10:62, 1:8]
    f = f.rename(columns = {f.columns[0]: 'id', f.columns[1]: 'ho', f.columns[2]: 'ten', f.columns[3]: 'ngay sinh', f.columns[4]: 'toan', f.columns[5]: 'ly', f.columns[6]: 'hoa'})
    f = f.sort_values(by = ['ten']) 
    print(f)
sapXep(docFile)

def thongKe(file):
    f = file
    f = f.iloc[10:62, 1:8]
    f = f.rename(columns={f.columns[0]: 'id', f.columns[1]: 'ho', f.columns[2]: 'ten', f.columns[3]: 'ngay sinh', f.columns[4]: 'toan', f.columns[5]: 'ly', f.columns[6]: 'hoa'})
    f['diem trung binh'] = (f['toan'] + f['ly'] + f['hoa']) / 3
    f['xep loai'] = f['diem trung binh'].apply(lambda x: "gioi" if x >= 8 else "kha" if x >= 6.5 else "trung binh")
 
    gioi = 0
    kha = 0
    trungBinh = 0

    for index in f.index:
        if f['diem trung binh'][index] >= 8:
            gioi += 1
        elif f['diem trung binh'][index] >= 6.5:
            kha += 1
        else:
            trungBinh += 1
    newF = pd.DataFrame({
        'Gioi': [gioi],
        'Kha': [kha],
        'Trung binh': [trungBinh]
    })
    print(f"Số học sinh giỏi: {gioi}")
    print(f"Số học sinh khá: {kha}")
    print(f"Số học sinh trung bình: {trungBinh}")

thongKe(docFile)