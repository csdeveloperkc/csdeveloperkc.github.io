import json
import urllib.request
import os

data = [
  {
    "id": "3a1a9eaf5d9840f88b818c83971aba06",
    "name": "What to Expect - Updated Content",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzQ2MjgzNTkxZjM3NjQyNDQ4ZGFiODQyYWZlNjk3ZWU5EgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0ug43Km4jaqQk1AB10_dfDLHDYYs_8Lgqf6hVgGExG7avjvZe9FpBM-tc85wl1ZxQaGslKAGiIwEjJSOkKSGhT0aj5bPywyL06iQfTSvejoKkFRVGs-H1T2enyuslt0clr0xIxWX98EKnENmjXaOFZhxmIpWQBCT439UmM-6MXJZvPV73xDpU9tYec6F3Qs6eyeDL9tk_7qv25M9bV4ndfJ9CrZVPXQSps0nI_HwoTLLQ-JUTEuxgGAoWQ"
  },
  {
    "id": "9258798ac04d4a229472928fb094d82c",
    "name": "Generated Screen",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY0YzYzN2Y3OTA1ZWEwMWViNDIwZmY3MTA5MWQzEgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0ugdzKH3fVqNLhYbqiy1A6y4P57gU4lFbwA3Zle_GH7KHWwqY7n1uHYUaxBv8eS5VYCXoEvM0Jy1y318_1Njdn_5mUfQnpMa-p4fCrPhOTbfA9V7s3-keolbcI9l7qiKTJH1pJAaxul0vGqLhYM_o1VaBhNBEtQIX-cwG16cfu6or-qTMcca3TEalIGOx3kaQJ9zbSDoq_rVRl8CPS1vEmruolJ1mpjuMjC1E-5vDAZgSlajVzXAftZ3aa4"
  },
  {
    "id": "c993942a82194cd285dcc9f630c6c3d9",
    "name": "Grief Share - Updated Layout",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzFiMjc5OWZiZjliZDRhYTRiNDhkYjk3YWZiODk2MWZkEgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0uiwS11j6kYrXvhlqpkscRf9ZbQObBz32MAk1G8gqufO2mNhTMKtdh9Fj2uvG5RQfkfLna_cYtfP0MaXhHsh9xa8TBJRBPZZe7cYcNIaPAXmA_MDQlnXU6DiFFfc56Pjkx_c3zeLGcPeUeUgVRiwbJAp59OLP6z9XYxwut-RYQVx8Lq3kRTVOli76lzZgZ8ti7hoVc6EmKRCGGjVncEXReUcoH61llHW2u6sKsHLN0AHm4u-eRscKTudisE"
  },
  {
    "id": "cb02bae640e340da9c55453df8b89309",
    "name": "Home Page - Updated Footer Address",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzdiMDE3YmE3Y2ZlZjQ5NzBhZmM2NDRlYmNjMWZiM2JmEgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0uidkOfkazw8FhXc6HR5k6f01wH_pdQ6K-63e2SfPg7xfi_yDh1Ehgyx7owRFgAadakZI-15g8iftNtYwrP5tXVeuq-XmvyQ_bKrmoJ-tUefOcRP0VYwaw_IhSQzNTn9AkLPpbKO_m6CW_i_DSuL8Uhx3KC8PUlETny7cEd_FKhKLEdR3i1CWAuOc17lRVpLYO8RqVeYL4jkrBwgBOgBVbIEYA5XwbnIPWnp3lvInlgOJmtjvHeGRm5sEAw"
  },
  {
    "id": "f7baa5b9b86043169377e30c3028d4fc",
    "name": "Staff Page - Updated Call to Action",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sX2E2ZjBkOTI2MmU1MTRiMTNhNjk5NDQwZDlkMWZhN2RlEgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0ujcE2UcBF13ZT2X-qdaO0z4djNwngZeZHg-tKo4TXK6KLZLvaz9eR-w8pOoUR1T6nt2iRy7YrWikWC7HgXKs6NToHKQLARzKUSebubv5tDRSCJVIXhpmE7w9TzxKDyyCT_Wn3m8_k95zazNQClVK4Me16Fql_738VzAydbIJI753y9gmWo3UzB-GY8cM4SOU9gqQcbagznGsPnLhcQNJZHeUeE5nWEb6p1qMyXx19wVwhb2XmcukPEIU4I"
  },
  {
    "id": "fa41e3618a7d48d9b8aa644cc0245a41",
    "name": "Connect Page",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sX2M4Y2EyNWU2YTYxOTQyNjM4YWI4Mzg2NWU2ZjM0MWUxEgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0uiGqD9nCG706kk2HnPkNTQqm8Do4n7tRPwVUETT8lbBHkKSBOdva6Cz-an1CU4vxix36_FPtzcW2sBslZVeHxmsUsLtJqY6oZlUtb9VAHjIL0urA-wJLkbeOYbvI6bb2Ps3uHmHStvgX3Jj3NfQXfmebW_pR079iOy-D1L5F95mFyopzeF5yx-ZWgKDKhtBEhW0RM5QZ7aQV3DjNQPMvROV37n8Lusyvq2U3GyJ-em2Si45nYGtKD5-POk"
  },
  {
    "id": "362c6e8035cf46c68303d39d17ee5397",
    "name": "Compassion Outreach with Video",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzVlMWZhMzNlZWFiZDQxYjliODBhZTI4M2IwOGM0NDYyEgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0ujGKq4EXmEvFJ6oG7zVuOk4cpIFsoidpzSO5h4NS_EGfAyM5EFnPw-Cr3CyPrkMmPmKBfurDL_ozGfgyYXcFCDuwVmynzpYfddCBMIifLIBK8__C4UckSJ8kKV5uitd7O8JmvJn5yG8gbQtFCkJ6w3sQnngOGzp2B0GgT4300xUJmZcS4VdtPu1Uih2SxB5nBKjPjCsp8Ss3VMGOzlES3leeCD1s1zD0xnQM9zbnUJ_VtlW858rxAU1HaQ"
  },
  {
    "id": "0b6126a864714fdf984fd9c0a6ea9017",
    "name": "Compassion Outreach with Video",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzUyZWE4NzYzYjFlNjQ3YzhhOTM5MjdjMTg2YjE1M2U2EgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0uhcCwkz-N2K26sJ3Fx9sey_vZBNpX_go4g5mk_7ivovHSRTlWK9ECPGW7xwkZIkTwMl-QBcgWP76eQi4861HydexFLCY014Ba9ZwxnZAeVNbiBAJcJNf37jIXCvFO69hOmF0zYa7LkPdud5Ely0lsove6uUFwsCwxchesJaYAW1HOqaUiHTh773TXYaQC0PpxTGGdy2QwynwLHZrT3NRiDiGTj3eAwph6-hr8w1bLFTsKrvsFiHJgFz1CY"
  },
  {
    "id": "0ba57511199a4ecdb0c9af837173a23a",
    "name": "Sermon Library - Unified Footer",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzg3Yzg1NzAwNDlkYjQ3MDNhNTY5Njg1ZmU1NjAyNTdmEgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0uhfmTJoxdRuT2GiXiVWxX64qZYTomYjdtsCcuvZwCjYxP1JdPJENXIe0-UC2qD3LnUKJ2HyOUAtapJbeCtAMO_g7Al5w1Re91LIFpmLTaYg4IcOui18RzMJX4uDsrcwodTgO_aogyJYky-35ahXNnSM5THZXREWVZNuf28BOQKLWYSqc_NHUMGm8KiIEK5x8n8qriJzERZcO9yrZ510rtl18PvTpnVzfEhXKLnG0_d30Mrx9B05zNg9QUs"
  },
  {
    "id": "169b63d1f68a464a94b32d7323f54614",
    "name": "Prayer Warriors - Simplified Layout",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzMzZTQzZGYzY2M4NDQ0NzY5MzdhMjIyMjFjMmNlMzZmEgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0ugpTjwg8C-OSDfGgGwzQNTHyZnid_ZtmhV32cLO-WVdsGntjQ4abH2Yb1KCI-2kNT6x3vZTqZfVJafXCk78sO0yY8-u-KqNCMSdGFWNwIh26emgoMU8OOwnkYO0QSKTUYtgEBrs0E3LG0az9U1gAl1B37dvLcmXBnjbR2ZQo0Q0owM3qh-HYAtU6Jp9X58DSzdlIiyjblL7kQsaimYmym8xhvfnJUoGCoUreB3E-kV2Nd0ZY1Xv2gq6aJU"
  },
  {
    "id": "1dc69b2ef0a9452f982d52d188edc5ea",
    "name": "Men's Ministry - Updated Layout",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sX2ViMjhkNmJmNzY3YjRlNDk5OTNmZjY3NTVkODM1M2IzEgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0ugcCCMkcnbUPQpHpU2h5pS7tdYs4Wq6xH9M5s2UuyCUEOTb29zKtXD3-JDNvwJeJLaaC3HrWC3YXNAxiYEvW96u3O8tybAMFb1o4pKqDlH77DaXAwV6SQcD-nJ4x1pIBos8KlygvA53zCn17nHJm4gPGh3aT5DvlE_FA4PGZGV37e-ee2LqWTGBYZDxqo47QZxe67ugFBR1I81a99LD3jGasT2MlPBbciR0V5M7iFJPLg5wE_4xvJY9aOg"
  },
  {
    "id": "2056e68eca0e4d29859c8a3999757ec2",
    "name": "G.L.O.W. Women's Ministry Page",
    "html_url": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzNkODhjMDIxMTBkYzQ1OTQ4MzkwNTBjY2E1OWIyNTUyEgsSBxCu8JOz5gsYAZIBIwoKcHJvamVjdF9pZBIVQhMxNDkwODgzNTk1NjE3Nzg2ODc0&filename=&opi=89354086",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0uiMigijmD_cTMxjZQSaqdQKc2DJNSSAwn0Z8dtlGIHaR1JGCl4Apeo5UhCv7UCHmTBiDGcYQk2VD62S2LnDhkl3baq-uZsns1M-cnUFXgZJMDg94xNIBhvZubQPmaf_h5G7Esf6fHqko8Rr8_gV1gWuARVdeLjc1RnPd9UJaRB9bMQHcOW9XHyjTqdSZhUAQ2buTRb_M4gBQch6USnl1xSxqfHdb3B6DkSy4jIsgK8X-66XSaAdMRQ8XJI"
  },
  {
    "id": "990012635160266755",
    "name": "gfgbcrialto-new-logo-2025-70x70.png",
    "html_url": "",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0uh6m2Tauj5Bcd8TxU_5EkQSCFJ_cETf7Jw0Dn3nlgTNQCQblcOebqdqyx9vAsq5sjAAdQ7BEvfdsYThU4oyHV6t3zx1SrQRRGi89WMPJzYftde4s_HV3ir_fdaYcRIOLil-v5Gojho1_AgdWPTdGWNYVSfHJiz1uJTk-mTYS46Y4cjR7aP68RA47mqr-1gWuKyvthHi01uP-8vPQ_Q6eZTObkJTRLMUdt4cXgQltNBFZHO8Lj9HA1TtEFkuGSPRzmzRTYCUFoS5Sg"
  },
  {
    "id": "16109936438301925898",
    "name": "doctrinal.jpg",
    "html_url": "",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0ugHaBNeSeW0z9ie1wJC53h32Z5F04uUzSDq52JuAYlLpX3m9jR9Q6dLLcukqh8HLLJCVbCMWWgfOj5Nm2RPCseRkDWeC6SnEqvkkz-B7XBZnrjwaaW0_LOLf6Y-Ulovay_BrhQq6Mk3PbdsLSHbHV1NYhBWViimLyZkMfXG58qP8cvSKyZyy4fXCUZCHKLqhjreoSFRiAKu6EMj8vgS_udlbuu35atMM1ldH2zxiP5cz7IQ6HORrs8qdaG51ol6a7tzlVHgY-BpMA"
  },
  {
    "id": "5497139907902674817",
    "name": "mens-ministry.jpg",
    "html_url": "",
    "img_url": "https://lh3.googleusercontent.com/aida/ADBb0uinf8QcHwyEOoTqA2BfNX45m3oZeAbf_3KmY7T1RoN10eBwhdaPrcmBNLrkd0HP8M1pEVQA1B0itlhnkP30xkeb2m4FdPQzUuSODPH1m0USyk4G405_7QirWxfQndJNa-S1k7uoqMeGd4VetbZQDJYedRchx_oMRuOt9rNNuAfsyvkT0jcbODMtd93Y8ioTvszbXiM8QwL-W0ehqbFzP5lJZ7uK5vqqqKL-lK_MgvROyQmD4HWl9oHmVKvmVKBDVUWLPytmPkr8og"
  }
]

out_dir = "/Users/kcoleman/Development/webdev/gfgbc-redesign-2026/gfgbc-2026/stitch_downloads"
os.makedirs(out_dir, exist_ok=True)

for item in data:
    name_sanitized = item["name"].replace("/", "-").replace(" ", "_")
    
    if item["html_url"]:
        html_path = os.path.join(out_dir, f"{item['id']}_{name_sanitized}.html")
        print(f"Downloading {html_path}...")
        try:
            req = urllib.request.Request(item["html_url"], headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(html_path, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Failed to download HTML for {item['id']}: {e}")

    if item["img_url"]:
        img_ext = "png"
        if item["name"].endswith(".jpg"):
            img_ext = "jpg"
        elif item["name"].endswith(".png"):
            img_ext = "png"
            
        img_path = os.path.join(out_dir, f"{item['id']}_{name_sanitized}.{img_ext}")
        print(f"Downloading {img_path}...")
        try:
            req = urllib.request.Request(item["img_url"], headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Failed to download image for {item['id']}: {e}")

print("Done downloading!")
