import json


def list_all_videos():
    for index, video in enumerate(videos, start=1):
        print(f"{index}, {video} ")

def add_video():
    name = input("enter video name")
    time = input("enter video time")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

    
def update_video():
    list_all_videos(videos)
    index = int(input("enter video number to update"))
    if 1 <= index <= len(videos):
        name = input("Enter new video name : ")
        time = input("Enter new video time : ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid Index selected   ")



def search_videos():
    name = input("enter name of video to search ")
    for video in videos:
        if video['name'] == name:
            print(video)
            return

    for index, video in enumerate(videos, start=1):
        print(f"{index}, {video} ")
              
def delete_video():
    list_all_videos(videos)
    index = int(input("enter video number to delete"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid Index selected   ")



def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def main():
    global videos
    videos = load_data()

    while True:
        print("select opotions")
        print("1. List all videos")
        print("2. add new video")
        print("3. Update new video")
        print("4. delete a video")
        print("5. search for videos")
        print("6. Exit")
        choise = input("select opotions  :  ")
        # print(videos)

        match choise:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                search_videos()
            case '6':
                break
            case _:
                print("Invalid choice")

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []




if __name__ == "__main__":
    main()




