reference_string = []
page_faults = 0
page_hits = 0

pages = int(input("Enter Total Number of Pages : "))
print("\nEnter the Values of the Reference String : ")
for m in range(pages):
    reference_string.append(int(input(f"Value No. [{m + 1}] : ")))

frames = int(input("Enter Total Number of Frames : "))
temp = [-1] * frames

for m in range(pages):
    s = 0
    for n in range(frames):
        if reference_string[m] == temp[n]:
            s += 1
            page_faults -= 1
    page_faults += 1
    if page_faults <= frames and s == 0:
        temp[m] = reference_string[m]
    elif s == 0:
        temp[(page_faults - 1) % frames] = reference_string[m]
    print()
    for n in range(frames):
        print(temp[n], end="\t")
    page_hits = pages - page_faults

print(f"\nTotal Page Hits : {page_hits}")
print(f"\nTotal Page Miss : {page_faults}")
print(f"\nPage Hit Ratio : {(page_hits / pages):.2f}")
print(f"\nPage Miss Ratio : {(page_faults / pages):.2f}")

