# -*- coding: utf-8 -*-
import requests

def random_bitmap(x_pixels=128, y_pixels=128):
    from PIL import Image
    sequence_size = x_pixels * y_pixels
    results = get_random_integers(0, 255, y_pixels, x_pixels, sequence_size)
    bitmap = Image.fromarray(results, "RGB")
    bitmap.save("random_bitmap.bmp")


def get_random_integers(the_min, the_max, cols, rows, size):
    results = []
    payload = {
            "min": the_min,
            "max": the_max,
            "col": cols,
            "format": "plain",
            "rnd": "new",
            "base": "10",
            }
    url = "https://www.random.org/integers"
    while True:
        request_size = max(1, min(10000, size))
        payload["num"] = request_size
        response = requests.get(url, params=payload)
        # print(response.url)
        results.extend(response.text)
        remainder = size - request_size
        if remainder <= 0: break
        size = remainder

    one_dimensional = [int(i) for i in "".join(results).split()]
    if cols == 1:
        return one_dimensional
    else:
        # because of the chunking, we have to reconstruct the 2D array
        output = []
        y = 0
        for x in range(rows):
            output.append(one_dimensional[y:y+cols])
            y += cols
        return output


def random_RSA_key_pair(bits=1024):
    def random_generator(N):
        return get_random_integers(0, 255, 1, 1, N)

    from Crypto.PublicKey import RSA

    private_key = RSA.generate(bits, random_generator)
    public_key = key.publickey()
    print("private_key:", private_key)
    print("public_key:", public_key)

if __name__ == "__main__":
    random_bitmap()
    random_RSA_key_pair()

