#I really don't know how to do it. I tried really hard, but this was due
# before office hours so I couldn't figure it out 
#Download the script 
curl -L https://www.dropbox.com/s/u70dtrdr35p5tgk/seminars.tar.gz | tar zxv
#list them in order 
for li in rating_li:
    div = li.find("div", class_="dates")
    dates_numbers = div.a
    meta = li.find("meta", class_="names")
    names_letters = h2.names
    print names_letters 
    print dates_numbers 
#parse HTML files for names and dates 
