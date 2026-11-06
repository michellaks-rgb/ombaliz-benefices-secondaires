# Après publication, exécuter : python generer_flashcode.py https://votre-adresse-publique
import sys,qrcode
if len(sys.argv)!=2 or not sys.argv[1].startswith('https://'):
    raise SystemExit('Indiquer l’URL publique HTTPS de l’application')
qrcode.make(sys.argv[1]).save('flashcode_ombaliz.png')
print('Flashcode créé : flashcode_ombaliz.png')
