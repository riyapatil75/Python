import requests

def free_api_username():
    url ="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return( username, country)
    else:
        raise Exception("There is no data input")


def main():
    print("Fetching data....")
    try:
        username, country=free_api_username()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    main()

