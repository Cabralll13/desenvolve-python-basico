URLs = ["www.google.com", "www.gmail.com", "www.github.com", 
        "www.reddit.com", "www.yahoo.com"]

dominios = []

for url in URLs:
    nome_do_dominio = url[4:-4]
    dominios.append(nome_do_dominio)

print("URLs:", URLs)
print("dominios:", dominios)