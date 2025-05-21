import json

def Load_data():
     try:
          with open('youtube.txt','r') as file:
               return json.load(file)
     except FileNotFoundError:
          return []
     
def save_data_Helper(videos):
     with open('youtube.txt','w') as file:
          json.dump(videos,file)

def List_all_videos(videos):
    if not videos:
        print("No videos found.")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - {video['time']}")


def Add_video(videos):
       name = input("Enter video name: ")
       time = input("Enter video time: ")
       videos.append({'name':name,'time':time})
       save_data_Helper(videos)

def Update_video(videos):
       List_all_videos(videos)
       index=int(input("Enter the video number to update : "))
       if 1<=index<=len(videos):
            name=input("Enter the new video name : ")
            time=input("Enter the new video duration : ")
            videos[index-1]={'name':name,'time':time}
            save_data_Helper(videos)
       else:
            print("Enter valid address")     

def Delete_video(videos):
    List_all_videos(videos)
    index=int(input("Enter the video number you want to delete : "))
    if 1<=index<=len(videos):
         del videos[index-1]
         save_data_Helper(videos)
    else:
         print("Invalid index")

def main():
    videos=Load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1.List all youtube videos")
        print("2.Add a youtube video")
        print("3.Update youtube video details")
        print("4.Delete the video")
        print("5.Exit")

        choice=input("Enter a number")
        print(videos)
        match choice:
            case '1':
                List_all_videos(videos)

            case '2':
                Add_video(videos)

            case '3':
                Update_video(videos)

            case '4':
                Delete_video(videos)

            case '5':
                break
            
            case _:
                print("Enter valid input")
        
if __name__== "__main__":
     main()