import requests


class JSONPlaceHolder:

    def __init__(self):

        self.url = "https://jsonplaceholder.typicode.com/"

    def tum_kullacilari_listele(self):

        response = requests.get(self.url + "users")
        veri =  response.json()
        return veri

    def postlarini_goster(self, user_id):

        response = requests.get(f"{self.url}posts?userId={user_id}")
        veri = response.json()
        return veri



    def yorum_sayisi_getir(self, post_idd):

        response = requests.get(f"{self.url}posts/{post_idd}/comments")
        veri = response.json()

        return len(veri)




api = JSONPlaceHolder()
users = api.tum_kullacilari_listele()

en_aktif_kullanici = None
en_yuksek_ortalama = 0

for user in users:
    postlar = api.postlarini_goster(user["id"])
    toplam_yorum = 0

    for post in postlar:
        yorum_sayisi = api.yorum_sayisi_getir(post["id"])
        toplam_yorum += yorum_sayisi

    toplam_post = len(postlar)
    ortalama = toplam_yorum / toplam_post if toplam_post else 0

    print(f"👤 {user['name']}: {toplam_post} post, {toplam_yorum} yorum, ortalama {ortalama:.2f} yorum/post")




