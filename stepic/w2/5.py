s = input()

seq = [int(i) for i in s.split()]
seq_len = len(seq)
if seq_len == 1:
    print(seq[0])
else:
    for i in range(seq_len):
        if i == 0:
            prev = seq[-1]
        else:
            prev = seq[i - 1]
        if i == seq_len - 1:
            nxt = seq[0]
        else:
            nxt = seq[i + 1]
        sm = prev + nxt
        print(sm, end=' ')
