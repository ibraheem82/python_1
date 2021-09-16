# answer(q1)
a = "django"
print(a[0])
print(a[5])
print(a[0:5])

# answer(q2)

b = [3, 7, [1, 4, "hello"]]
b[2][2] = "goodbye"
print(b)

# Question3
d1 = {"simple_key": "hello"}
d2 = {"k1":{"k2" : "hello"}}
d3 = {"k1":[{"nest_key":["this is deep",["hello"]]}]}

print(d1["simple_key"])
print(d2["k1"]["k2"])
print(d3["k1"][0]["nest_key"][1][0])

#Question 4:

sample = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "History":80,
            }

        }
    }
}

print(sample["class"]["student"]["marks"]["History"])

# Question5
students = {
    "first":{
        "name":"Yaqub",
        "scores":{
            "Maths":80, "Eng":70,
        }
    },

     "second":{
        "name":"Olanrewaju",
        "scores":{
            "Maths":95, "Eng":60,
        }
    },

     "third":{
        "name":"Deji",
        "scores":{
            "Maths":95, "Eng":90,
        }
    },

     "forth":{
        "name":"Toheeb",
        "scores":{
            "Maths":50, "Eng":70,
        }
    },

     "fifth":{
        "name":"Pelumi",
        "scores":{
            "Maths":50, "Eng":77,
        }
    },

     "sixth":{
        "name":"Sofiat",
        "scores":{
            "Maths":80, "Eng":60,
        }
    },

     "seventh":{
        "name":"Azeezat",
        "scores":{
            "Maths":40, "Eng":85,
        }
    },

     "eighth":{
        "name":"Rasheed",
        "scores":{
            "Maths":50, "Eng":40,
        }
    },

     "nineth":{
        "name":"Kazeem",
        "scores":{
            "Maths":75, "Eng":70,
        }
    },

     "tenth":{
        "name":"Jemilat",
        "scores":{
            "Maths":60, "Eng":70,
        }
    }

}

for i in students:
    ave = (students[i]["scores"]["Maths"] + students[i]["scores"]["Eng"]) / 2
    del(students[i]["scores"])
    students[i].update({"name":students[i]["name"],"average":ave})
print(students)

