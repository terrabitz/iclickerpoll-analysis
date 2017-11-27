def binary_string_to_hex(bin_string, bit_shift=0):
    for _ in range(bit_shift):
        bin_string = bin_string + '0'
    hstr = '%0*X' % ((len(bin_string) + 3) // 4, int(bin_string, 2))
    return hstr

def samples_to_binary_string(samples, invert=False):
    vector = ''
    for sample in samples:
        if sample > 0:
            if invert:
                vector += '0'
            else:
                vector += '1'
        else:
            if invert:
                vector += '1'
            else:
                vector += '0'

    return vector

def samples_to_hex(samples, invert=False, bit_shift=0):
    data = samples_to_binary_string(samples, invert)
    return binary_string_to_hex(data, bit_shift)

def binary_samples_to_binary_string(samples, invert=False):
    if invert:
        new_samples = []
        for i in samples:
            if i:
                new_samples.append(0)
            else:
                new_samples.append(1)
        samples = new_samples

    samples = [str(sample) for sample in samples]
    return ''.join(samples)

def binary_samples_to_hex(samples, invert=False, bit_shift=0):
    data = binary_samples_to_binary_string(samples, invert)
    return binary_string_to_hex(data, bit_shift)
