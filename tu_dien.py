tu_dien={"love":"yêu","seen":"xem","mother":"mẹ","father":"ba"}
tu_dien2={"speak":"nói"}
tu_dien.update(tu_dien2)
print(tu_dien)
tu_can_dich=input("nhập từ cần dịch: ")
for key,value in (tu_dien.items()):
    if key==tu_can_dich:
        print(key,':',value)