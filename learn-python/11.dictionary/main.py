
profile = {
    "id": 1,
    "created_at": "2023-01-01",
    "name": "Iqbal",
    "score": 80,
    "is_pass": True,
    "subjects": ["Math", "English"],
    "deleted_at": None
}

print("Dictionary elements:")
print(profile)
print("name", profile["name"])

# Pretty print
# import pprint
# pprint.pprint(profile)

# import pprint
# pprint.pprint(profile)

# JSON string
# import json
# print(json.dumps(profile))

profile = dict([
    ("id", 2),
    ("created_at", "2023-01-01"),
    ("name", "Iqbal"),
    ("score", 90),
    ("is_pass", True),
    ("subjects", ["Math", "English"]),
    ("deleted_at", None),
])

print("Dictionary elements with dict constructor:")
print(profile)

print("Dictionary elements (using values method):")
for key in profile.values():
    print(key)

print("Dictionary elements (using keys method):")
for key in profile: # use profile.keys() is same but not recommended
    print(key, profile[key]) 

print("Dictionary elements (using items method):")
for key, value in profile.items():
    print(key, value)


profile = {
    "id": 1,
    "created_at": "2023-01-01",
    "name": "Iqbal",
    "score": 80,
    "is_pass": True,
    "subjects": ["Math", "English"],
    "deleted_at": None,
    "friends": [
        {
            "id": 2,
            "name": "Ali",
            "score": 90,
        },
        {
            "id": 3,
            "name": "ZKh",
            "score": 80,
        },
    ],
    "address": {
        "city": "Jakarta",
        "province": "DKI",
    },
}

print("Dictionary with nested elements:")
print(profile)

print("change name")
profile["name"] = "Muhammad"
print(profile)

print("add notes")
profile["notes"] = "Good student"
print(profile)

print("update address with update method")
profile.update({"address": {"city": "Bandung", "province": "Jawa Barat"}})
print(profile)

print("remove notes with pop method")
profile.pop("notes")
print(profile)

print("add notes again")
profile["notes"] = "Good student"
print(profile)

print("remove notes with del statement")
del profile["notes"]
print(profile)

print("Dictionary keys:")
print(list(profile.keys()))

print("Dictionary values:")
print(list(profile.values()))

print("Dictionary items:")
print(list(profile.items()))

print("Dictionary length:")
print(len(profile))

print("Dictionary copy with copy method:")
copy_profile = profile.copy()
print(copy_profile)

print("Dictionary clear with clear method:")
profile.clear()
print(profile)