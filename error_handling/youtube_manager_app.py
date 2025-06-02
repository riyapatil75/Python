import json

def load_data():
    try:
        with open("youtube.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def show_list(videos):
    print("*" * 70)
    for index,video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name'] }, Duration: {video['time']}")
    print("*" * 70)


def add_video(videos):
    name= input("Enter the video name: ")
    time= input("Enter the time taken by video: ")
    videos.append({'name':name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    show_list(videos)
    index=int(input("Enter the index number to update"))
    if 1 <= index <= len(videos):
        name=input("Enter the new name: ")
        time=input("Enter the new video time: ")
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def delete_video(videos):
    show_list(videos)
    index=int(input("Enter the video index to delete video"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")



def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager")
        print("1.List the youtube videos")
        print("2.Add the youtube videos")
        print("3.Update the youtube videos")
        print("4.Delete the youtube videos")
        print("5.Exit the app")
        choice = input("Enter your choice: ")
       # print(videos)

        match choice:
            case '1':
                show_list(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
