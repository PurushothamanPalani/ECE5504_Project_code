import os
import csv

path = "/home/purushothsankari/rocket/chipyard-PurushothamanPalani/sims/verilator/output/chipyard.TestHarness.ECE5504RocketPrefetchConfig"

fnames = ['file_names']
cycles = ['cycles']
instret = ['instret']
loads = ['loads']
stores = ['stores']
I_miss = ['I$_miss']
D_regular_miss = ['D$_reg_miss']
D_prefetch_miss = ['D$_prefetch_miss']
D_release = ['D$_release']
ITLB_miss = ['ITLB_miss']
DTLB_miss = ['DTLB_miss']
L2_TLB_miss = ['L2_TLB_miss']
branches = ['branches']
mispredicts = ['mispredicts']
load_use_interlock = ['load_use_interlock']
I_blocked = ['I$_blocked']
D_blocked = ['D$_blocked']
averages = ['averages']
files = os.listdir(path)
files.sort()
for i in files:
    if "log" in i:
        fname = os.path.join(path, i)
        print(i)
        with open(fname) as f:
            x = f.readlines()
        f.close()
        fnames.append(i)
        cycles.append(int(x[1][x[1].rfind(':') + 1:]))
        instret.append(int(x[2][x[2].rfind(':') + 1:]))
        loads.append(int(x[3][x[3].rfind(':') + 1:]))
        stores.append(int(x[4][x[4].rfind(':') + 1:]))
        I_miss.append(int(x[5][x[5].rfind(':') + 1:]))
        D_regular_miss.append(int(x[6][x[6].rfind(':') + 1:]))
        D_prefetch_miss.append(int(x[7][x[7].rfind(':') + 1:]))
        D_release.append(int(x[8][x[8].rfind(':') + 1:]))
        ITLB_miss.append(int(x[9][x[9].rfind(':') + 1:]))
        DTLB_miss.append(int(x[10][x[10].rfind(':') + 1:]))
        L2_TLB_miss.append(int(x[11][x[11].rfind(':') + 1:]))
        branches.append(int(x[12][x[12].rfind(':') + 1:]))
        mispredicts.append(int(x[13][x[13].rfind(':') + 1:]))
        load_use_interlock.append(int(x[14][x[14].rfind(':') + 1:]))
        I_blocked.append(int(x[15][x[15].rfind(':') + 1:]))
        D_blocked.append(int(x[16][x[16].rfind(':') + 1:]))

with open('prefetch_5-30.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fnames)
    writer.writerow(cycles)
    writer.writerow(instret)
    writer.writerow(loads)
    writer.writerow(stores)
    writer.writerow(I_miss)
    writer.writerow(D_regular_miss)
    writer.writerow(D_prefetch_miss)
    writer.writerow(D_release)
    writer.writerow(ITLB_miss)
    writer.writerow(DTLB_miss)
    writer.writerow(L2_TLB_miss)
    writer.writerow(branches)
    writer.writerow(mispredicts)
    writer.writerow(load_use_interlock)
    writer.writerow(I_blocked)
    writer.writerow(D_blocked)
    
f.close()