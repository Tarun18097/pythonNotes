import requests

def download_file(url, file_name):
    # get the extension from url
    url_ext = url.split('.')[-1].lower()

    file_name = f"{file_name}.{url_ext}"

    try: 
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name,'wb') as file:
                file.write(response.content)
            print(f"File {file_name} downloaded successfully")
        else:
            print(f"Failed to download file {file_name}")
            print(f"Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = 'https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-1024.png'
    
    download_file(url, "python_logo")



