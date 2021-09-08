times = ('ATLETICO-MG','PALMEIRAS','FLAMENGO','FORTALEZA','BRAGANTINO','CORIMTHIANS',
'FLUMINENSE','CUIABA','INTERNACIONAL','ATLÉTICO-GO','ATHLETICO-PR','CEARÁ','SANTOS',
'JUVENTUDE','BAHIA','SÃO PAULO','AMÉRICA-MG','GREMIO','SPORT','CHAPECOENSE')
print(f'Os cinco primeiros times são : {times[0:6]}')
print(f'Os ultimos 4 colocados são : {times[-4:]}')
print(f'Em ordem alfabética:{sorted(times)}')
print(f'Chapeconse está na posição {times.index("CHAPECOENSE")}')