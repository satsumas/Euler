def splitter_upper(s):
    bits = []
    if " " not  in s:
        bits.append(s)
    else:
        bits = []
        n = s.find(" ")
        bit = s[0: n]
        bits.append(bit)
        s = s[n+1:len(s)]
        bits.extend(splitter_upper(s))
    return bits

s = " "
print splitter_upper(s)



def test_splitter_upper():
    print splitter_upper("hello")
    assert splitter_upper("hello") == ["hello"]

def test_splitter_upper_multiple():
    print splitter_upper("hello kate")
    assert splitter_upper("hello kate") == ["hello", "kate"]

test_splitter_upper()
test_splitter_upper_multiple()



