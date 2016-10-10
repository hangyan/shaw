from shaw import collection

d = {
        "1": "1",
        "2": "2",
        }

collection.pop_keys(['1'], d)

print d
