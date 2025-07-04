# working with files, repository, folder()repository and folder are same / terminal bash and CMD /
# ფაილებთან მუშაობა, გახსნა ჩართვა და ა. შ.
# txt_file = open("persons.txt", "r+")
# # open ბრძანებით ხდება ფაილის გამოძახება, რომელსაც გადაეცემა ორი ბრძანება
# # 1: ფაილის სახელი
# # 2: ფაილის ფორმატი
# # print(txt_file.write("lashikoooo"))
# print(txt_file.read())
# # ფაილი აუცილებლად ნდა დაიხუროს .close მეთოდოთ
# txt_file.close()

# გვაქვს 4 ფორმატი ფაილებთან სამუშაოდ
# 1: "r" ფორმატი - რომელსაც შეუძლია ფაილის წაკითხვა
# 2: "w" ფორმატი რომელიც ფაილში შეგვიძლია ჩავწეროთ ტექსტი
# 3: "a" ფორმატი, append, რომლითაც შეგვიძლია ფაილში ჩავამატოთ ტექსტი
# 4: "x" ფორმატი რომლითაც შეგვიძლია შევქმნათ ფაილი

# "r" ფორმატის მეთოდები :
# readable() გვიჩვენებს არის თუ არა წაკითვადი
"გახსნისას უნდა მივუთითით ის ფორმატი რომლითაც გვინდა რომ ვემუშავოთ ტექსტს, თყ მივუთუთებთ "r" ფორმატს მას, wის ფორმატის მეთოდებით ვერ ვემუშავებით"r""
# txt_file = open("persons.txt", "r+")
# print(txt_file.readable())
# 1: readable() გვიბრუნებს შეიძლება თუ არა ფაილის წაკითხვა
# txt_file.close()


"2 : ორმატ "r" გააჩნია read() მეთოდი, რომელსაც შეუძლია ფაილის წაკითხვა"
txt_file = open("persons.txt", "r+")
# print(txt_file.read())
# ფრჩხელბში შეგვიძლია გადავცეთ ბაიტების რაოდენობა და იმდენ სიმბოლოს გამიტანს რამდენ ბაიტსაც გადავცემთ
# print(txt_file.read(26))
# txt_file.close()
# new_text_file = open("text.txt", "r")
# print(new_text_file.read(11))
# # read() მეთდი, წაკითხულ ტექსტს ხელახლა არ გამოიტანს თუ მას არ დავარესტარტებთ
# # მაგ: read() ით წავიკითხეთ პირველი 2 აბზაცი, თავიდან რომ გადავცეთ ბრძანება
# # წაკითხვას გააგრძელებს, იმ ხაზიდან რომელზეც გაჩერებული იყო
# print(new_text_file.read())
# # თუ გვინდა რომ 0დან დაიწყოს წაკითხვა seek() მეთოდით, უნდა დავაბრუნოთ საწყის, ნულ ეტაპზე
# new_text_file.seek(0)
# # seek() მეთოდს გადაეცემა ბაიტები, თუ რომელ ეტაპზე უნდა დადგეს, რომელი სიმბოლოდან უნდა დაიწყოს წაკითვა
# # თ გადავცემთ 0ს საწყის ეტაპზე დაბრუნდება
#
# new_data = new_text_file.read()
# print(new_data)
# new_text_file.close()


file = open("text.txt", "r+")
"readline და readlines მეთოდები და განსხვაავება"
print(file.readline())
# ისევე კითხულობს როგორც read() მეთოდი
print(file.readline())
file.close()
# !!!!!!!!!!!!!!!!!!!!!!!!!
# ხოლო readlines() კითულობს მთლიან ფაილს, და წამოიღეს, ლისტის სახით
file = open("text.txt", "r+")
print(file.readlines())
# წამოიღო ლისტის სახით თავის \n new line  სიმბოლოთი
file.close()



"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
# "w" ფორმატი
# ფორმატი საშუალოებს გვაძლევს რომ ფაილებში ჩავწეროთ ტექსტი
file = open("text.txt", "w")
file.writelines("hello world smn")
# w ფორმატს შეუძლია ჩაწეროს ტექსტი ფაილსი, მაგრამ, ფაილში არსებულ ტექსტს ამოშლის და ჩაწერს იმას რასაც გადავცემთ
file.writelines("\nhello world smn meored")
# გააჩნია wrtiable მეთოდი, რომელიც გვიჩვენებს შეგვიძლია თუ არა ფაილის ჩაწერა და გამოიტანს ბულიეან მნიშვნელობას true/false
print(file.writable())
file.write("makho")
names = ["\nmakho", "\nnika", "\nlasha", "\ntoro"]
file.writelines(names)
# file.write(names)
# განსხვავება write() და writelines() ისსა რომ, write() უნდა გადავცეთ მხოლოდ სტრინგი და არა სხვა იტერეირებადი ობიექტი
# ხოლო, writelines()ს შეგვიძლია გადავცეთ სხვა იტერირებადი ობიექტიც


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# w ფორმტი, ამატებს ფაილში მონაცემებს, მაგრამ იქ არსებულ მონაცემებს ამოშლის,
# თუ გვინდა რომ არ ამოშალოს და უბრალოდ ჩაამატოს მონაცემები, უნდა გამოვიყენოთ a ფორმატი უნდა გამოვიყენოთ append()
file = open("text.txt", "a")
print(file.write("\nhellosm"))
# a ფორმატსაც გადაეცემა write() და writelines() მეთოდები
print(file.writelines("hello"))
file.close()




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# x ფორმატი
# new_file = open("newtext.txt", "x")
# new_file.write("hello\nworld\nmakho\nnika\lasha\ntoro")
# new_file.seek(0)
#
# file_lines = new_file.readlines()
# print(file_lines)
# new_file.close()



# + ფორმატი
# + ნიშანი უნდა დაისვას ყოველი ფორმატის შემდეგ, და გო გახდება მულტი ფორმატული,
# w+ არამარტო ჩაწერადი გახდება და არამედ წაკითვადიც / და პიქირიტაც


# context manager
# ფაილს როცა გავხსნით აღარაა საჭირო მისი დახურვა
# comprehensionის მსგავსი მოკლე გზააა ფაილებთან სამუშაოდ
# სინტაქსია:
with open("text.txt", "r+") as file:
    file.write("context manager syntax")
# მსგავს შემთხვევაში, ფაილის ბლოკში უნდა ჩავწროთ ბრძანებები
# ბლოკს გარეთ თუ გავალთ იგი ბლოკს აღარ ეკუთვნის



# იწყება with საკვანძო სიტყვით, შემდგომ ვხსნით ფაილს ჩვეულებრივ
# ვუწერთ ფაილის დასახელებას და ფორმატს
# ბოლო კი ვწერთ იმ ცვლადის სახელს სახაც უნდა შეინახოს ფაილი
# იგივენაირად მუშაობს როგორც
file = open("text.txt", "r")
file.close()











#
# def write_names_to_file():
#     with open('names.txt', 'w+') as file:
#         counter = 1
#         while True:
#             first_name = input("Enter your first name: ")
#             if first_name.lower() == 'stop':
#                 break
#
#             last_name = input("Enter your last name: ")
#             file.write(f"{counter}. {first_name} {last_name}\n")
#             counter += 1
# print(write_names_to_file())

