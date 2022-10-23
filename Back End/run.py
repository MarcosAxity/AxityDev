import os

os.system('rm gender.json')
os.system('rm tweetsFeelings.json')

busqueda=input("Buscar Twitter: ")
os.system('python3 /var/www/src/private/Twitter/hackaton_analysis_v2.py ' + busqueda)
print('principal ok')
os.system('python3 /var/www/src/private/Twitter/demo-aws.py')
print('demo-aws ok')
os.system('python3 /var/www/src/private/Twitter/demo-aws4.py')
print('demo-aws4 ok')
os.system('python3 /var/www/src/private/Twitter/gender_bias.py')
print('Lo logramos !!')

