import pandas as pd

config = pd.read_json('config.json')
print('This is the actual config: ')
print(config)


entrada = input('If you want to change the link, press "E", otherwise press "Enter".')
if entrada == 'e':
    new_link = input('Enter link here: ')
    config.link[0] = new_link
    config.to_json('config.json')
else:
    pass

"""while True:
    print('If you want to change anything, press "C"')
    
    entrada = input()"""
    


