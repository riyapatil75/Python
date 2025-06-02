import sqlite3

conn = sqlite3.connect ('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name YEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name ,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name,time))
    conn.commit()

def update_video(new_index,new_name,new_time):
    cursor.execute("UPDATE videos SET (name,time)(?,?) WHERE index=?",(new_name,new_time,new_index))
    conn.commit()

def delete_video(index):
    cursor.execute("DELETE videos WHERE index=?", (index))
    conn.commit()

def main():
    while True:
        print("\n youtube Manager in DB")
        print("\n 1. Show list")
        print("\n 2. Add list")
        print("\n 3. Update list")
        print("\n 4. Delete list")
        print("\n 5.exit app")
        choice =input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2' :
                name =input("Enter the name of the video: ")
                time =input("Enter the time taken: ")
                add_videos(name,time)
            case '3' :
                new_index=int(input("Enter the index number to update: "))
                new_name =input("Enter the name of the video: ")
                new_time =input("Enter the time taken: ")
                update_video(index,name,time)
            case '4' :
                index=int(input("Enter the index number to delete: "))
                delete_video(index)
            case '5' :
                break
            case _:
                print("Invalid input")

    conn.close()


if __name__=="__main__":
    main()



