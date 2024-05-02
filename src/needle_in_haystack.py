def find_needle_in_haystack(haystack, needle):
    def compute_lps_array(needle):
        length = 0
        lps_array = [0] * len(needle)
        i = 1

        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps_array[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps_array[length - 1]
                else:
                    lps_array[i] = 0
                    i += 1

        return lps_array

    lps_array = compute_lps_array(needle)

    indexes = ""
    m = len(needle)
    n = len(haystack)
    i = 0
    j = 0

    while i < n:
        if needle[j] == haystack[i]:
            i += 1
            j += 1

        if j == m:
            indexes += str(i - j) + ","
            j = lps_array[j - 1]
        elif i < n and needle[j] != haystack[i]:
            if j != 0:
                j = lps_array[j - 1]
            else:
                i += 1

    if indexes:
        return indexes[:-1]
    else:
        return None
