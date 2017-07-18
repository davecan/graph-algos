# shortcut for typing all those damn quotation marks
# each letter is now a Node('...') for that letter
for x in [chr(i) for i in range(ord('A'),ord('N'))]:
    exec("%s = Node('%s')" % (x, x.lower()))

Adj = { A: { B:1, C:5, D:4, M:8 },
        B: { A:1, C:6, G:7, M:9 },
        C: { A:5, B:6, M:7 },
        D: { A:4, M:9, F:3, E:2 },
        E: { D:2, F:3, M:4, J:9 },
        F: { D:3, M:3, E:2 },
        G: { B:7, M:5, I:8, H:1 },
        H: { G:1, I:8, M:2, K:8 },
        I: { G:8, H:8, M:9 },
        J: { E:9, M:1, L:7, K:7 },
        K: { J:7, L:3, M:6, H:8 },
        L: { J:7, M:9, K:3 },
        M: { A:8, B:9, C:7, G:5, I:9, H:2, K:6, L:9, J:1, E:4, F:3, D:9 } }