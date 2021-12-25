import json
#### Generate Metadata for each Image    

# f = open('./metadata/all-traits.json',) 
# data = json.load(f)

# Changes this IMAGES_BASE_URL to yours 
IMAGES_BASE_URL = "https://gateway.pinata.cloud/ipfs/QmYVXnDEQqMPxGbhy8frEUuPSkPs6E8EuS84nbf9eQY7sM/"
PROJECT_NAME = "WeHapeTogether"

# def getAttribute(key, value):
#     return {
#         "trait_type": key,
#         "value": value
#    }
for i in range(1,1001):
    token_id = i
    token = {
        "image": IMAGES_BASE_URL + 'wehapetogether_' + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "description": 'This is a fan made memorial NFT for those who be proud of contributing to HAPE community!'
    }
    # token["attributes"].append(getAttribute("Face", i["Face"]))
    # token["attributes"].append(getAttribute("Ears", i["Ears"]))
    # token["attributes"].append(getAttribute("Eyes", i["Eyes"]))
    # token["attributes"].append(getAttribute("Hair", i["Hair"]))
    # token["attributes"].append(getAttribute("Mouth", i["Mouth"]))
    # token["attributes"].append(getAttribute("Nose", i["Nose"]))

    with open('./HapeM_json/' + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)
# f.close()