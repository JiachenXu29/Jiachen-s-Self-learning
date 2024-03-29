import re


def extract_name(url):

    url = input("URL: ").strip()
    print(f"The URL is: {url}")

    # url =  "www.linkedin.com/in/jiachen-xu-997166270"

    # usernameandnumber = re.sub(r"^(https?://)?(www\.)?linkedin\.com/in/", "", url)
    # print(f"Username:{usernameandnumber}")

    # www.linkedin.com/in/jiachen-xu-997166270
    matches= re.search(r"^(?:https?://)?(?:www\.)?linkedin\.com/in/([a-z]+)(?:[-]+)([a-z]+)" , url, re.IGNORECASE)
    if matches:
        print(f"The Username is:", matches.group(1)[0].upper()+matches.group(1)[1:] + " " + matches.group(2)[0].upper()+matches.group(2)[1:] )



