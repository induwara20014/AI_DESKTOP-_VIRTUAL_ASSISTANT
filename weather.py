#https://www.google.com/search?q=weather+patna&sca_esv=0d1ec8b342403671&rlz=1C1GCEU_enLK1162LK1162&sxsrf=AE3TifMtDOf72IzSY1QwKdkjpZbsowbmhQ%3A1748880361890&ei=6cs9aMmANt2MseMPhsev8Ao&ved=0ahUKEwiJmeaFj9ONAxVdRmwGHYbjC64Q4dUDCBA&uact=5&oq=weather+patna&gs_lp=Egxnd3Mtd2l6LXNlcnAiDXdlYXRoZXIgcGF0bmEyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyDRAAGIAEGLADGEMYigUyDRAAGIAEGLADGEMYigVI_WRQ9BFY3DlwAXgBkAEAmAGxAqAB4QeqAQUyLTMuMbgBA8gBAPgBAZgCBKAC4AXCAgsQABiABBiRAhiKBcICBxAAGIAEGArCAgwQIxiwAhgnGEYYgALCAgcQABiABBgNmAMA4gMFEgExIECIBgGQBgqSBwUxLjAuM6AH8SayBwMyLTO4B8sFwgcFMi0yLjLIByU&sclient=gws-wiz-serp
# user agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36



#  span  id = wob_tm

from requests_html import HTMLSession
import speech_to_text

def weather():
    s = HTMLSession()
    query = "patan"
    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'})
    temp = r.html.find('span#wob_tm' , first= True).text
    unit = r.html.find('div.vk_bk.wod-unit span.wob_t' , first=True).text
    desc = r.html.find('span#wob_dc' , first=True).text
    return temp+" "+unit+" "+desc
