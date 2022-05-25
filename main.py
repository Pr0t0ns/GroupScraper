# Made by RobloxDeveloperHub

import httpx
import threading
import time
threads = 2 # More threads = Faster
group_id = 0
groups = []
cookie = "RBXcb=RBXViralAcquisition=true&RBXSource=true&GoogleAnalytics=true; rbx-ip2=; RBXEventTrackerV2=CreateDate=5/24/2022 8:53:04 PM&rbxid=&browserid=134568068502; GuestData=UserID=-1759249199; _gcl_au=1.1.1586504561.1653443586; RBXSource=rbx_acquisition_time=5/24/2022 8:53:28 PM&rbx_acquisition_referrer=&rbx_medium=Direct&rbx_source=&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=1; __utma=200924205.214891096.1653443609.1653443609.1653443609.1; __utmb=200924205.0.10.1653443609; __utmc=200924205; __utmz=200924205.1653443609.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"





def main():
  global group_id
  set_id = group_id
  group_id += 1
  if set_id in groups:
    try:
      return main()
    except RecursionError:
      print("Python Recursion Error small sleep!")
      time.sleep(1)
      return main()
  groups.append(set_id)
  url = f"https://www.roblox.com/groups/{set_id}/redirect"

  headers = {
    "cookie": cookie
  }
  req_group = httpx.get(url, headers=headers)
  if req_group.status_code == 404:
    print("Seems like we hit a 404")
    try:
      return main()
    except RecursionError:
      print("Python Recursion Error small sleep!")
      time.sleep(1)
      return main()
  try:
    req_headers = req_group.headers['location']
  except KeyError:
    print("Unexpected KeyError Hit, Rerunning thread!")
    try:
      return main()
    except RecursionError:
      print("Python Recursion Error small sleep!")
      time.sleep(1)
      return main()
  if req_headers == "https://www.roblox.com/search/groups?keyword=":
    print(f"Group with id {set_id} cannot be found!")
    try:
      return main()
    except RecursionError:
      print("Python Recursion Error small sleep!")
      time.sleep(1)
      return main()
  else:
    full_url = "https://www.roblox.com{}".format(req_headers)
    file = open('groups.txt', "r+")
    data = file.read()
    file.close()
    if full_url in data:
      print("Duplicate group found not adding to txt file!")
      try:
        return main()
      except RecursionError:
        print("Python Recursion Error small sleep!")
        time.sleep(1)
        return main()
    print(f"Found group with id {set_id}")
    file = open("groups.txt", "a+")
    file.write(full_url + "\n")
    file.close()
    try:
      return main()
    except RecursionError:
      print("Python Recursion Error small sleep!")
      time.sleep(1)
      return main()
  
  



if __name__ == "__main__":
  for i in range(threads):
    threading.Thread(target=main).start()
  
