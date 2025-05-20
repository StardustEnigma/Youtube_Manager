import json

def Load_data():
     try:
          with open('youtube.txt','r') as file:
               return json.load(file)
     except FileNotFoundError:
          return []
     
def save_data_Helper(videos):
     with open('youtube.txr','w') as file:
          json.dump(videos,file)

def List_all_videos(videos):
        pass

def Add_video(videos):
       pass


def Update_video(videos):
       pass

def Delete_video(videos):
    pass

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