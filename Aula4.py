import calculos as calc
from time import sleep
import random
def main():
    while True:
        print("-------------------------------")
        sleep(3)
        valores_sensor_comb, valores_sensor_temp, valores_sensor_bat = pega_valores()
        dict_sns = {'Comb':valores_sensor_comb, 'Temp':valores_sensor_temp, 'Bat':valores_sensor_bat}
        media_comb = calc.media(dict_sns['Comb'])
        media_temp = calc.media(dict_sns['Temp'])
        media_bat = calc.media(dict_sns['Bat'])
        
        print(f"\nValor do Combustível: {media_comb:5.2f}")
        print(f"\nValor da temperatura: {media_temp:5.2f}")
        print(f"\nValor da bateria:     {media_bat:5.2f}")
def pega_valores():
    div = 2
    list_comb = []
    list_temp = []
    list_bat = []
    for _ in range(div):
        list_comb.append(random.randrange(1,600))
        list_temp.append(random.randrange(1,600))
        list_bat.append(random.randrange(1,600))
    return list_comb, list_temp, list_bat

main()