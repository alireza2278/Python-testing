#سانسور کردن با کاربرد کروتونی در تابع
# def sansor(words):
#     print("hi my frind :)")
#     a = None
#     while True:
#         word = yield a
#         if word in words:
#             a = ("*"* len(word))
#         else:
#             a = word
#
# l = ["mother fucker","kiri","koni","fuck you"]
# g = sansor(l)
# next(g)
# print(g.send("mother fucker"))
# print(g.send("karim"))
#-----------------------------------------------------------
# اجرای .split با کاربرد کروتونی در تابع
# def Split_gen(joda_konande = " "):
#     print("srart!!")
#     s = None
#     while True:
#         line = yield s
#         s = line.split(joda_konande)
#
# g = Split_gen()
# next(g)
# print(g.send("ali reza abdol maleki"))



