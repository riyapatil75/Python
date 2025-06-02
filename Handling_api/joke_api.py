import requests

def tell_me_a_joke():
    url="https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke=data["data"]["content"]
        return joke
    else:
        return Exception("Cannot fetch the data")
    
def main():
    try :
        joke=tell_me_a_joke()
        print(joke)
    except Exception as e:
        print(str(e))    

if __name__=="__main__":
    main()



