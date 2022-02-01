import csv

header = ['filename', 'category', 'description', 'permalink']

def get_bayc_data(i):
    return [
        f'bayc_{str(i)}.jpg',
        'BAYC',
        'BAYC is a collection of 10,000 Bored Ape NFTs. Owning a Bored Ape doubles as your membership to the Club.',
        f'https://opensea.io/assets/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/{str(i)}'
    ]

def get_kgf_data(i):
    return [
        f'killergf_{str(i)}.png',
        'Killer GF',
        'Killer GF is a 7,777 generative portrait art collection by a former Riot Games Artist, Zeronis, with over 240 meticulously designed features that contrasts cute and aesthetically appealing girlfriends that also happen to be dangerous assassins.',
        f'https://opensea.io/assets/0x6be69b2a9b153737887cfcdca7781ed1511c7e36/{str(i)}'
    ]

with open('metadata.csv', 'w') as f:
    w = csv.writer(f)

    w.writerow(header)

    for i in range(0, 10000):
        print(i)
        w.writerow(get_bayc_data(i))

    for i in range(1, 7778):
        print(i)
        w.writerow(get_kgf_data(i))
