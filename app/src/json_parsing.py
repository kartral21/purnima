import json

class JsonParse():
    def json_parser(self):
        try:
             with open('sample.json', ) as f:
                # returns JSON object as
                # a dictionary
                data = json.load(f)
                print("data",data)

                # Iterating through the json
                # list
                for key in data.keys():
                    #print("key",data[key])
                    if isinstance(data[key], list) and data[key]:
                        for lkey in data[key]:
                            #print("1",lkey)
                            if isinstance(lkey, dict) and lkey:
                                for lkey1 in lkey.keys():
                                    print("hu",lkey[lkey1])

                for values in data.values():
                         print("val",values)
        except Exception as e:
            raise e



if __name__ == "__main__":
    s= JsonParse()
    s.json_parser()



