import csv

def processarDadosSpotify():
    nomeArquivo = "spotify-2023.csv"
    topMusicasPorAno = {}
    
    with open(nomeArquivo, 'r', encoding='latin-1') as f:
        leitor_csv = csv.reader(f)

        next(leitor_csv)

        for dados in leitor_csv:
            if len(dados) != 24:
                continue

            trackName = dados[0]
            artistName = dados[1]
            artistCountStr = dados[2]
            releasedYearStr = dados[3]
            streamsStr = dados[8]
            
            if not (artistCountStr.isdigit() and releasedYearStr.isdigit() and streamsStr.isdigit()):
                continue

            artistCount = int(artistCountStr)
            releasedYear = int(releasedYearStr)
            streams = int(streamsStr)
            
            if artistCount > 1:
                continue
            
            if 2012 <= releasedYear <= 2022:
                if releasedYear not in topMusicasPorAno or streams > topMusicasPorAno[releasedYear]['streams']:
                    topMusicasPorAno[releasedYear] = {
                        'track_name': trackName,
                        'artist_name': artistName,
                        'released_year': releasedYear,
                        'streams': streams
                    }
    
    listaFinal = []
    for ano in range(2012, 2023):
        if ano in topMusicasPorAno:
            musica = topMusicasPorAno[ano]
            listaFinal.append([
                musica['track_name'],
                musica['artist_name'],
                musica['released_year'],
                musica['streams']
            ])
            
    return listaFinal

resultado = processarDadosSpotify()
print("Lista com as músicas mais tocadas de cada ano (2012-2022):")
for item in resultado:
    print(item)